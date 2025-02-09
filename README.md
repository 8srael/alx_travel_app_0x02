# Chapa API Integration for Payment Processing in Django

## 📌 Overview  
This project integrates **Chapa API** to handle online payments in a **Django** application. It allows users to **initiate payments, verify transactions**, and manage payment records securely.

## 🚀 Features  
- **Secure Payment Processing** with Chapa API  
- **Unique Transaction References** using UUID  
- **Automatic Payment Status Updates**  
- **Django REST Framework API Endpoints**  

---

## 🛠️ Setup Instructions  

### **1. Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/your-repo-name.git
cd your-repo-name
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**  
Create a `.env` file in the project root and add your Chapa API credentials:
```
CHAPA_SECRET_KEY=your_chapa_secret_key
SITE_URL=http://127.0.0.1:8000
```

### **5. Apply Migrations**
```bash
python manage.py migrate
```

### **6. Run the Django Server**
```bash
python manage.py runserver
```

---

## 🔗 API Endpoints  

### **1️⃣ Initiate Payment**  
**URL:** `POST /api/pay/`  
**Description:** Creates a new payment and returns a **Chapa checkout URL** for the user.  
#### **Request Body:**
```json
{
    "tel": "+123456789",
    "email": "user@example.com",
    "amount": "100.00"
}
```
#### **Response:**
```json
{
    "message": "Payment initiated",
    "checkout_url": "https://checkout.chapa.co/..."
}
```

### **2️⃣ Verify Payment Status**  
**URL:** `GET /api/pay/verify/{payment_reference}/`  
**Description:** Verifies the payment status with Chapa and updates the database.  
#### **Response (Success):**
```json
{
    "status": "Success",
    "message": "Payment verified successfully"
}
```
#### **Response (Failed Payment):**
```json
{
    "status": "Failed",
    "message": "Payment verification failed"
}
```

---

## 📂 Project Structure  

```
📦 alx_travel_app
 ┣ 📂 alx_travel_app
 ┃ ┣ 📂 alx_travel_app
 ┃ ┣ 📂 listings
 ┃ ┃ ┣ 📜 models.py   # Payment model is here 👈🏽
 ┃ ┃ ┣ 📜 views.py    # API Views
 ┃ ┃ ┣ 📜 serializers.py
 ┃ ┃ ┣ 📜 urls.py
 ┃ 📜 manage.py
 ┃ 📜 README.md
 ┃ 📜 .gitignore
 ┗ 📜 requirements.txt
```

---

## ⚡ Technologies Used  
- **Python 3**  
- **Django & Django REST Framework**  
- **Chapa API** for payments  

---

## 👨‍💻 Contributors  
- **Your Name** ([@8srael](https://github.com/8srael))  

---
