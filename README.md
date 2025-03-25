
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

## How We Built It

### Technologies, Frameworks, and Tools  
1. **Generative AI Model**:  
   - **Google Gemini**: Used for text classification and summarization tasks.

2. **Python Libraries**:  
   - **Tesseract**: OCR tool for extracting text from scanned or image-based PDFs.  
   - **PDFPlumber**: For extracting text from PDFs while preserving document structure.  
   - **Pandas**: Used for managing and processing email data.

3. **Web Framework**:  
   - **Flask**: Lightweight Python framework for building the UI and API.

## 🚧 Challenges We Faced  
Throughout the development process, we encountered several challenges that required innovative solutions:

1. **OCR Accuracy**:  
   - **Challenge:** Extracting data from scanned or image-based PDFs often results in errors due to noise, low quality, or irregular fonts.  
   - **Solution:** We employed **Tesseract OCR** with pre-processing steps like image resizing and noise reduction to improve extraction accuracy.

2. **Real-Time Processing**:  
   - **Challenge:** Ensuring that emails and attachments are processed in real-time without significant delays, especially when handling large volumes of incoming data.  
   - **Solution:** Optimized backend processing by breaking down tasks into smaller, manageable chunks and using asynchronous processing methods to maintain performance under heavy load.

3. **Handling Diverse Attachment Types**:  
   - **Challenge:** Attachments came in many formats (e.g., PDFs, images, Word docs), each requiring different processing techniques for data extraction.  
   - **Solution:** Integrated multiple libraries like **PDFPlumber** for PDFs and **Tesseract** for OCR to ensure seamless extraction across formats.

4. **Security Concerns**:  
   - **Challenge:** Safeguarding sensitive email content during processing and storage, particularly when dealing with personal or confidential information.  
   - **Solution:** We implemented **data encryption**, used **secure servers**, and followed best practices to ensure that no sensitive data was exposed.

5. **Duplicate Detection**:  
   - **Challenge:** Identifying and removing duplicate emails and attachments, especially when emails were forwarded multiple times or included attachments in varying formats.  
   - **Solution:** Developed an algorithm to detect similarities in email content, subject, and attachments, enabling the system to flag duplicates effectively.

6. **Ensuring Scalability**:  
   - **Challenge:** As the system scales to handle larger volumes of emails, performance could degrade if not properly managed.  
   - **Solution:** We utilized **scalable cloud infrastructure** and optimized the processing pipelines to ensure smooth handling of increasing volumes of data, ensuring that performance is maintained even with growing demand.

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
- **Frontend:** Flask (Used for building the UI and handling API requests to interact with the backend)  
- **Backend:** Python (Flask for developing the backend logic and integrating the Google Gemini model for email classification and summarization)  
- **AI Model:** Google Gemini (Generative AI model for classifying emails, summarizing content, and extracting key insights)  
- **OCR:** Tesseract (For Optical Character Recognition to extract text from scanned PDFs and images), PDFPlumber (For reading and extracting structured text from PDFs)  

## 👥 Team  
- **Your Name** - [GitHub](#) | [LinkedIn](#)  
- **Teammate 2** - [GitHub](#) | [LinkedIn](#)  

---
