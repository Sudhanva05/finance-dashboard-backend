# Finance Dashboard Backend

## Overview

This project is a backend system for managing financial records with secure authentication and role-based access control. It allows users to create, view, and analyze financial data while enforcing access restrictions based on user roles.

---

## Features

### Authentication & Security

* JWT-based authentication
* Secure password hashing
* OAuth2 password flow integration
* Protected API endpoints

### Role-Based Access Control (RBAC)

* **Admin**: Can create financial records
* **User**: Can only view records

### Financial Records Management

* Create financial records (admin only)
* Retrieve all records (authenticated users)
* Associate records with users

### Filtering & Querying

* Filter by category (e.g., Income, Expense)
* Filter by minimum and maximum amount
* Flexible query parameters

### Dashboard & Analytics

* Total income calculation
* Total expense calculation
* Net balance computation

---

## Tech Stack

* **Backend Framework**: FastAPI
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy
* **Migrations**: Alembic
* **Authentication**: JWT (JSON Web Tokens)
* **API Documentation**: Swagger (OpenAPI)

---

## Project Structure

```
finance-backend/
│
├── app/
│   ├── core/        # Config, security
│   ├── db/          # Database setup
│   ├── models/      # SQLAlchemy models
│   ├── schemas/     # Pydantic schemas
│   ├── routes/      # API endpoints
│   └── main.py      # Entry point
│
├── alembic/         # Database migrations
├── .env             # Environment variables
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone <your-repo-url>
cd finance-backend
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/finance_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
```

---

## Running the Application

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

Access interactive docs:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Authentication

* `POST /auth/register` — Register new user
* `POST /auth/login` — Login and receive JWT token

### Records

* `GET /records/` — Get all records (with filters)
* `POST /records/` — Create record (admin only)
* `GET /records/summary` — Financial summary

---

## Example Request

### Create Record

```json
{
  "title": "Food",
  "amount": 200,
  "category": "Expense"
}
```

---

## Key Learnings

* Implemented secure authentication using JWT
* Designed role-based access control system
* Managed database schema using Alembic migrations
* Built scalable REST APIs with FastAPI
* Implemented filtering and aggregation logic

---

## Author

Sudhanva J Rao
