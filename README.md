# 🚀 Gen AI-Based Email Classification and OCR

## 📌 Table of Contents
- [Introduction](#🎯-introduction)
- [Demo](#🎥-demo)
- [Inspiration](#💡-inspiration)
- [What It Does](#⚙️-what-it-does)
- [How We Built It](#🛠️-how-we-built-it)
- [How to Run](#🏃-how-to-run)
- [Project Structure](#📂-project-structure)
- [Challenges We Faced](#🚧-challenges-we-faced)
- [Tech Stack](#🏗️-tech-stack)
- [Team](#👥-team)

---

## 🎯 Introduction

**Gen AI-Based Email Classification and OCR** is an intelligent solution designed to streamline email management by leveraging advanced AI techniques. The system automates the process of classifying emails, extracting content from attachments, and identifying duplicate entries. It not only categorizes emails into predefined categories but also assigns a **confidence score** and **priority level** to ensure efficient handling.

This solution automates tedious email processing tasks, reduces manual effort, and improves overall efficiency, making it an ideal tool for organizations that handle a high volume of emails and documents.

---

## 🎥 Demo

📹 [Video Demo](#) (if available)  
🖼️ Screenshots:

![Landing Page](artifacts/screenshots/LandingPage.PNG)  
*Landing Page - User interface to interact with the system.*

![Processing](artifacts/screenshots/Processing.PNG)  
*Real-time processing and extraction from attachments.*

![Email Classification](artifacts/screenshots/EmailClassification.PNG)  
*Classifying emails into predefined categories.*

![Duplicate Detection](artifacts/screenshots/DuplicateDetection.PNG)  
*Identifying and eliminating duplicate emails.*

---

## 💡 Inspiration

Organizations dealing with a **large volume of emails** require manual investigation for classification, intent detection, attachment analysis, and forwarding actions. This process is:

- ⏳ **Time-consuming**
- ❌ **Error-prone**
- 🧠 **Mentally exhausting**

To **automate and optimize** this workflow, we developed an **AI-powered system** that performs **real-time email classification, content extraction, and summarization**—freeing teams to focus on **critical tasks**.

---

## ⚙️ What It Does

- 📧 **Email Classification:** Classifies incoming emails into predefined categories using cutting-edge AI models.
- 📎 **Attachment Processing & OCR:** Extracts relevant information from email attachments (PDFs, images, scanned documents) using advanced OCR technology.
- 🔁 **Duplicate Detection:** Identifies and eliminates duplicate emails and attachments to avoid redundant processing.
- 🎯 **Confidence Score & Priority Assignment:** Each classified email is assigned a confidence score and priority level, ensuring critical emails receive immediate attention.
- 📝 **Summary Generation:** Generates concise summaries of email content and extracted data, enabling quick decision-making.

---

## 🛠️ How We Built It

### **Technologies, Frameworks, and Tools**

#### **Generative AI Model**
- **Google Gemini**: Used for text classification and summarization tasks.

#### **Python Libraries**
- **Tesseract**: OCR tool for extracting text from scanned or image-based PDFs.
- **PDFPlumber**: For extracting text from PDFs while preserving document structure.
- **Pandas**: Used for managing and processing email data.

#### **Web Framework**
- **Flask**: Lightweight Python framework for building the UI and API.

---

## 🏃 How to Run

1. **Clone the repository**
   ```sh
   git clone https://github.com/ewfx/gaied-classifiers.git
   cd gaied-classifiers
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Update Configuration**
   - Update `config.py` to input your **GenAI API Key for Gemini** and **Tesseract path** from your system.

4. **Ensure Emails are in the Correct Folder**
   - Make sure all emails that need to be processed are placed inside the folder:  
     ```sh
     app/Emails
     ```

5. **Run the Application**
   ```sh
   python src/app.py
   ```

6. **Access the Application**
   - Open your browser and go to:
     ```
     http://127.0.0.1:5000/
     ```

7. **Start Processing**
   - Click on **Start** to begin processing emails.

---

## 📂 Project Structure

```
📦 gaied-classifiers  
├── 📂 artifacts  
│   ├── 📂 arch              # Tech architecture  
│   ├── 📂 demo              # Video Demo  
│   ├── 📂 presentation      # Presentation PPT  
│   ├── 📂 screenshots       # Screenshots  
│  
├── 📂 code  
│   ├── 📂 src  
│   │   ├── 📂 app  
│   │   │   ├── categories.xlsx      # Request Types and Sub Types  
│   │   │   ├── main.py              # Main logic  
│   │   │   ├── prompt.txt           # Prompt templates  
│   │   │   ├── 📂 DataFrames        # Folder to hold in-process CSV files  
│   │   │   ├── 📂 Emails            # Folder to store emails for processing  
│   │   │   ├── 📂 Processing        # Folder for execution process  
│   │   │   ├── 📂 util              # Utility scripts  
│   │   │   │   ├── detectDuplicate.py      # Detect duplicates  
│   │   │   │   ├── extractTextFromAttachment.py  # Extract text from email attachments  
│   │   │   │   ├── genAIProcessing.py         # General AI processing logic  
│   │   │   │   ├── processEmails.py           # Process emails  
│   │   │   │   ├── workspaceSetup.py          # Workspace setup utilities  
│   │   ├── 📂 static                # Static files (e.g., images, CSS, JS)  
│   │   │   ├── 📂 css               # CSS folder  
│   │   │   │   ├── styles.css       # Stylesheet for the project  
│   │   ├── 📂 templates             # Template files (e.g., HTML)  
│   │   │   ├── index.html           # Main HTML file  
│   │   ├── app.py                  # App entry point  
│   │   ├── config.py               # Configuration settings  
│   │   ├── requirements.txt        # Python dependencies  
├── .gitignore                     # Git ignore file  
├── LICENSE                         # Project license  
├── README.md                       # Project documentation  

```

---

## 🚧 Challenges We Faced

During the development of this project, we encountered several technical challenges that required innovative solutions. Below are some of the key challenges and how we addressed them:

### **1. OCR Accuracy**
- **Challenge:** Extracting data from scanned or image-based PDFs proved difficult due to the inherent issues of noise, low image quality, and irregular fonts, which often resulted in inaccurate text recognition.
- **Solution:** To overcome this, we utilized **Tesseract OCR** along with various pre-processing techniques, including image resizing, contrast enhancement, and noise reduction. These steps significantly improved the accuracy of the data extraction, ensuring more reliable results from scanned documents.

### **2. Real-Time Processing**
- **Challenge:** Processing emails and attachments in real-time posed a significant challenge, especially when dealing with a large volume of incoming data. The system needed to handle high throughput without introducing delays in processing.
- **Solution:** To ensure seamless real-time processing, we optimized the backend by breaking down tasks into smaller, more manageable chunks. Additionally, we leveraged asynchronous processing methods, allowing the system to maintain performance even under heavy load, thus ensuring smooth and efficient data handling.

### **3. Handling Diverse Attachment Types**
- **Challenge:** Attachments in emails came in various formats (such as PDFs, Word documents, images, and spreadsheets), each requiring distinct processing techniques for accurate data extraction. This diversity increased the complexity of the system.
- **Solution:** To handle this, we integrated multiple specialized libraries. **PDFPlumber** was used for structured PDF extraction, while **Tesseract OCR** was implemented to process scanned PDFs and image-based attachments. This multi-library approach enabled us to extract data across diverse formats efficiently, ensuring a high level of accuracy and consistency.


---

## 👥 Team

- **Varun Bansal** (Captain) - [GitHub](https://github.com/VarunBansal126) | [LinkedIn](https://www.linkedin.com/in/varun-bansal-58345a12b/)  
- **Dipak Nayak**  
- **Kazhian Muthusami**  
- **Swarnlata Singh**  
- **Manish Pandey**  
