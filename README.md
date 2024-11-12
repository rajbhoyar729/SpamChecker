Here’s the complete README rewritten in Markdown:

```markdown
# Spam Checker REST API

## 📍 Overview

Spam Checker is a REST API built using Django REST Framework. It serves as the backend for a mobile application that helps users identify spam phone numbers and perform reverse lookups by phone number or name. The API supports user registration, contact management, spam reporting, and search functionality while ensuring secure and scalable operations.

---

## 👾 Features

1. **User Authentication**:
   - Registration with phone, name, password, and optional email.
   - Token-based authentication using JWT (access and refresh tokens).

2. **Contact Management**:
   - Users can manage their personal contacts.
   - Automatically links uploaded contacts to the global database.

3. **Spam Reporting**:
   - Mark any phone number as spam.
   - Calculate the likelihood of a number being spam based on user reports.

4. **Search Functionality**:
   - **By Name**: Search for users or contacts by name with priority on exact matches.
   - **By Phone Number**: Look up users or contacts based on phone numbers.

5. **Secure API**:
   - All endpoints require authentication.
   - Email visibility restrictions based on user relationships.

6. **Database Population**:
   - Script for generating random users, contacts, and spam reports for testing purposes.

---

## 📁 Project Structure

```plaintext
spam_checker/
├── Pipfile                 # Dependency management
├── Pipfile.lock            # Dependency lockfile
├── README.md               # Project documentation
├── api/                    # Main app folder
│   ├── models.py           # Database models
│   ├── serializers.py      # API serializers
│   ├── views.py            # API views
│   ├── urls.py             # API endpoints
│   ├── tests.py            # Automated tests
│   ├── migrations/         # Database migrations
├── spam_checker/           # Project settings and WSGI configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # Root URL configuration
│   ├── wsgi.py             # WSGI configuration
│   ├── asgi.py             # ASGI configuration
├── db.sqlite3              # SQLite database (development only)
├── manage.py               # Django management script
├── populate_db.py          # Script to populate database with sample data
```

---

## 🚀 Getting Started

### ☑️ Prerequisites

- Python 3.8+
-django for backend
- Pipenv for dependency management

---

### ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>![git@github.com:rajbhoyar729/SpamChecker.git]
   cd spam_checker
   ```

2. Install dependencies using Pipenv:
   ```bash
   pipenv install
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

### 🤖 Usage

- **Register a User**:
  ```bash
  curl -X POST http://127.0.0.1:8000/api/register/ \
       -H "Content-Type: application/json" \
       -d '{"name": "John Doe", "phone": "1234567890", "password": "password123"}'
  ```

- **Login**:
  ```bash
  curl -X POST http://127.0.0.1:8000/api/login/ \
       -H "Content-Type: application/json" \
       -d '{"phone": "1234567890", "password": "password123"}'
  ```

- **Search by Name**:
  ```bash
  curl -X GET "http://127.0.0.1:8000/api/search/name/?name=John" \
       -H "Authorization: Bearer <access_token>"
  ```

- **Search by Phone**:
  ```bash
  curl -X GET "http://127.0.0.1:8000/api/search/phone/1234567890/" \
       -H "Authorization: Bearer <access_token>"
  ```

---

### 🧪 Testing

Run the test suite using pytest:
```bash
pipenv run pytest
```

---

## 📌 Roadmap

- Add role-based access controls.
- Introduce caching for spam likelihood calculations.
- Enhance search with fuzzy matching.

---

## 🔰 Contributing

1. Fork the repository and create a new branch:
   ```bash
   git checkout -b feature-name
   ```

2. Make your changes and commit them:
   ```bash
   git commit -m "Description of feature"
   ```

3. Push to your fork and submit a pull request.

---

## 🎗 License

This project is licensed under [MIT License](https://choosealicense.com/licenses/mit/).
```

