# 🚗 Vehicle Management & Inspection API Documentation

This documentation details the endpoints and parameters required for adding, updating, and performing inspections on vehicles in the Marketplace.

---

## 🏗️ Base URL
`{{SERVER_URL}}/api/`

---

## 🔐 1. Authentication (Employee/Inspector)

To perform vehicle management and inspections, you must login as an employee/staff.

### **Endpoint:** `POST /api/auth/employee/login/`

**Payload:**
```json
{
  "email": "employee@example.com",
  "password": "yourpassword"
}
```

**Response:** Returns a `token`. Include this token in the header of all subsequent requests.
`Authorization: Bearer <your_token>`

---

## 📦 2. Vehicle Operations

### **A. Add New Vehicle (Main Form)**
**Endpoint:** `POST /marketplace/vehicles/`
**Content-Type:** `multipart/form-data`

### **B. Edit/Update Vehicle**
**Endpoint:** `PATCH /marketplace/vehicles/{id}/`
**Content-Type:** `multipart/form-data`
*(Note: Use the Vehicle ID like TVI-000000001)*

---

## 📝 3. Detailed Parameters

### **Section A: Basic Info**
| Parameter Name | Type | Options / Validation |
| :--- | :--- | :--- |
| `make` | String | Brand Name (e.g., Maruti) |
| `model` | String | Model Name (e.g., Swift) |
| `variant` | String | Version (e.g., VXI) |
| `price` | Number | Numeric value (e.g., 550000) |
| `year` | Number | Manufacturing Year (e.g., 2022) |
| `category` | String | `4w` (Car), `2w` (Bike) |
| `fuelType` | String | `Petrol`, `Diesel`, `CNG`, `Electric` |
| `transmission` | String | `Manual`, `Automatic` |
| `status` | String | `For Sale`, `Sold`, `Paused` |
| `verified` | Boolean | `true` / `false` |

### **Section B: Registration & Documents**
| Parameter Name | Type | Logic / Dependent Fields |
| :--- | :--- | :--- |
| `regNumber` | String | Vehicle Number (e.g., MH01AB1234) |
| `rtoState` | String | RTO City/State |
| `odometer` | Number | Total km driven |
| `ownership` | String | `1st Owner`, `2nd Owner`, etc. |
| `rcAvailable` | Boolean | If `true` -> Send File in `img_rc` |
| `hypothecation` | String | `Open`, `Close`, `NA` |
| `insurance` | String | `Comprehensive`, `Third Party`, `Expired` |
| `insuranceExpiry`| Date | Send only if insurance is NOT Expired |
| **Files** | | |
| `img_rc` | File | RC Document Photo |
| `img_noc` | File | NOC Document (if hypothecation is Close) |

---

## 🛠️ 4. Inspection Logic (Condition Report)

Backend validation requires specific patterns for inspection. Each part has 3 data points.

### **Logic Template:**
For any part (e.g., **Engine**):
1.  **Status (`insp_engine_status`):** `OK`, `Issue`, `NA` (**Mandatory**)
2.  **Remark (`insp_engine_remark`):** String (**Mandatory if status is 'Issue'**)
3.  **Media (`img_insp_engine`):** File (Optional evidence photo)

### **Part Categories and Parameter Slugs:**

| Category | Part Name | Status Parameter | Remark Parameter | Media (Photo/Video) |
| :--- | :--- | :--- | :--- | :--- |
| **Structure** | Apron | `insp_apron_status` | `insp_apron_remark` | `img_insp_apron_1`, `2`, `img_insp_apron_leg_1`, `2` |
| | Firewall | `insp_firewall_status` | `insp_firewall_remark` | `img_insp_firewall` |
| | Cowl Top | `insp_cowl_top_status` | `insp_cowl_top_remark` | `img_insp_cowl_top` |
| **Body** | Bumper | `insp_bumper_status` | `insp_bumper_remark` | `img_insp_bumper` |
| | Bonnet | `insp_bonnet_status` | `insp_bonnet_remark` | `img_insp_bonnet` |
| | Roof | `insp_roof_status` | `insp_roof_remark` | `img_insp_roof` |
| | Doors | `insp_doors_status` | `insp_doors_remark` | `img_insp_door_1` to `4` |
| | Pillar | `insp_pillar_status` | `insp_pillar_remark` | `img_insp_pillar_1` to `6` |
| **Engine** | Assembly | `insp_engine_assembly_status`| `insp_engine_assembly_remark`| `img_insp_engine_assembly`|
| | Battery | `insp_battery_status` | `insp_battery_remark` | `img_insp_battery` |
| | Engine Oil| `insp_engine_oil_status` | `insp_engine_oil_remark` | `img_insp_engine_oil`, `img_insp_engine_oil_level` |
| | Sound | `insp_engine_sound_status` | `insp_engine_sound_remark` | `video_insp_engine_sound` |
| | Smoke | `insp_engine_smoke_status` | `insp_engine_smoke_remark` | `video_insp_engine_smoke` |
| | Blowby | `insp_blowby_status` | `insp_blowby_remark` | `video_insp_blowby` |
| **Others** | AC / Heater | `insp_ac_status` | `insp_ac_remark` | `img_insp_ac`, `img_insp_heater` |
| | Electrical | `insp_electrical_status` | `insp_electrical_remark` | `img_insp_electrical`, `img_insp_power_window` |
| | Airbags | `insp_airbag_status` | `insp_airbag_remark` | `img_insp_airbag` |
| | Suspension | `insp_suspension_status` | `insp_suspension_remark` | `img_insp_suspension` |
| | Steering | `insp_steering_status` | `insp_steering_remark` | `img_insp_steering` |
| | Interior | `insp_interior_status` | `insp_interior_remark` | `img_insp_interior`, `img_insp_seat`, `img_insp_sunroof` |

---

## 🖼️ 5. Gallery (Full Vehicle Photos)

The following keys are for the main vehicle gallery display:

*   `mainImage`: Main cover photo (**Mandatory** for listing)
*   `img_front`: Front view
*   `img_back`: Back view
*   `img_right`, `img_left`: Side views
*   `img_dashboard`: Interior view
*   `img_engine`: Engine bay view
*   `img_tyre_1`, `2`, `3`, `4`: Individual tyre photos

---

## 🚀 6. Sample Request (JavaScript Fetch)

```javascript
const formData = new FormData();

// Basic Info
formData.append('make', 'Toyota');
formData.append('model', 'Fortuner');
formData.append('price', 2800000);
formData.append('fuelType', 'Diesel');

// Inspection Logic
formData.append('insp_bumper_status', 'Issue');
formData.append('insp_bumper_remark', 'Deep scratches on front left bumper');
formData.append('img_insp_bumper', fileInput.files[0]); // File

// Gallery
formData.append('mainImage', coverFile);

fetch('/api/marketplace/vehicles/', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_JWT_TOKEN'
  },
  body: formData
})
.then(res => res.json())
.then(data => console.log(data));
```

## ✅ Response Codes
*   **201 Created**: Vehicle added successfully. Returns the full vehicle object.
*   **200 OK**: Vehicle updated successfully (on PATCH).
*   **400 Bad Request**: Validation failed (e.g., Status is 'Issue' but Remark is empty).
*   **401 Unauthorized**: Token missing or expired.
*   **403 Forbidden**: You don't have employee/staff permissions.
