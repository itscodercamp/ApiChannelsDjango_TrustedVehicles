# Complete Admin Panel API Documentation

**Base URL**: `https://apis.trustedvehicles.com/api`

---

## 🔐 Authentication

### Employee/Admin Login
**Endpoint**: `POST /api/auth/employee/login/`

**Request Body**:
```json
{
  "email": "admin@example.com",
  "password": "yourpassword"
}
```

**Response (200 OK)**:
```json
{
  "message": "Login successful",
  "token": "eyJhbGciOiJIUzI1NiIsInR...",
  "user": {
    "id": 1,
    "email": "admin@example.com",
    "username": "admin",
    "is_staff": true,
    "is_superuser": false
  }
}
```

**Error Responses**:
- `400` - Missing email/password
- `401` - Invalid credentials
- `403` - Account disabled

**Usage**: Store the `token` and use it in all subsequent requests:
```
Authorization: Bearer <token>
```

---

## 👥 User Management

### List All Users
**Endpoint**: `GET /api/admin/users/`

**Query Parameters**:
- `?user_type=Dealer` or `Customer`
- `?city=Mumbai`
- `?search=rahul` (searches name, email, phone, dealership)

**Response**:
```json
[
  {
    "id": 1,
    "user_type": "Dealer",
    "full_name": "Rahul Kumar",
    "phone": "9988776655",
    "email": "dealer@example.com",
    "dealership_name": "Rahul Motors Pvt Ltd",
    "dealership_type": "Franchise",
    "city": "Mumbai",
    "state": "MH",
    "pincode": "400001",
    "created_at": "2023-01-01T12:00:00Z",
    "updated_at": "2023-01-01T12:00:00Z"
  }
]
```

### Get Single User
**Endpoint**: `GET /api/admin/users/{id}/`

### Create User
**Endpoint**: `POST /api/admin/users/`

**Request Body**:
```json
{
  "user_type": "Customer",
  "full_name": "John Doe",
  "phone": "9876543210",
  "email": "john@example.com",
  "password": "securepassword",
  "city": "Delhi",
  "state": "DL",
  "pincode": "110001"
}
```

### Update User
**Endpoint**: `PUT /api/admin/users/{id}/`

**Request Body**: Same as Create

### Delete User
**Endpoint**: `DELETE /api/admin/users/{id}/`

---

## 🚗 Vehicle Management

### List All Vehicles
**Endpoint**: `GET /api/admin/marketplace/vehicles/`

**Query Parameters**:
- `?status=For Sale` / `Sold` / `Reserved`
- `?category=4w` / `2w`
- `?vehicle_type=Private` / `Commercial`
- `?fuel_type=Petrol` / `Diesel` / `CNG` / `EV`
- `?transmission=Manual` / `Automatic`
- `?make=Hyundai`
- `?model=Creta`
- `?price__gte=500000` (min price)
- `?price__lte=1500000` (max price)
- `?year__gte=2020` (min year)
- `?search=TVI-000000001` (searches ID, make, model, variant, reg_number)

**Response**:
```json
[
  {
    "id": "TVI-000000001",
    "make": "Hyundai",
    "model": "Creta",
    "variant": "SX",
    "price": 1500000.00,
    "year": 2023,
    "mfg_year": 2023,
    "reg_year": 2023,
    "fuel_type": "Diesel",
    "transmission": "Automatic",
    "km_driven": 12000,
    "color": "White",
    "reg_number": "MH02DN1234",
    "chassis_number": "MA...",
    "rto_state": "Maharashtra",
    "ownership": "1st",
    "valid_upto": "2038-01-01",
    "tax": "LTT",
    "status": "For Sale",
    "category": "4w",
    "vehicle_type": "Private",
    "verified": true,
    "service_history": "Authorized Service Center",
    "remarks": "Excellent Condition",
    "rc_available": true,
    "hypothecation": "Close",
    "insurance": "Comprehensive",
    "insurance_expiry": "2024-05-20",
    "inspection_report": {
      "insp_bumper_status": "Issue",
      "insp_bumper_remark": "Minor Scratches",
      "insp_engine_oil_status": "OK"
    },
    "main_image": "https://apis.trustedvehicles.com/media/vehicles/...",
    "img_front": "https://...",
    "img_rc": "https://...",
    "img_noc": "https://...",
    "created_at": "2023-01-01T12:00:00Z",
    "updated_at": "2023-01-01T12:00:00Z"
  }
]
```

### Get Single Vehicle
**Endpoint**: `GET /api/admin/marketplace/vehicles/{TVI-ID}/`

### Create Vehicle
**Endpoint**: `POST /api/admin/marketplace/vehicles/`

**Headers**: `Content-Type: multipart/form-data`

**Form Fields**:

**Basic Details**:
- `category` (required): `4w` or `2w`
- `vehicle_type` (required): `Private` or `Commercial`
- `make` (required): e.g., `Maruti`
- `model` (required): e.g., `Swift`
- `variant`: e.g., `VXI`
- `price` (required): e.g., `500000`
- `year` (required): e.g., `2020`
- `mfg_year`: Manufacturing year
- `reg_year`: Registration year
- `fuel_type`: `Petrol`, `Diesel`, `CNG`, `EV`
- `transmission`: `Manual`, `Automatic`
- `km_driven`: e.g., `35000`
- `color`: e.g., `White`
- `reg_number`: e.g., `MH01AB1234`
- `chassis_number`: Chassis number
- `rto_state`: e.g., `MH`
- `ownership`: `1st`, `2nd`, `3rd`
- `tax`: `LTT`, `OTT`
- `status`: `For Sale` (default)
- `verified`: `true` / `false`

**Documents**:
- `rc_available`: `true` / `false`
- `hypothecation`: `Open`, `Close`, `NA`
- `insurance`: Insurance type
- `insurance_expiry`: Date (YYYY-MM-DD)
- `valid_upto`: RC validity date
- `service_history`: Text
- `remarks`: Text
- `img_rc`: File (if rc_available=true)
- `img_noc`: File (if hypothecation=Close)

**Gallery Images**:
- `main_image` (required): File
- `img_front`: File
- `img_back`: File
- `img_left`: File
- `img_right`: File
- `img_front_right`: File
- `img_back_right`: File
- `img_back_left`: File
- `img_front_left`: File
- `img_open_dickey`: File
- `img_open_bonnet`: File
- `img_roof`: File
- `img_engine`: File
- `img_dashboard`: File
- `img_right_front_door`: File
- `img_right_back_door`: File
- `img_interior_1`: File
- `img_interior_2`: File

**Tyre Images**:
- `img_tyre_1`: File (Front Left)
- `img_tyre_2`: File (Front Right)
- `img_tyre_3`: File (Rear Left)
- `img_tyre_4`: File (Rear Right)
- `img_tyre_optional`: File

**Inspection Status (Text Fields)**:
- `insp_bumper_status`: `OK` / `Issue`
- `insp_bumper_remark`: Text
- `insp_bonnet_status`: `OK` / `Issue`
- `insp_bonnet_remark`: Text
- `insp_roof_status`: `OK` / `Issue`
- `insp_fender_status`: `OK` / `Issue`
- `insp_engine_oil_status`: `OK` / `Issue`
- `insp_battery_status`: `OK` / `Issue`
- `insp_suspension_status`: `OK` / `Issue`
- `insp_ac_status`: `OK` / `Issue`
- *(and many more inspection points)*

**Inspection Images**:
- `img_insp_bumper`: File
- `img_insp_bonnet`: File
- `img_insp_roof`: File
- `img_insp_fender`: File
- `img_insp_door_1`: File
- `img_insp_door_2`: File
- `img_insp_door_3`: File
- `img_insp_door_4`: File
- `img_insp_pillar_1` to `img_insp_pillar_6`: Files
- `img_insp_engine_assembly`: File
- `img_insp_battery`: File
- `img_insp_engine_oil`: File
- `img_insp_suspension`: File
- `img_insp_ac`: File
- `img_insp_power_window`: File
- `img_insp_airbag`: File
- *(and many more)*

**Inspection Videos**:
- `video_insp_engine_sound`: File
- `video_insp_engine_smoke`: File
- `video_insp_blowby`: File

### Update Vehicle
**Endpoint**: `PUT /api/admin/marketplace/vehicles/{TVI-ID}/`

**Headers**: `Content-Type: multipart/form-data`

**Form Fields**: Same as Create (send only fields you want to update)

### Delete Vehicle
**Endpoint**: `DELETE /api/admin/marketplace/vehicles/{TVI-ID}/`

---

## 💬 Inquiries Management

### List All Inquiries
**Endpoint**: `GET /api/admin/marketplace/inquiries/`

**Query Parameters**:
- `?vehicle=TVI-000000001`
- `?user=1`

**Response**:
```json
[
  {
    "id": 5,
    "vehicle": "TVI-000000001",
    "user": 1,
    "message": "Is this negotiable?",
    "offer_price": 500000.00,
    "created_at": "2023-01-01T12:00:00Z"
  }
]
```

### Get Single Inquiry
**Endpoint**: `GET /api/admin/marketplace/inquiries/{id}/`

### Delete Inquiry
**Endpoint**: `DELETE /api/admin/marketplace/inquiries/{id}/`

---

## 🎨 Banner Management

### List All Banners
**Endpoint**: `GET /api/admin/marketplace/banners/`

**Response**:
```json
[
  {
    "id": 1,
    "title": "Summer Sale",
    "image": "https://apis.trustedvehicles.com/media/banners/...",
    "is_active": true,
    "created_at": "2023-01-01T12:00:00Z"
  }
]
```

### Create Banner
**Endpoint**: `POST /api/admin/marketplace/banners/`

**Headers**: `Content-Type: multipart/form-data`

**Form Fields**:
- `title` (required): Text
- `image` (required): File
- `is_active`: `true` / `false`

### Update Banner
**Endpoint**: `PUT /api/admin/marketplace/banners/{id}/`

### Delete Banner
**Endpoint**: `DELETE /api/admin/marketplace/banners/{id}/`

---

## ⭐ Favorites Management

### List All Favorites
**Endpoint**: `GET /api/admin/marketplace/favorites/`

**Query Parameters**:
- `?user=1`
- `?vehicle=TVI-000000001`

**Response**:
```json
[
  {
    "id": 1,
    "user": 1,
    "vehicle": {
      "id": "TVI-000000001",
      "make": "Hyundai",
      "model": "Creta",
      "price": 1500000.00
    },
    "created_at": "2023-01-01T12:00:00Z"
  }
]
```

### Delete Favorite
**Endpoint**: `DELETE /api/admin/marketplace/favorites/{id}/`

---

## 🔔 Notifications Management

### List All Notifications
**Endpoint**: `GET /api/admin/marketplace/notifications/`

**Query Parameters**:
- `?user=1`
- `?type=info` / `warning` / `success`
- `?is_read=true` / `false`

**Response**:
```json
[
  {
    "id": 1,
    "user": 1,
    "title": "New Vehicle Added",
    "message": "A new vehicle matching your criteria is available",
    "type": "info",
    "is_read": false,
    "created_at": "2023-01-01T12:00:00Z"
  }
]
```

### Create Notification
**Endpoint**: `POST /api/admin/marketplace/notifications/`

**Request Body**:
```json
{
  "user": 1,
  "title": "Important Update",
  "message": "Your inquiry has been responded to",
  "type": "info"
}
```

### Update Notification
**Endpoint**: `PUT /api/admin/marketplace/notifications/{id}/`

### Delete Notification
**Endpoint**: `DELETE /api/admin/marketplace/notifications/{id}/`

---

## 📞 Marketplace Contacts

### List All Marketplace Contacts
**Endpoint**: `GET /api/admin/marketplace/contacts/`

**Response**:
```json
[
  {
    "id": 1,
    "name": "Customer Name",
    "email": "customer@example.com",
    "phone": "9876543210",
    "message": "I want to know more about...",
    "created_at": "2023-01-01T12:00:00Z"
  }
]
```

### Delete Contact
**Endpoint**: `DELETE /api/admin/marketplace/contacts/{id}/`

---

## 🔍 Inspections Management

### List All Inspections
**Endpoint**: `GET /api/admin/inspections/`

**Response**:
```json
[
  {
    "id": 1,
    "vehicle_id": "TVI-000000001",
    "inspector_name": "Inspector Name",
    "inspection_date": "2023-01-01",
    "status": "Completed",
    "report": "Detailed inspection report...",
    "created_at": "2023-01-01T12:00:00Z"
  }
]
```

### Create Inspection
**Endpoint**: `POST /api/admin/inspections/`

**Request Body**:
```json
{
  "vehicle_id": "TVI-000000001",
  "inspector_name": "John Inspector",
  "inspection_date": "2023-01-15",
  "status": "Pending",
  "report": "Initial inspection notes"
}
```

### Update Inspection
**Endpoint**: `PUT /api/admin/inspections/{id}/`

### Delete Inspection
**Endpoint**: `DELETE /api/admin/inspections/{id}/`

---

## 🌐 Website Requests Management

### Sell Car Requests

**List**: `GET /api/admin/website/sell-requests/`

**Query**: `?search=phone_or_name`

**Response**:
```json
[
  {
    "id": 1,
    "make": "Hyundai",
    "model": "Creta",
    "variant": "SX",
    "reg_number": "MH01AB1234",
    "reg_year": 2020,
    "fuel_type": "Diesel",
    "ownership": "1st",
    "transmission": "Manual",
    "km_driven": 35000,
    "state": "Maharashtra",
    "city": "Mumbai",
    "address": "Full Address...",
    "name": "Seller Name",
    "phone": "9876543210",
    "scheduled_date": "2024-01-15",
    "created_at": "2023-01-01T12:00:00Z"
  }
]
```

**Get Single**: `GET /api/admin/website/sell-requests/{id}/`

**Delete**: `DELETE /api/admin/website/sell-requests/{id}/`

---

### Loan Applications

**List**: `GET /api/admin/website/loan-requests/`

**Response**:
```json
[
  {
    "id": 1,
    "name": "Applicant Name",
    "mobile": "9876543210",
    "income": 50000.00,
    "loan_amount": 300000.00,
    "employment_type": "Salaried",
    "created_at": "2023-01-01T12:00:00Z"
  }
]
```

**Get Single**: `GET /api/admin/website/loan-requests/{id}/`

**Delete**: `DELETE /api/admin/website/loan-requests/{id}/`

---

### Insurance Leads

**List**: `GET /api/admin/website/insurance-leads/`

**Response**:
```json
[
  {
    "id": 1,
    "reg_number": "MH02AB1234",
    "name": "Owner Name",
    "mobile": "9876543210",
    "policy_type": "Comprehensive",
    "expiry_date": "2024-02-01",
    "created_at": "2023-01-01T12:00:00Z"
  }
]
```

**Get Single**: `GET /api/admin/website/insurance-leads/{id}/`

**Delete**: `DELETE /api/admin/website/insurance-leads/{id}/`

---

### PDI Booking Requests

**List**: `GET /api/admin/website/pdi-requests/`

**Response**:
```json
[
  {
    "id": 1,
    "name": "Customer Name",
    "email": "customer@example.com",
    "phone": "9876543210",
    "city": "Mumbai",
    "make": "Hyundai",
    "model": "Creta",
    "scheduled_date": "2024-01-20",
    "created_at": "2023-01-01T12:00:00Z"
  }
]
```

**Get Single**: `GET /api/admin/website/pdi-requests/{id}/`

**Delete**: `DELETE /api/admin/website/pdi-requests/{id}/`

---

### Dealer Demo Requests

**List**: `GET /api/admin/website/dealer-demos/`

**Response**:
```json
[
  {
    "id": 1,
    "name": "Dealer Name",
    "phone": "9876543210",
    "email": "dealer@example.com",
    "dealership_name": "ABC Motors",
    "created_at": "2023-01-01T12:00:00Z"
  }
]
```

**Get Single**: `GET /api/admin/website/dealer-demos/{id}/`

**Delete**: `DELETE /api/admin/website/dealer-demos/{id}/`

---

### Contact Us Messages

**List**: `GET /api/admin/website/contacts/`

**Response**:
```json
[
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "subject": "Help Needed",
    "message": "I need assistance with...",
    "created_at": "2023-01-01T12:00:00Z"
  }
]
```

**Get Single**: `GET /api/admin/website/contacts/{id}/`

**Delete**: `DELETE /api/admin/website/contacts/{id}/`

---

## 📝 Common Patterns

### Pagination
All list endpoints support pagination:
```
?page=1&page_size=20
```

### Ordering
```
?ordering=-created_at  (descending)
?ordering=created_at   (ascending)
```

### Multiple Filters
```
?status=For Sale&fuel_type=Diesel&price__lte=1000000
```

---

## ⚠️ Error Responses

### 400 Bad Request
```json
{
  "error": "Invalid data",
  "details": {
    "field_name": ["Error message"]
  }
}
```

### 401 Unauthorized
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 403 Forbidden
```json
{
  "detail": "You do not have permission to perform this action."
}
```

### 404 Not Found
```json
{
  "detail": "Not found."
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error"
}
```

---

## 🔒 Security Notes

1. **Always use HTTPS** in production
2. **Token expires** after 24 hours (refresh required)
3. **Rate limiting** may apply
4. **CORS** is configured for trusted domains only
5. **File uploads** have size limits (check with backend team)

---

## 📞 Support

For any API issues or questions, contact the backend team.

**Last Updated**: December 16, 2025
