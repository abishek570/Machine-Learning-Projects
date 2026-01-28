# ❤️ Heart Disease Prediction System

An end-to-end Machine Learning–based web application designed to predict the likelihood of heart disease using clinically relevant patient health parameters.  
The system integrates a trained classification model with a FastAPI backend and a responsive, user-friendly web interface for real-time risk assessment.

---

## 📌 Project Overview

Cardiovascular diseases remain one of the leading causes of mortality worldwide. Early detection and risk assessment play a critical role in prevention and treatment planning.  

This project aims to provide an **AI-assisted clinical decision support system** that evaluates heart disease risk based on patient data such as age, blood pressure, cholesterol levels, ECG results, exercise response, and other medically significant indicators.

> **Disclaimer:**  
> This project is intended strictly for **educational and research purposes** and must not be considered a replacement for professional medical diagnosis or treatment.

---

## 🧠 Machine Learning Details

- **Problem Type:** Binary Classification  
- **Algorithm Used:** Logistic Regression  
- **Target Variable:** Heart Disease Presence (0 = No, 1 = Yes)  
- **Input Features:** 13 clinical parameters  
- **Model Serialization:** Joblib  

The model is trained on a structured heart disease dataset and optimized for real-time inference through an API endpoint.

---

## 🏗️ System Architecture

User Interface (HTML / CSS / JavaScript)

↓

FastAPI Backend

↓

Trained ML Classification Model

↓

Prediction Output (0 or 1)


---

## ✨ Key Features

- Clinically inspired and validated input parameters  
- Interactive medical assessment form with input validation  
- Real-time prediction using a trained ML model  
- Clean and responsive user interface  
- Modular and scalable project structure  
- Suitable for academic demonstration and portfolio presentation  

---

## 📁 Project Structure

```
├── app.py # FastAPI application for running the web app
|
├── train.py # Training script for the ML model
|
├── evaluate.py # Evaluation script for model assessment
|
├── heart.csv # Heart disease dataset
|
├── requirements.txt # Project dependencies
|
├── model/
| |
│ └── Heart_disease_model.joblib
|
├── templates/
| |
│ ├── index.html # Landing page
| |
│ └── formpage.html # Patient assessment form
|
├── static/
| |
│ ├── style_index.css
| |
│ └── style_formpage.css
|
├── .gitignore
|
└── README.md

```

---

## ⚙️ Installation & Setup

1. Clone the repository  
2. Create and activate a virtual environment (recommended)  
3. Install dependencies using `requirements.txt`  
4. **Train the model using `train.py`** (Run this first to create the trained model)  
5. (Optional) Evaluate the model using `evaluate.py`  
6. Run the FastAPI application using `app.py`  

The application runs locally and provides both a UI and API-based prediction interface.

---

## 🔌 API Overview

### Endpoint: `/prediction`  
- **Method:** POST  
- **Input:** 13 clinical features per patient  
- **Output:**  
  - `0` → Low risk / No heart disease detected  
  - `1` → High risk / Heart disease likely  

**Request Body**
```json
{
  "features": [[
    age, sex, cp, trestbps, chol, fbs,
    restecg, thalach, exang, oldpeak,
    slope, ca, thal
  ]]
}
```
**Response**
```json output
{
  "prediction": 0
}
```

The API performs input validation before generating predictions.

---

## 📊 Results & Evaluation

Model performance metrics on the test dataset:

- **Accuracy Score:** Measures the proportion of correct predictions out of total predictions  
- **Precision Score:** Indicates the accuracy of positive predictions (true positives / all positive predictions)  
- **Recall Score:** Measures the model's ability to identify all actual positive cases (true positives / all actual positives)  
- **F1-Score:** The harmonic mean of precision and recall, providing a balanced metric  
- **ROC-AUC Score:** Evaluates the model's ability to distinguish between classes across all classification thresholds  
- **Confusion Matrix:** Visual representation of true positives, true negatives, false positives, and false negatives  

Run `python evaluate.py` to view the detailed metrics and confusion matrix visualization.  

---

## � Deployment on AWS

This application has been successfully deployed on AWS EC2. Follow the steps below to deploy on your own AWS instance:

### Prerequisites
- AWS Account with free tier access
- Putty (SSH client for Windows) or SSH client
- Generated `.pem` key file for EC2 instance authentication

### Deployment Steps

1. **Create EC2 Instance**
   - Log in to AWS Management Console
   - Navigate to EC2 Dashboard
   - Create a new instance with `t3.micro` (free tier eligible)
   - Configure security groups to allow HTTP (port 80), HTTPS (port 443), and SSH (port 22)
   - Download the `.pem` key file during instance creation

2. **Launch the Instance**
   - Start the EC2 instance from the AWS Console
   - Wait for the instance to enter "running" state
   - Note down the instance's **Public IP address**

3. **Access the Instance via SSH**
   - Open Putty (SSH client)
   - Configure connection with:
     - **Host Name:** `ec2-user@<your-public-ip>` (for Amazon Linux) or `ubuntu@<your-public-ip>` (for Ubuntu)
     - **Port:** 22
     - **Auth:** Select your `.pem` key file (convert to `.ppk` format if needed)
   - Click "Open" to establish SSH connection

4. **Deploy Project Files**
   - Clone or push all project files to the EC2 instance
   - Install dependencies: `pip install -r requirements.txt`
   - Train the model: `python train.py`
   - (Optional) Evaluate the model: `python evaluate.py`

5. **Run the Application**
   - Start the FastAPI server: `python app.py`
   - Access the application using the EC2 instance's **Public IP address** in your browser
   - Example: `http://<your-public-ip>:8001`

The application will now be accessible from anywhere with internet access!

---

## �🔮 Future Enhancements

- Integrate feature scaling and pipelines  
- Compare multiple ML models (SVM, Random Forest, XGBoost) 
- Store patient prediction history 
- Deploy on cloud platforms (AWS / Azure / GCP)  

---

## 👨‍💻 Author

**John Abishek Jaisingh P**  
Final Year Electronics and Communication Engineering Student  
Machine Learning & AI Enthusiast  

---

## 📜 License

This project is developed for **academic and educational use** only.

---

## 🙏 Acknowledgements

- Scikit-learn  
- FastAPI  
- UCI Heart Disease Dataset  
- Open-source developer community  

---

⭐ If you find this project useful, consider starring the repository.
