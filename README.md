
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

![Processing](artifacts/screenshots/Processing.PNG)  
*Real-time processing and extraction from attachments.*

![Email Classification](artifacts/screenshots/EmailClassification.PNG)  
*Classifying emails into predefined categories.*

![Duplicate Detection](artifacts/screenshots/DuplicateDetection.PNG)  
*Identifying and eliminating duplicate emails.*

## 💡 Inspiration  
In the current process, a team receives a significant volume of **emails**, many of which contain **attachments** and long email chains. Each email requires **manual investigation**, with the team—referred to as *Gatekeepers*—spending substantial time reading the emails, analyzing the content of **attachments**, identifying the **intent** behind each message, and classifying the **request type** and **sub-request type**. Additionally, **key attributes** must be extracted to raise further actions and forward the email to the appropriate teams for resolution.  

This **manual process** is not only **time-consuming** but also **error-prone**, **inefficient**, and burdensome. The sheer volume of emails leads to **delays**, and the complexity of handling attachments and varying email formats increases the likelihood of **mistakes** or **missed information**. The repetitive nature of this work is mentally exhausting and can impact team **productivity** and **decision-making**.

Seeing the opportunity for improvement, we were inspired to create an **AI-powered solution** that could **automate** these time-consuming tasks. By leveraging **machine learning** and **natural language processing (NLP)** techniques, we envisioned a system capable of **classifying emails**, extracting **key data** from attachments, **detecting duplicates**, and generating **summaries**—all in **real time**. This solution aims to reduce the **manual effort**, improve **efficiency**, and enhance **accuracy**, allowing the team to focus on more critical tasks and making the entire email management process **faster**, more **reliable**, and **scalable**.

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
