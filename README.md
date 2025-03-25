
# 🚀 Gen AI-Based Email Classification and OCR  

## 📌 Table of Contents  
- [Introduction](#introduction)  
- [Demo](#demo)  
- [Inspiration](#inspiration)  
- [What It Does](#what-it-does)  
- [How We Built It](#how-we-built-it)  
- [Challenges We Faced](#challenges-we-faced)  
- [How to Run](#how-to-run)  
- [Tech Stack](#tech-stack)  
- [Team](#team)  

---

## 🎯 Introduction  
**Gen AI-Based Email Classification and OCR** is an intelligent solution designed to streamline email management by leveraging advanced AI techniques. The system automates the process of classifying emails, extracting content from attachments, and identifying duplicate entries. It not only categorizes emails into predefined categories but also assigns a **confidence score** and **priority level** to ensure efficient handling.  

This solution automates tedious email processing tasks, reduces manual effort, and improves overall efficiency, making it an ideal tool for organizations that handle a high volume of emails and documents.  

## 🎥 Demo  
📹 [Video Demo](#) (if available)  
🖼️ Screenshots:  

![Landing Page](artifacts/screenshots/LandingPage.PNG)  
*Landing Page - User interface to interact with the system.*

![Email Classification](artifacts/screenshots/EmailClassification.PNG)  
*Classifying emails into predefined categories.*

![Duplicate Detection](artifacts/screenshots/DuplicateDetection.PNG)  
*Identifying and eliminating duplicate emails.*

![Processing](artifacts/screenshots/Processing.PNG)  
*Real-time processing and extraction from attachments.*

## 💡 Inspiration  
Managing large volumes of emails manually can be overwhelming, especially when they contain important attachments such as invoices, reports, or contracts. Inspired by the need to streamline this process, we aimed to build an AI-powered solution that automates email classification and data extraction, saving time and minimizing human errors.

## ⚙️ What It Does  
### Key Features:  
1. 📧 **Email Classification:** Classifies incoming emails into predefined categories using cutting-edge AI models.  
2. 📎 **Attachment Processing & OCR:** Extracts relevant information from email attachments (PDFs, images, scanned documents) using advanced OCR technology.  
3. 🔁 **Duplicate Detection:** Identifies and eliminates duplicate emails and attachments to avoid redundant processing.  
4. 🎯 **Confidence Score & Priority Assignment:** Each classified email is assigned a confidence score and priority level, ensuring critical emails receive immediate attention.  
5. 📝 **Summary Generation:** Generates concise summaries of email content and extracted data, enabling quick decision-making.  

## 🛠️ How We Built It  
- **AI Model:** Fine-tuned a large language model (LLM) for email classification.  
- **OCR Engine:** Integrated Tesseract OCR for accurate text extraction.  
- **Backend:** Developed using Flask/FastAPI for seamless API integration.  
- **Frontend:** Built a user-friendly interface using React for email visualization.  
- **Email Parsing:** Utilized IMAP/SMTP protocols to retrieve and process emails.  

## 🚧 Challenges We Faced  
- 🔥 **Model Tuning:** Fine-tuning the AI model for high accuracy in classifying diverse email content.  
- 📄 **OCR Accuracy:** Handling noisy and low-quality scanned documents to extract relevant data effectively.  
- 🕒 **Real-Time Processing:** Ensuring real-time processing of incoming emails without latency.  
- 🔐 **Security Concerns:** Safeguarding sensitive email content during processing and storage.  

## 🏃 How to Run  
Follow these steps to set up and run the project locally:

1. **Clone the repository**  
   ```sh
   git clone https://github.com/your-repo.git
   ```
2. **Navigate to the project directory**  
   ```sh
   cd gen-ai-email-classification
   ```
3. **Install dependencies**  
   - For backend:  
     ```sh
     pip install -r requirements.txt
     ```
   - For frontend:  
     ```sh
     cd client
     npm install
     ```

4. **Run the backend server**  
   ```sh
   python app.py  # or uvicorn main:app --reload (for FastAPI)
   ```

5. **Run the frontend**  
   ```sh
   npm start  # inside the client directory
   ```

6. **Open in Browser**  
   ```
   http://localhost:3000
   ```

## 🏗️ Tech Stack  
- 🔹 **Frontend:** React / Vue / Angular  
- 🔹 **Backend:** Flask / FastAPI  
- 🔹 **AI Models:** OpenAI API / Custom Fine-Tuned LLM  
- 🔹 **OCR Engine:** Tesseract / EasyOCR  
- 🔹 **Database:** PostgreSQL / MongoDB  
- 🔹 **Email Protocols:** IMAP / SMTP  
- 🔹 **Other:** REST APIs, JWT Authentication  

## 👥 Team  
- **Your Name** - [GitHub](#) | [LinkedIn](#)  
- **Teammate 2** - [GitHub](#) | [LinkedIn](#)  

---

✅ **Feel free to raise an issue or contribute by submitting a pull request!**  
📧 For any inquiries, reach out to us at [your-email@example.com](mailto:your-email@example.com).  
