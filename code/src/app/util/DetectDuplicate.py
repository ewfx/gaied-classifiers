import os
import hashlib
import re
import pandas as pd
from email import message_from_file
import extract_msg
from datetime import datetime
import difflib

def detect_duplicates(folder_path):
    """Main function to detect duplicates, replies, and forwards in a folder."""
    email_groups = process_emails(folder_path)
    data = prepare_dataframe(email_groups)

    if data:
        df = pd.DataFrame(data, columns=["Group ID", "Group Hash", "Filename", "Subject", "Date", "Type", "Latest"])
        df = df.sort_values(by=["Group ID", "Date"], ascending=[True, False])
        return df
    else:
        print("✅ No duplicate, reply, or forward emails found. Returning empty DataFrame.")
        return pd.DataFrame(columns=["Group ID", "Group Hash", "Filename", "Subject", "Date", "Type", "Latest"])


def process_emails(folder_path):
    """Process all emails in the folder and group related ones."""
    email_groups = {}
    group_counter = 1

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.endswith(".msg"):
            subject, body, date = get_msg_subject_body_date(file_path)
        elif filename.endswith(".eml"):
            subject, body, date = get_eml_subject_body_date(file_path)
        else:
            continue  # Skip non-email files

        email_hash = hash_subject_body(subject, body)

        # Group emails with similar hashes
        matched_group = find_similar_group(email_hash, email_groups, subject, body)

        if matched_group:
            email_groups[matched_group]["emails"].append({'filename': filename, 'subject': subject, 'date': date})
        else:
            email_groups[email_hash] = {
                "group_id": group_counter,
                "emails": [{'filename': filename, 'subject': subject, 'date': date}]
            }
            group_counter += 1
    
    return email_groups


def prepare_dataframe(email_groups):
    """Prepare data for DataFrame with related email groups."""
    data = []
    for email_hash, group in email_groups.items():
        group_id = group["group_id"]
        emails = group["emails"]
        
        if len(emails) > 1:  # Only include groups with replies/forwards/duplicates
            sorted_emails = sorted(emails, key=lambda x: x['date'], reverse=True)
            latest_email = sorted_emails[0]

            for email in sorted_emails:
                email_type = get_email_type(email['subject'])
                data.append({
                    "Group ID": group_id,
                    "Group Hash": email_hash,
                    "Filename": email['filename'],
                    "Subject": email['subject'],
                    "Date": email['date'],
                    "Type": email_type,
                    "Latest": "✅" if email['filename'] == latest_email['filename'] else ""
                })
    return data


def get_msg_subject_body_date(msg_path):
    """Extract subject, body, and date from .msg file."""
    msg = extract_msg.Message(msg_path)
    subject = clean_subject(msg.subject if msg.subject else "")
    body = clean_body(msg.body if msg.body else "")
    date = msg.date if msg.date else "1970-01-01 00:00:00"
    msg.close()
    return subject, body, parse_date(date)


def get_eml_subject_body_date(eml_path):
    """Extract subject, body, and date from .eml file."""
    with open(eml_path, 'r', encoding='utf-8', errors='ignore') as f:
        msg = message_from_file(f)
    subject = clean_subject(msg.get('Subject', ''))
    body = ''
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                body += part.get_payload(decode=True).decode('utf-8', errors='ignore')
    else:
        body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
    body = clean_body(body)
    date = msg.get('Date', '1970-01-01 00:00:00')
    return subject, body, parse_date(date)


def clean_subject(subject):
    """Clean the subject by removing Re: and Fwd: prefixes."""
    return re.sub(r'(?i)^(re:|fwd:)\s*', '', subject).strip()


def clean_body(body):
    """Clean the body by removing quoted/reply/forwarded content."""
    clean_body = re.sub(r'(?m)^>.*$', '', body)  # Remove quoted lines
    clean_body = re.split(
        r'(?i)(-----Original Message-----|From:|Forwarded message|Subject:|Sent:|To:)', 
        clean_body,
        maxsplit=1
    )[0]
    return clean_body.strip()


def parse_date(date_str):
    """Parse date string and return datetime object."""
    try:
        return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z')
    except (ValueError, TypeError):
        return datetime(1970, 1, 1)


def hash_subject_body(subject, body):
    """Create a hash of the subject and the first 50 words of the cleaned body."""
    content = subject.strip() + " ".join(body.strip().split()[:50])
    return hashlib.md5(content.encode('utf-8')).hexdigest()


def find_similar_group(email_hash, email_groups, subject, body):
    """Find a similar group based on subject and partial body similarity."""
    for existing_hash, group in email_groups.items():
        existing_subject = group["emails"][0]['subject']
        similarity_ratio = subject_similarity(subject, existing_subject)

        # If similar subject and body, group them together
        if similarity_ratio > 0.85 and hash_subject_body(existing_subject, body) == email_hash:
            return existing_hash
    return None


def subject_similarity(subject1, subject2):
    """Calculate similarity ratio between two subjects."""
    return difflib.SequenceMatcher(None, subject1, subject2).ratio()


def get_email_type(subject):
    """Identify email type based on subject."""
    subject_lower = subject.lower()
    if subject_lower.startswith("re:"):
        return "Reply"
    elif subject_lower.startswith("fwd:"):
        return "Forward"
    return "Original"

