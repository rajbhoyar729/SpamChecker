
---

# **Spam Checker API**

## 📖 **Overview**

The **Spam Checker API** is a Django-based REST API that allows users to:
- Register and log in securely using phone-based authentication.
- Manage personal contacts and mark phone numbers as spam.
- Search for users by name or phone number.
- Access spam likelihood data to identify potential spam callers.

This application is built using the **Django REST Framework (DRF)** and utilizes **JWT tokens** for secure API access.

---

## 🎯 **Features**

### **Authentication**
- **User Registration**: Register using phone, name, password, and optional email.
- **Token-based Login**: Obtain access and refresh tokens using JWT.

### **Contact Management**
- Add, view, and manage personal contacts.
- Spam reporting: Mark phone numbers as spam and calculate spam likelihood based on reports.

### **Search**
- **Search by Name**: Look up users by their names.
- **Search by Phone Number**: Retrieve user details using a phone number.

### **Spam Likelihood**
- Displays the likelihood of a phone number being spam based on user feedback.

---

## 🛠️ **Tech Stack**

- **Backend**: Django, Django REST Framework
- **Authentication**: djangorestframework-simplejwt
- **Database**: SQLite (development)

---

## 🚀 **Setup Instructions**

### **Prerequisites**
- Python 3.8+
- Pipenv (for dependency management)

### **Installation**

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd  SpamChecker
   ```

2. **Install dependencies**:
   ```bash
   pipenv install
   ```

3. **Activate the virtual environment**:
   ```bash
   pipenv shell
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

---

## 📄 **API Documentation**

### **Endpoints**

#### **Authentication**
1. **Register**: `/api/register/` (POST)
   ```json
   {
       "name": "John Doe",
       "phone": "1234567890",
       "password": "password123",
       "email": "john@example.com"
   }
   ```

2. **Login**: `/api/login/` (POST)
   ```json
   {
       "phone": "1234567890",
       "password": "password123"
   }
   ```

   **Response**:
   ```json
   {
       "refresh": "<refresh_token>",
       "access": "<access_token>"
   }
   ```

#### **Contact Management**
1. **Add Contact**: `/api/contacts/` (POST, Auth Required)
   ```json
   {
       "name": "Jane Doe",
       "phone": "9876543210"
   }
   ```

2. **View Contacts**: `/api/contacts/` (GET, Auth Required)

#### **Spam Reporting**
1. **Mark Spam**: `/api/spam/` (POST, Auth Required)
   ```json
   {
       "phone": "9876543210",
       "is_spam": true
   }
   ```

#### **Search**
1. **Search by Name**: `/api/search/name/` (GET, Auth Required)
   - Query Parameter: `?name=Jane`

2. **Search by Phone Number**: `/api/search/phone/` (GET, Auth Required)
   - Query Parameter: `?phone=9876543210`

---

## 🧪 **Testing**

1. **Run Tests**:
   ```bash
   pytest
   ```

2. **Test Scenarios**:
   - User registration and login.
   - Token-based authentication.
   - Contact management and spam reporting.
   - Search functionality (name and phone).

---

## 📌 **Project Structure**

```plaintext
instahyre_hiring_challenge/
├── api/                    # Main app folder
│   ├── models.py           # Database models
│   ├── serializers.py      # API serializers
│   ├── views.py            # API views
│   ├── urls.py             # API routes
│   ├── tests.py            # Automated tests
├── spam_checker/           # Project settings and configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Root URL configurations
├── Pipfile                 # Dependency manager
├── Pipfile.lock            # Dependency lock file
├── README.md               # Project documentation
├── manage.py               # Django management script
└── db.sqlite3              # SQLite database (development)
```

---

## 🎗 **License**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---
