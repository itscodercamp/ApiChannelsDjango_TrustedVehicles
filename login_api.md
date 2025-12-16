# Admin & Inspector Login API Documentation

Use these endpoints to login to your Admin Panel or Inspection App.

## 1. Employee Login (Admin / Inspector)
This endpoint is for Staff, Admins, and Inspectors (who are registered as standard Django Users).

- **Endpoint**: `POST /api/auth/employee/login`
- **Request Body**:
```json
{
  "email": "employee@example.com",
  "password": "yourpassword"
}
```

- **Response (200 OK)**:
```json
{
  "message": "Login successful",
  "token": "eyJhbGciOiJIUzI1NiIsInR...", // JWT Token
  "user": {
    "id": 1,
    "email": "employee@example.com",
    "username": "employee",
    "is_staff": true,      // True for Admin/Staff
    "is_superuser": false  // True for SuperAdmin
  }
}
```

**Note**:
- Store the `token` in LocalStorage/Cookies.
- Send this token in headers for all subsequent requests: `Authorization: Bearer <token>`
- Use `is_staff` or `is_superuser` to control access in your frontend (e.g., show/hide "Manage Users" button).

## 2. Customer / Dealer Login
(Only for the public Marketplace App, DO NOT use for Admin Panel)
- **Endpoint**: `POST /api/auth/login`
- **Body**: `{"email": "...", "password": "..."}`
