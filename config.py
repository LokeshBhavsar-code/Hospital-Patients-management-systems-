import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
PATIENTS_CSV = os.path.join(DATA_DIR, "patients.csv")  ## API 1
EHR_CSV_PATH = os.path.join(DATA_DIR, "EHR.csv")  ## API 2
VISIT_LOG_CSV = os.path.join(DATA_DIR, "visit_logs.csv")
REFERRAL_CSV = os.path.join(os.path.dirname(__file__), "data", "referral.csv")
CHRONIC_PATIENTS_CSV = os.path.join(os.path.dirname(__file__), "data", "chronic_patients.csv")
CHRONIC_LOGS_CSV = os.path.join(os.path.dirname(__file__), "data", "chronic_logs.csv")
WEARABLE_CSV =  os.path.join(os.path.dirname(__file__), "data", "wearable.csv")
VITALS_CSV = os.path.join(os.path.dirname(__file__), "data", "vitals_log.csv")
APPOINTMENTS_CSV = os.path.join(os.path.dirname(__file__), "data", "appointments.csv")
DOCTOR_AVAILABILITY_CSV = os.path.join(os.path.dirname(__file__), "data", "doctor_availability.csv")