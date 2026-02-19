# 🛒 E-Commerce API Automation Testing Framework

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Pytest](https://img.shields.io/badge/Pytest-Framework-green?logo=pytest)
![Requests](https://img.shields.io/badge/Requests-HTTP-orange)
![Allure](https://img.shields.io/badge/Allure-Reports-purple)
![API Automation](https://img.shields.io/badge/API-Automation-red)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)
![Repo Size](https://img.shields.io/github/repo-size/TMranga20/Ecommerce_API_Automation_Testing)
![Git](https://img.shields.io/badge/Git-Version%20Control-orange?logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

---

## 📌 Project Overview

This project implements an **API Automation Testing Framework** for an E-Commerce application using:

* **Python**
* **Pytest**
* **Requests**
* **JSON Schema Validation**
* **Allure Reporting**

The framework validates **status codes, response body, schema, and data integrity**, and generates **HTML and Allure interactive reports**.

Reference APIs: https://automationexercise.com/api
---

## 🧰 Tech Stack

* Python 3.x
* Pytest
* Requests
* JSON Schema
* Allure Reports
* Pytest HTML Reports
* VS Code
* Git & GitHub

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
│   ├── config.py
│   ├── schemas.py
│   └── test_data.json
│
│── allure-results/
│── reports/
│── pytest.ini
│── requirements.txt
│── README.md
```

---

## 🚀 Key Features

✔ Reusable API client for GET, POST, DELETE requests

✔ Automated Login, Products, and Cart APIs

✔ JSON schema validation for response structure

✔ Data-driven testing using external JSON data

✔ Smoke & Regression test tagging

✔ HTML report generation

✔ Allure interactive dashboard with:

* Feature grouping
* Severity levels
* Step logging
* Request/Response attachments

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

## ▶️ Test Execution

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

Generated after execution:

```
reports/report.html
```

Open in a browser to view test results.

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

Provides:

* Execution summary
* Step-level logs
* Request & response payloads
* Severity & feature grouping

---

## 🧪 APIs Covered

* POST `/verifyLogin` → Validate user login
* GET `/productsList` → Fetch all products
* POST `/addToCart` → Add product to cart
* DELETE `/removeFromCart` → Remove product from cart

---

## 🏷️ Test Markers

Configured in `pytest.ini`:

* `smoke` → Critical test cases
* `regression` → Full test suite

Run by marker:

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

```
