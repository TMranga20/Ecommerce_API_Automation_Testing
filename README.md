# 🛒 E-Commerce API Automation Testing

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Pytest](https://img.shields.io/badge/Pytest-Framework-green?logo=pytest)
![Requests](https://img.shields.io/badge/Requests-HTTP-orange)
![Allure](https://img.shields.io/badge/Allure-Reports-purple)
![API Testing](https://img.shields.io/badge/API-Automation-red)

---

## 📌 Project Overview

Automated REST API testing for an E-Commerce application using **Python, Pytest, and Requests**.
The framework validates **status codes, response structure, data integrity**, and generates **HTML & Allure interactive reports**.

---

## 🔧 Tech Stack

* Python
* Pytest
* Requests
* JSON Schema Validation
* Allure Reports
* HTML Reports
* VS Code

---

## 📁 Project Structure

```
ecommerce_api_automation/
│── tests/
│   ├── test_login.py
│   ├── test_products.py
│   └── test_cart.py
│
│── utils/
│   ├── api_client.py
│   ├── test_data.json
│   └── schemas.py
│
│── allure-results/
│── pytest.ini
│── requirements.txt
│── README.md
```

---

## 🚀 Features

✔ Reusable API client for GET, POST, DELETE requests
✔ Automated Login, Products, and Cart APIs
✔ JSON schema validation
✔ Smoke & Regression test tagging
✔ HTML report generation
✔ Allure interactive dashboard with:

* Feature & severity grouping
* Step logging
* Request & response attachments

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-api-automation.git
cd ecommerce-api-automation
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Tests

### Run All Tests

```bash
pytest
```

### Run Smoke Tests Only

```bash
pytest -m smoke
```

---

## 📊 HTML Report

Generated automatically after execution:

```
reports/report.html
```

Open in browser to view test results.

---

## 📈 Allure Interactive Report

### Generate Allure Results

```bash
pytest --alluredir=allure-results
```

### Open Allure Dashboard

```bash
allure serve allure-results
```

This provides:

* Test execution summary
* Step-level logs
* Request/response payloads
* Severity & feature grouping

---

## 🧪 Sample APIs Covered

* POST `/verifyLogin` → User login validation
* GET `/productsList` → Fetch all products
* POST `/addToCart` → Add product to cart
* DELETE `/removeFromCart` → Remove product from cart

Reference: https://automationexercise.com/api

---

## 🏷️ Test Markers

Configured in `pytest.ini`:

* `smoke` → Critical test cases
* `regression` → Full test suite

Run specific marker:

```bash
pytest -m regression
```

---

## 📜 Requirements

```
pytest
requests
jsonschema
pytest-html
allure-pytest
```

---

## 👨‍💻 Author

**Mohan Ranga Talari**
QA Automation Engineer (Fresher)
🔗 GitHub: https://github.com/TMranga20

---


```
```
