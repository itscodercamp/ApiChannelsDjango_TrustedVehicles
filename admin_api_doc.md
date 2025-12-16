# Admin API Documentation

Base URL: `/api/admin`
Authentication: **Requires Admin User** (Staff status).
Header: `Authorization: Bearer <admin_token>`

> **Admin Login (Employee/Staff)**
> Endpoint: `POST /api/auth/employee/login`
> Body: `{"email": "admin@example.com", "password": "..."}`
> Response: Returns `token` (JWT) and `user` details including `is_staff`, `is_superuser`.

> These APIs follow standard REST patterns (GET list, POST create, GET detail, PUT update, DELETE).
> All responses are standard JSON. Lists are paginated (optional) or full (depending on config).

## 1. Authentication & Users

### List/Filter Users
- **Endpoint**: `GET /api/admin/users/`
- **Filters**:
  - `?user_type=Dealer` or `Customer`
  - `?city=Mumbai`
  - `?search=rahul` (searches full_name, email, phone, dealership_name)
- **Response**:
```json
[
  {
    "id": 1,
    "user_type": "Dealer",
    "full_name": "Rahul Motors",
    "phone": "9988776655",
    "email": "dealer@example.com",
    "dealership_name": "Rahul Motors Pvt Ltd",
    "dealership_type": "Franchise",
    "city": "Mumbai",
    "state": "MH",
    "pincode": "400001",
    "created_at": "2023-01-01T12:00:00Z"
  }
]
```

### Create User
- **Endpoint**: `POST /api/admin/users/`
- **Body**: Same fields as response. `password` is required and will be hashed unique.

---

## 2. Marketplace Management

### Vehicles (Inventory)
> Detailed Vehicle Object is same as Marketplace API documentation.
- **List**: `GET /api/admin/marketplace/vehicles/`
  - Filters: `?status=For Sale`, `?search=Creta`
- **Create**: `POST /api/admin/marketplace/vehicles/` (Multipart/Form-data)
- **Update**: `PUT /api/admin/marketplace/vehicles/{id}/` (Multipart)
  - Toggle `verified` status here: `verified=true`.
  - Change status: `status=Sold`.

### Inquiries (Messages)
- **List**: `GET /api/admin/marketplace/inquiries/`
- **Filters**: `?vehicle={ID}`, `?user={ID}`
- **Response**:
```json
[
  {
    "id": 5,
    "vehicle": "TVI-000000001", // Vehicle ID
    "user": 1, // User ID
    "message": "Is this negotiable?",
    "offer_price": 500000.00,
    "created_at": "..."
  }
]
```

### Banners
- **List**: `GET /api/admin/marketplace/banners/`
- **Create**: `POST /api/admin/marketplace/banners/`
- **Body**: `title` (text), `image` (file), `is_active` (boolean).

---

## 3. Website Requests (Leads)

### Sell Car Requests
- **Endpoint**: `GET /api/admin/website/sell-requests/`
- **Search**: `?search=phone_or_name`
- **Response**:
```json
{
  "make": "Hyundai",
  "model": "Creta",
  "variant": "SX",
  "regNumber": "MH01AB1234",
  "regYear": 2020,
  "fuelType": "Diesel",
  "ownership": "1st",
  "transmission": "Manual",
  "kmDriven": 35000,
  "state": "Maharashtra",
  "city": "Mumbai",
  "address": "Full Address...",
  "name": "Seller Name",
  "phone": "9876543210",
  "scheduledDate": "2024-01-15"
}
```

### Loan Applications
- **Endpoint**: `GET /api/admin/website/loan-requests/`
- **Response**:
```json
{
  "name": "Applicant Name",
  "mobile": "9876543210",
  "income": 50000.00,
  "loanAmount": 300000.00,
  "employmentType": "Salaried"
}
```

### Insurance Leads
- **Endpoint**: `GET /api/admin/website/insurance-leads/`
- **Response**:
```json
{
  "regNumber": "MH02...",
  "name": "Owner Name",
  "mobile": "9876543210",
  "policyType": "Comprehensive",
  "expiryDate": "2024-02-01"
}
```

### PDI Booking
- **Endpoint**: `GET /api/admin/website/pdi-requests/`
- **Response**:
```json
{
  "name": "User",
  "email": "u@x.com",
  "phone": "...",
  "city": "...",
  "make": "...",
  "model": "...",
  "scheduledDate": "..."
}
```

### Dealer Demo Requests
- **Endpoint**: `GET /api/admin/website/dealer-demos/`
- **Response**:
```json
{
  "name": "User",
  "phone": "...",
  "email": "...",
  "dealershipName": "ABC Motors"
}
```

### Contact Messages
- **Endpoint**: `GET /api/admin/website/contacts/`
- **Response**:
```json
{
  "firstName": "John",
  "lastName": "Doe",
  "email": "john@example.com",
  "subject": "Help",
  "message": "..."
}
```
