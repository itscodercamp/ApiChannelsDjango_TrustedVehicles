# AdminTVGodMode API Documentation

This documentation provides the details for all API endpoints required to build the Admin Panel and integrate the Website frontend.

## Base URL
`http://127.0.0.1:8000/api`

---

## 1. Authentication

### **Employee/Admin Login**
*   **Endpoint:** `/login`
*   **Method:** `POST`
*   **Description:** Authenticates an admin/employee and returns a token.
*   **Body:**
    ```json
    {
      "email": "admin@example.com",
      "password": "yourpassword"
    }
    ```
*   **Response:**
    ```json
    {
      "token": "eyJhbGciOiJIUzI1NiIsIn...",
      "user": { "id": 1, "name": "Admin", "email": "..." }
    }
    ```

---

## 2. Marketplace & Inventory (Vehicles)

### **Get All Vehicles (Inventory)**
*   **Endpoint:** `/marketplace/vehicles`
*   **Method:** `GET`
*   **Description:** Retrieve a list of all vehicles. Supports filtering for the public website.
*   **Query Parameters (Optional):**
    *   `status`: Filter by status (e.g., `For Sale`, `Sold`, `Paused`).
*   **Response:** Array of vehicle objects.

### **Get Single Vehicle**
*   **Endpoint:** `/marketplace/vehicles/{id}`
*   **Method:** `GET`
*   **Description:** Retrieve full details of a specific vehicle.

### **Add New Vehicle**
*   **Endpoint:** `/marketplace/vehicles`
*   **Method:** `POST`
*   **Content-Type:** `multipart/form-data`
*   **Description:** Create a new vehicle listing with text details and images/videos.
*   **Form Fields (Text):**
    *   `make`, `model`, `variant`, `price`, `year`, `mfg_year`, `reg_year`
    *   `status` (Default: "For Sale"), `verified` (true/false)
    *   `category` ("4w"/"2w"), `vehicle_type` ("Private"/"Commercial")
    *   `color`, `fuel_type`, `transmission`, `km_driven`, `owner_type`
    *   `reg_number`, `chassis_number`, `rto_state`, `valid_upto` (Date)
    *   `tax`, `rc_available` (true/false), `hypothecation` (Open/Close/NA)
    *   `insurance`, `insurance_expiry` (Date)
    *   `service_history`, `remarks`
    *   **`inspection_report`**: A JSON string containing status and remarks for all inspection points (exterior, engine, etc.).
*   **File Fields (Images/Videos):**
    *   **Documents:** `img_rc`, `img_noc`
    *   **Gallery:** `main_image`, `img_front`, `img_back`, `img_left`, `img_right`, `img_open_bonnet`, `img_open_dickey`, `img_dashboard`, `img_engine`, `img_roof`, etc.
    *   **Tyres:** `img_tyre_1` to `img_tyre_4`, `img_tyre_optional`
    *   **Inspection:** `img_insp_bumper`, `img_insp_bonnet`, `img_insp_engine_oil`, `img_insp_roof`, `img_insp_fender`, `img_insp_quarter_panel`, etc.
    *   **Videos:** `video_insp_engine_sound`, `video_insp_blowby`, `video_insp_engine_smoke`

### **Update Vehicle**
*   **Endpoint:** `/marketplace/vehicles/{id}`
*   **Method:** `PUT` or `PATCH`
*   **Content-Type:** `multipart/form-data`
*   **Description:** Update any field of an existing vehicle.

---

## 3. Website Forms (Public Submission)

These endpoints are used by the public website to submit requests.

### **Sell Car Request**
*   **Endpoint:** `/website/sell-request`
*   **Method:** `POST`
*   **Body:**
    ```json
    {
      "make": "Maruti", "model": "Swift", "variant": "VXI",
      "regNumber": "MH12AB1234", "regYear": 2020,
      "fuelType": "Petrol", "transmission": "Manual",
      "ownership": "1st", "kmDriven": 50000,
      "state": "Maharashtra", "city": "Pune",
      "address": "Full address...",
      "name": "Seller Name", "phone": "9876543210",
      "scheduledDate": "2023-10-30"
    }
    ```

### **Car Loan Application**
*   **Endpoint:** `/website/loan/apply`
*   **Method:** `POST`
*   **Body:**
    ```json
    {
      "name": "Applicant Name",
      "mobile": "9876543210",
      "income": 500000,
      "loanAmount": 1000000,
      "employmentType": "Salaried"
    }
    ```

### **Insurance Quote Request**
*   **Endpoint:** `/website/insurance/quote`
*   **Method:** `POST`
*   **Body:**
    ```json
    {
      "regNumber": "MH12AB1234",
      "name": "User Name",
      "mobile": "9876543210",
      "policyType": "Comprehensive",
      "expiryDate": "2023-12-31" (Optional)
    }
    ```

### **PDI Booking**
*   **Endpoint:** `/website/pdi/book`
*   **Method:** `POST`
*   **Body:**
    ```json
    {
      "name": "User Name", "email": "user@example.com", "phone": "9876543210",
      "city": "Mumbai", "make": "Tata", "model": "Nexon",
      "scheduledDate": "2023-11-15"
    }
    ```

### **Dealer Demo Request**
*   **Endpoint:** `/website/dealer/demo-request`
*   **Method:** `POST`
*   **Body:**
    ```json
    {
      "name": "Dealer Name",
      "phone": "9876543210",
      "email": "dealer@example.com",
      "dealershipName": "Auto World" (Optional)
    }
    ```

### **Contact Us**
*   **Endpoint:** `/website/contact`
*   **Method:** `POST`
*   **Body:**
    ```json
    {
      "firstName": "John", "lastName": "Doe",
      "email": "john@example.com",
      "subject": "Inquiry",
      "message": "Hello..."
    }
    ```

---

## 4. Admin Panel Data (Read-Only Lists)

Use these endpoints to display submitted form data in the Admin Panel tables.

| Feature | Endpoint | Method | Description |
| :--- | :--- | :--- | :--- |
| **Sell Requests** | `/website/admin/sell-requests` | `GET` | List all sell car requests (Newest first) |
| **Loan Applications** | `/website/admin/loan-requests` | `GET` | List all car loan applications |
| **Insurance Leads** | `/website/admin/insurance-leads` | `GET` | List all insurance quote requests |
| **PDI Bookings** | `/website/admin/pdi-requests` | `GET` | List all PDI inspection bookings |
| **Dealer Demos** | `/website/admin/dealer-demo-requests` | `GET` | List all dealer demo requests |
| **Contact Msgs** | `/website/admin/contacts` | `GET` | List all contact form submissions |

---

## 5. Other
*   **Stats:** `GET /core/stats` - Verification of admin dashboard statistics.
*   **File Upload:** `POST /core/upload` - Generic file upload.

