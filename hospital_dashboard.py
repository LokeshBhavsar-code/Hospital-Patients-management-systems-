# hospital_dashboard.py
import streamlit as st
import requests
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000"
st.set_page_config(page_title="🏥 Hospital AI Dashboard", layout="wide")

# -------------------- SIDEBAR NAV --------------------
menu = st.sidebar.selectbox(
    "🚀 Navigate",
    [
        "🏠 Home",
        "🧍 Patient Registration",
        "📄 Electronic Health Records (EHR)",
        "📅 Appointments",
        "🩺 Visit Logs",
        "❤️ Remote Monitoring",
        "🧠 Chronic Disease Monitoring",
        "🔁 Referrals",
        "📡 Wearable Data"
    ]
)

# -------------------- HOME PAGE --------------------
if menu == "🏠 Home":
    st.title("🏥 Welcome to Smart Hospital Dashboard")
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image("Hospital_icon.png", caption="Smart Health, Smart Life 💡", use_column_width=True)

    st.markdown("""
    <div style='text-align: center; font-size:18px;'>
        🚀 Empowered by AI, Built for Healthcare Professionals  
        <br>📈 Real-time vitals · 🗂️ Unified records · 📡 Wearable sync  
        <br><br>👉 Use the <b>sidebar</b> to navigate
    </div>
    """, unsafe_allow_html=True)


# -------------------- PATIENT REGISTRATION --------------------
elif menu == "🧍 Patient Registration":
    st.header("🧍 Register New Patient")
    with st.form("register_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", 0, 120)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        contact = st.text_input("Phone Number")
        email = st.text_input("Email")
        address = st.text_area("Address")
        blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        medical_history = st.text_area("Medical History")
        emergency_name = st.text_input("Emergency Contact Name")
        emergency_relation = st.text_input("Relation")
        emergency_phone = st.text_input("Emergency Contact Phone")
        submitted = st.form_submit_button("Register")

    if submitted:
        payload = {
            "name": name,
            "age": age,
            "gender": gender,
            "contact": contact,
            "email": email,
            "address": address,
            "blood_group": blood_group,
            "medical_history": medical_history,
            "emergency_contact": {
                "name": emergency_name,
                "relation": emergency_relation,
                "phone": emergency_phone
            }
        }
        res = requests.post(f"{BASE_URL}/register_patient", json=payload)
        st.json(res.json())

# -------------------- EHR --------------------
elif menu == "📄 Electronic Health Records (EHR)":
    st.header("📄 Create Electronic Health Record")
    with st.form("ehr_form"):
        patient_id = st.text_input("Patient ID")
        allergies = st.text_area("Allergies (comma-separated)")
        chronic = st.text_area("Chronic Conditions")
        medications = st.text_area("Current Medications")
        surgeries = st.text_area("Past Surgeries")
        diagnoses = st.text_area("Recent Diagnoses")
        notes = st.text_area("Doctor Notes")
        submitted = st.form_submit_button("Submit EHR")

    if submitted:
        payload = {
            "patient_id": patient_id,
            "allergies": [x.strip() for x in allergies.split(",")],
            "chronic_conditions": [x.strip() for x in chronic.split(",")],
            "current_medications": [x.strip() for x in medications.split(",")],
            "past_surgeries": [x.strip() for x in surgeries.split(",")],
            "recent_diagnoses": [x.strip() for x in diagnoses.split(",")],
            "doctor_notes": notes
        }
        res = requests.post(f"{BASE_URL}/ehr/create", json=payload)
        st.json(res.json())

    st.subheader("🔍 Retrieve EHR")
    ehr_lookup = st.text_input("Enter Patient ID to Fetch EHR")
    if st.button("Fetch EHR"):
        res = requests.get(f"{BASE_URL}/ehr/{ehr_lookup}")
        st.json(res.json())

# -------------------- APPOINTMENTS --------------------
elif menu == "📅 Appointments":
    st.header("📅 Book Appointment")
    with st.form("appt_form"):
        patient_id = st.text_input("Patient ID")
        doctor_id = st.text_input("Doctor ID")
        date = st.date_input("Date")
        time = st.text_input("Time (HH:MM)")
        reason = st.text_area("Reason for Appointment")
        submitted = st.form_submit_button("Book Appointment")

    if submitted:
        payload = {
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "appointment_date": str(date),
            "appointment_time": time,
            "reason": reason
        }
        res = requests.post(f"{BASE_URL}/appointments/book", json=payload)
        st.json(res.json())

    st.subheader("🔍 Get Doctor Appointments")
    doc_id = st.text_input("Enter Doctor ID")
    if st.button("Fetch Appointments"):
        res = requests.get(f"{BASE_URL}/appointments/{doc_id}")
        st.json(res.json())

# -------------------- VISIT LOG --------------------
elif menu == "🩺 Visit Logs":
    st.header("🩺 Log Patient Visit")
    with st.form("visit_form"):
        patient_id = st.text_input("Patient ID")
        doctor_id = st.text_input("Doctor ID")
        visit_date = st.date_input("Visit Date")
        symptoms = st.text_area("Symptoms")
        diagnosis = st.text_area("Diagnosis")
        treatment = st.text_area("Treatment")
        follow_up = st.checkbox("Follow-up Required")
        next_date = st.date_input("Next Visit Date") if follow_up else ""
        submitted = st.form_submit_button("Log Visit")

    if submitted:
        payload = {
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "visit_date": str(visit_date),
            "symptoms": symptoms,
            "diagnosis": diagnosis,
            "treatment": treatment,
            "follow_up_required": follow_up,
            "next_visit_date": str(next_date) if follow_up else ""
        }
        res = requests.post(f"{BASE_URL}/visit/log", json=payload)
        st.json(res.json())

    st.subheader("🔍 Get Patient Visit Logs")
    pid = st.text_input("Enter Patient ID")
    if st.button("Fetch Visits"):
        res = requests.get(f"{BASE_URL}/visit/{pid}")
        st.json(res.json())

# -------------------- REMOTE MONITORING --------------------
elif menu == "❤️ Remote Monitoring":
    st.header("❤️ Remote Patient Vitals")
    with st.form("remote_form"):
        patient_id = st.text_input("Patient ID")
        device_id = st.text_input("Device ID")
        timestamp = st.text_input("Timestamp (YYYY-MM-DD HH:MM AM/PM)")
        heart_rate = st.number_input("Heart Rate")
        blood_pressure = st.text_input("Blood Pressure (e.g. 120/80)")
        oxygen = st.slider("Oxygen Saturation", 0, 100, 98)
        temp = st.number_input("Body Temp (C)", 25.0, 45.0, 36.6)
        submitted = st.form_submit_button("Submit Vitals")

    if submitted:
        payload = {
            "patient_id": patient_id,
            "device_id": device_id,
            "timestamp": timestamp,
            "heart_rate": heart_rate,
            "blood_pressure": blood_pressure,
            "oxygen_saturation": oxygen,
            "temperature": temp
        }
        res = requests.post(f"{BASE_URL}/record_vitals/{patient_id}", json=payload)
        st.json(res.json())

    st.subheader("🔍 Fetch Vitals")
    pid = st.text_input("Patient ID for Vitals")
    if st.button("Get Vitals"):
        res = requests.get(f"{BASE_URL}/vitals/{pid}")
        st.json(res.json())

# -------------------- CHRONIC DISEASE --------------------
elif menu == "🧠 Chronic Disease Monitoring":
    st.header("🧠 Add Chronic Disease")
    with st.form("chronic_form"):
        patient_id = st.text_input("Patient ID")
        diseases = st.text_area("Chronic Diseases (comma-separated)")
        frequency = st.text_input("Monitoring Frequency")
        doctor = st.text_input("Assigned Doctor")
        lifestyle = st.text_area("Lifestyle Notes")
        submitted = st.form_submit_button("Submit Chronic")

    if submitted:
        payload = {
            "patient_id": patient_id,
            "chronic_diseases": [x.strip() for x in diseases.split(",")],
            "monitoring_frequency": frequency,
            "assigned_doctor": doctor,
            "lifestyle_notes": lifestyle
        }
        res = requests.post(f"{BASE_URL}/chronic/register", json=payload)
        st.json(res.json())

    st.subheader("📊 Log Chronic Reading")
    with st.form("log_form"):
        reading_date = st.date_input("Reading Date")
        sugar = st.number_input("Blood Sugar")
        bp = st.text_input("Blood Pressure")
        weight = st.number_input("Weight (kg)")
        notes = st.text_area("Notes")
        submitted = st.form_submit_button("Log Reading")

    if submitted:
        payload = {
            "patient_id": patient_id,
            "reading_date": str(reading_date),
            "blood_sugar_level": sugar,
            "blood_pressure": bp,
            "weight": weight,
            "notes": notes
        }
        res = requests.post(f"{BASE_URL}/chronic/log_reading", json=payload)
        st.json(res.json())

    st.subheader("🔍 Get Chronic History")
    if st.button("Get Chronic Logs"):
        res = requests.get(f"{BASE_URL}/chronic/{patient_id}")
        st.json(res.json())

# -------------------- REFERRALS --------------------
elif menu == "🔁 Referrals":
    st.header("🔁 Refer a Patient")
    with st.form("refer_form"):
        patient_id = st.text_input("Patient ID")
        curr_dept = st.text_input("Current Department")
        ref_dept = st.text_input("Referred Department")
        reason = st.text_input("Reason")
        referred_by = st.text_input("Referred By (Doctor ID)")
        notes = st.text_area("Notes")
        submitted = st.form_submit_button("Submit Referral")

    if submitted:
        payload = {
            "patient_id": patient_id,
            "current_department": curr_dept,
            "referred_department": ref_dept,
            "reason": reason,
            "referred_by": referred_by,
            "notes": notes
        }
        res = requests.post(f"{BASE_URL}/referral", params=payload)
        st.json(res.json())

    st.subheader("🔍 Lookup Referral")
    ref_id = st.text_input("Referral ID")
    if st.button("Get Referral"):
        res = requests.get(f"{BASE_URL}/referral/{ref_id}")
        st.json(res.json())

# -------------------- WEARABLE --------------------
elif menu == "📡 Wearable Data":
    st.header("📡 Sync Wearable Device")
    with st.form("wearable_form"):
        patient_id = st.text_input("Patient ID")
        device_id = st.text_input("Device ID")
        timestamp = st.text_input("Timestamp")
        heart_rate = st.number_input("Heart Rate")
        oxygen = st.slider("Oxygen Saturation", 0, 100, 98)
        steps = st.number_input("Steps Count", 0)
        glucose = st.number_input("Glucose Level")
        submitted = st.form_submit_button("Send Data")

    if submitted:
        payload = {
            "patient_id": patient_id,
            "device_id": device_id,
            "timestamp": timestamp,
            "heart_rate": heart_rate,
            "oxygen_saturation": oxygen,
            "steps_count": steps,
            "glucose_level": glucose
        }
        res = requests.post(f"{BASE_URL}/wearable", json=payload)
        st.json(res.json())

    st.subheader("🔍 Get Wearable Data")
    data_id = st.text_input("Data ID")
    if st.button("Fetch Wearable Log"):
        res = requests.get(f"{BASE_URL}/wearable/{data_id}")
        st.json(res.json())
