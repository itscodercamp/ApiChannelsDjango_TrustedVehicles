import requests
import json

BASE_URL = 'http://127.0.0.1:8000/api'

def test_employee_login():
    print("Testing Employee Login...")
    url = f"{BASE_URL}/login"
    data = {
        "email": "admin@example.com",
        "password": "admin123"
    }
    response = requests.post(url, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200

def test_marketplace_register():
    print("\nTesting Marketplace Register...")
    url = f"{BASE_URL}/marketplace/auth/register"
    data = {
        "user_type": "Customer",
        "full_name": "Test Customer",
        "phone": "9876543210",
        "email": "customer@example.com",
        "password": "secure_password"
    }
    response = requests.post(url, json=data)
    print(f"Status: {response.status_code}")
    # If already exists, it might fail, which is fine for re-runs
    if response.status_code == 400 and 'phone' in response.json():
        print("User already exists")
    else:
        print(f"Response: {response.json()}")
        assert response.status_code == 201

def test_marketplace_login():
    print("\nTesting Marketplace Login...")
    url = f"{BASE_URL}/marketplace/auth/login"
    data = {
        "phone": "9876543210",
        "password": "secure_password"
    }
    response = requests.post(url, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200

def test_contact_form():
    print("\nTesting Contact Form...")
    url = f"{BASE_URL}/contact"
    data = {
        "firstName": "Anjali",
        "lastName": "Gupta",
        "email": "anjali@test.com",
        "subject": "Buying a Car",
        "message": "I want to know about finance options..."
    }
    response = requests.post(url, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 201

def test_sell_request():
    print("\nTesting Sell Request...")
    url = f"{BASE_URL}/sell-request"
    data = {
        "make": "Maruti Suzuki",
        "model": "Swift",
        "variant": "VXI",
        "regNumber": "MH31AB1234",
        "regYear": 2018,
        "fuelType": "Petrol",
        "ownership": "1st",
        "transmission": "Manual",
        "state": "Maharashtra",
        "city": "Nagpur",
        "kmDriven": 45000,
        "address": "Plot no 4, Civil Lines...",
        "name": "Rahul Sharma",
        "phone": "9876543210",
        "scheduledDate": "2023-10-25"
    }
    response = requests.post(url, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 201

def test_loan_request():
    print("\nTesting Loan Request...")
    url = f"{BASE_URL}/loan/apply"
    data = {
        "name": "Priya Singh",
        "mobile": "9876543210",
        "income": 50000,
        "loanAmount": 800000,
        "employmentType": "salaried"
    }
    response = requests.post(url, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 201


def test_vehicle_list():
    print("\nTesting Vehicle List...")
    url = f"{BASE_URL}/marketplace/vehicles"
    response = requests.get(url)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200

def test_create_vehicle():
    print("\nTesting Create Vehicle...")
    url = f"{BASE_URL}/marketplace/vehicles"
    
    # Detailed inspection data matching the new requirement structure roughly
    inspection_data = {
        "exterior": {
            "insp_bumper_status": "OK", "insp_bumper_remark": "Clean",
            "insp_bonnet_status": "Issue", "insp_bonnet_remark": "Dent present"
        },
        "engine": {
            "insp_engine_oil_status": "OK", "insp_engine_oil_remark": "Level good"
        }
    }
    
    # using 'data' instead of 'json' for FormParser compatibility
    data = {
        "make": "Hyundai",
        "model": "Creta",
        "variant": "SX Optional",
        "price": "1450000",
        "year": "2023",
        "mfgYear": "2023",          # camelCase
        "regYear": "2023",          # camelCase
        "status": "For Sale",
        "verified": "true",
        "category": "4w",
        "vehicleType": "Private",   # camelCase
        "color": "White",
        "fuelType": "Diesel",       # camelCase
        "transmission": "Automatic",
        "odometer": 15000,          # camelCase mapped to km_driven
        "regNumber": "MH12PQ5678",  # camelCase
        "chassisNumber": "MA3...123", # camelCase
        "rtoState": "MH",           # camelCase
        "ownership": "1st Owner",
        "validUpto": "2038-05-20",  # camelCase
        "tax": "LTT",
        "rcAvailable": "true",      # camelCase
        "scraped": "false",
        "hypothecation": "Open",
        "insurance": "Comprehensive",
        "insuranceExpiry": "2024-05-20", # camelCase
        "serviceHistory": "Available",   # camelCase
        "remarks": "Excellent condition vehicle",
        "inspection_report": json.dumps(inspection_data)
    }
    
    # To properly test multipart/files, we would add 'files' arg, but for now we test data fields
    response = requests.post(url, data=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 201

if __name__ == "__main__":
    try:
        test_employee_login()
        test_marketplace_register()
        test_marketplace_login()
        test_contact_form()
        test_create_vehicle()  # Added this
        test_vehicle_list()
        test_sell_request()
        test_loan_request()
        print("\nAll tests passed!")
    except Exception as e:
        print(f"\nTest failed: {e}")
