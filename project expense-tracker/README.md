# 💰 Expense Management System

The **Expense Management System** is a full-stack application that helps users track and manage their personal or business expenses. It consists of a **Streamlit-based frontend** for a clean and interactive user interface and a **FastAPI-based backend** that handles data storage and processing. The application is modular, test-driven, and designed for ease of deployment and further scalability.

---

## 🚀 Features

- 📊 Add, edit, delete, and view expenses  
- 🗓️ Date-wise and category-wise expense tracking  
- 🧠 Visual analytics using interactive charts and tables  
- 🔐 Secure API endpoints for seamless data communication  
- 💡 Test coverage for both frontend and backend  
 

---

## 🏗️ Project Structure

expense-tracker/
│
├── frontend/                         # Streamlit frontend application
│   ├── add_update_ui/               # UI for adding and updating expenses
│   ├── analytics_category/          # Category-wise analytics
│   ├── analytics_month/             # Month-wise analytics
│   └── app.py                       # Main Streamlit app entry point
│
├── backend/                         # FastAPI backend server code
│   ├── db_helper/                   # Database helper functions
│   ├── logging_setup/              # Logging configuration
│   └── server.py                    # Main FastAPI server script
│
├── tests/                           # Unit and integration test cases
│   ├── frontend.py                  # Tests for frontend components
│   ├── backend.py                   # Tests for backend endpoints
│   └── conftest.py                  # Test configuration and fixtures
│
├── requirements.txt                 # List of all Python dependencies
└── README.md                        # Project overview and usage instructions





---

## 🛠️ Tech Stack

| Component     | Technology         |
|---------------|--------------------|
| Frontend      | Streamlit          |
| Backend       | FastAPI            |
| Testing       | Pytest             |
| Data Handling | Pandas, JSON       |
| Deployment    | Uvicorn (for API)  |
| Package Mgmt  | pip + requirements.txt |

---





