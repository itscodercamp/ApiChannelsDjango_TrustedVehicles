# Marketplace API Documentation

Base URL: `/api` (e.g., `https://apis.trustedvehicles.com/api`)

## 1. Authentication

### Register
- **Endpoint**: `POST /auth/register`
- **Description**: Create a new customer or dealer account.
- **Request Body**:
```json
{
  "name": "Rahul Kumar",
  "email": "user@example.com",
  "password": "yourpassword",
  "role": "customer", // "customer" or "dealer"
  "phone": "9876543210", // Optional
  "dealershipName": "Rahul Motors", // Required if role is dealer
  "location": "Mumbai" // Requested if role is dealer
}
```
- **Response (201 Created)**:
```json
{
  "message": "Registration successful",
  "user": {
    "id": "u_5",
    "name": "Rahul Kumar",
    "email": "user@example.com",
    "role": "Customer"
  }
}
```

### Login
- **Endpoint**: `POST /auth/login`
- **Description**: Authenticate and receive JWT token.
- **Request Body**:
```json
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```
- **Response (200 OK)**:
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR...",
  "user": {
    "id": "u_5",
    "name": "Rahul Kumar",
    "email": "user@example.com",
    "role": "Customer",
    "savedVehicles": ["v1", "v2"],
    "savedSearches": []
  }
}
```

---

## 2. Vehicles

### Get All Vehicles (Search & Filter)
- **Endpoint**: `GET /marketplace/vehicles`
- **Query Parameters**:
  - `page`: Page number (default: 1)
  - `limit`: Results per page (default: 20)
  - `search`: Generic search string (matches make, model, variant)
  - `status`: e.g., 'For Sale'
  - `make`: e.g., 'Hyundai'
  - `model`: e.g., 'Creta'
  - `price__gte`: Min Price (e.g., 500000)
  - `price__lte`: Max Price (e.g., 1500000)
  - `year__gte`: Min Year (e.g., 2020)
  - `fuel_type`: 'Petrol', 'Diesel', 'CNG', 'EV'
  - `transmission`: 'Manual', 'Automatic'
  - `rto_state`: Search by city/state code (e.g., 'MH')
  - `vehicle_type`: 'Private', 'Commercial'
  - `category`: '4w', '2w'

- **Example**: `/marketplace/vehicles?make=Hyundai&price__lte=1000000&fuel_type=Diesel`

### Get Single Vehicle
- **Endpoint**: `GET /marketplace/vehicles/{id}`
- **Description**: Ge full details of a vehicle.
- **Path Parameter**: `id` (String: e.g., 'TVI-000000001')
- **Response Structure (JSON)**:
```json
{
  "id": "TVI-000000001",
  "make": "Hyundai",
  "model": "Creta",
  "variant": "SX",
  "price": 1500000.00,
  "year": 2023,
  "mfgYear": 2023,
  "regYear": 2023,
  "fuelType": "Diesel",
  "transmission": "Automatic",
  "kmDriven": 12000,
  "color": "White",
  "regNumber": "MH02DN1234",
  "chassisNumber": "MA...",
  "rtoState": "Maharashtra",
  "ownership": "1st",
  "validUpto": "2038-01-01",
  "tax": "LTT",
  "status": "For Sale",
  "category": "4w",
  "vehicleType": "Private",
  "verified": true,
  "serviceHistory": "Authorized Service Center",
  "remarks": "Excellent Condition",
  
  "rcAvailable": true,
  "hypothecation": "Close",
  "insurance": "Comprehensive",
  "insuranceExpiry": "2024-05-20",
  
  "inspection_report": {
      "insp_bumper_status": "Issue",
      "insp_bumper_remark": "Minor Scratches",
      "insp_engine_oil_status": "OK",
      "...": "..."
  },

  "mainImage": "url...",
  "img_front": "url...",
  "img_back": "url...", 
  "img_left": "url...", 
  "img_right": "url...",
  "img_interior_1": "url...",
  "img_dashboard": "url...",
  "... (all gallery images)": "url...",

  "img_rc": "url...",
  "img_noc": "url...",

  "img_insp_bumper": "url... (if issue)",
  "img_insp_engine_assembly": "url...",
  "... (all inspection images)": "url...",

  "video_insp_engine_sound": "url...",
  "video_insp_engine_smoke": "url...",
  "video_insp_blowby": "url..."
}
```
**Notes**:
- **Images**: All image fields return full URLs.
- **CamelCase**: The API uses snake_case by default for some fields unless mapped. (Update: Serializer mapped standard ones).
- **Inspection**: `inspection_report` contains all status text. Corresponding images are in `img_insp_*` fields.

### Add Vehicle
- **Endpoint**: `POST /marketplace/vehicles`
- **Headers**: `Content-Type: multipart/form-data`
- **Body Parameters**:
  - **Basic Details**:
    - `category`: '4w' or '2w'
    - `vehicleType`: 'Private' or 'Commercial'
    - `make`: e.g., 'Maruti'
    - `model`: e.g., 'Swift'
    - `variant`: e.g., 'VXI'
    - `price`: Selling Price
    - `year`: Manufacturing Year
    - `fuelType`: 'Petrol', 'Diesel', etc.
    - `transmission`: 'Manual', 'Automatic'
    - `odometer`: KM Driven
    - `color`: e.g., 'White'
    - `regNumber`: Registration No.
    - `chassisNumber`: Chassis No.
    - `rtoState`: e.g., 'MH'
    - `ownership`: '1st', '2nd'
    - `tax`: 'LTT' or 'OTT'
    - `status`: 'For Sale' (default)

  - **Documents (Logic Based)**:
    - `rcAvailable`: `true` or `false`
    - `hypothecation`: 'Open', 'Close', 'NA'
    - `img_rc`: File (Required if rcAvailable=true)
    - `img_noc`: File (Required if hypothecation=Close)

  - **Gallery Images (Standard)**:
    - `mainImage` (Required), `img_front`, `img_back`, `img_left`, `img_right`, `img_front_right`, `img_back_right`, `img_back_left`, `img_front_left`, `img_open_dickey`, `img_open_bonnet`, `img_roof`, `img_engine`, `img_dashboard`, `img_right_front_door`, `img_right_back_door`, `img_interior_1`, `img_interior_2`.

  - **Inspection Status (Text Fields)**:
    - You can send granular status fields directly. Backend packs them into `inspection_report`.
    - Format: `insp_[part]_status` and `insp_[part]_remark`
    - Examples:
      - `insp_bumper_status`: 'OK' or 'Issue'
      - `insp_bumper_remark`: 'Scratched'
      - `insp_engine_oil_status`: 'OK'
    - Covers: `bumper`, `bonnet`, `roof`, `fender`, `doors`, `pillars`, `apron`, `firewall`, `engine_assembly`, `battery`, `suspension`, `ac`, `tyres`, etc.

  - **Inspection Images (Conditional)**:
    - Upload these if status is 'Issue' or for proof.
    - **Exterior**: `img_insp_bumper`, `img_insp_bonnet`, `img_insp_roof`, `img_insp_fender`, `img_insp_door_1`..`4`, `img_insp_pillar_1`..`6`, `img_insp_quarter_panel`, `img_insp_dickey_door`.
    - **Structure**: `img_insp_apron_1`, `img_insp_firewall`, `img_insp_cowl_top`, etc.
    - **Glass/Lights**: `img_insp_windshield`, `img_insp_lights_1`, etc.
    - **Engine/Mechanical**: `img_insp_engine_assembly`, `img_insp_battery`, `img_insp_engine_oil`, `img_insp_coolant`, `img_insp_engine_mounting`, `img_insp_suspension`, `img_insp_steering`, `img_insp_brake`, `img_insp_ac`.
    - **Interior/Electrical**: `img_insp_power_window`, `img_insp_airbag`, `img_insp_music_system`, `img_insp_seat`, `img_insp_interior`.
    - **Tyres**: `img_tyre_1` (Front Left), `img_tyre_2` (Front Right), `img_tyre_3` (Rear Left), `img_tyre_4` (Rear Right), `img_tyre_optional`.
  
  - **Inspection Videos**:
    - `video_insp_engine_sound`
    - `video_insp_engine_smoke`
    - `video_insp_blowby`

---

## 3. User Features (Requires Login)
Headers: `Authorization: Bearer <token>`

### Get Favorites
- **Endpoint**: `GET /user/favorites`
- **Description**: Returns a list of full Vehicle objects that the user has favorited.

### Add Favorite
- **Endpoint**: `POST /user/favorites`
- **Request Body**:
```json
{
  "vehicleId": "TVI-000000001"
}
```

### Remove Favorite
- **Endpoint**: `DELETE /user/favorites/{vehicleId}`
- **Path Parameter**: `vehicleId` (String: e.g., 'TVI-000000001')

### Get Notifications
- **Endpoint**: `GET /user/notifications`

### Mark Notification Read
- **Endpoint**: `PUT /user/notifications/{id}/read`

---

## 4. Inquiries & Support

### Submit Inquiry (Make Offer)
- **Endpoint**: `POST /marketplace/inquiries`
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**:
```json
{
  "vehicleId": "TVI-000000001",
  "offerPrice": 500000,
  "message": "Is this price negotiable?"
}
```

### Contact Support
- **Endpoint**: `POST /support/contact`
- **Request Body**:
```json
{
  "firstName": "Rahul",
  "lastName": "Kumar",
  "email": "user@example.com",
  "subject": "App Issue",
  "message": "I cannot upload images."
}
```
