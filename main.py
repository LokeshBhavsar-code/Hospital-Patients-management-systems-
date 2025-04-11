import sys
import os
from fastapi import FastAPI
sys.path.append(os.path.abspath("helper"))

from helper.csv_helper import load_data

# Initialize FastAPI
app = FastAPI(
    title="HOSPITAL_MANAGEMENT",
    description="The **Hospital Management System** streamlines hospital operations, manages patient records, and facilitates doctor referrals for efficient medical processes.",
)

# Load CSV data into memory at startup
dataframes = load_data()


# Import routes (Ensure these route files exist)
try:
    from routes.patients_route import router as patients_router
    app.include_router(patients_router, prefix="/patients", tags=["Patients"])

    from routes.EHR_route import router as ehr_router
    app.include_router(ehr_router, prefix="/ehr", tags=["EHR"])

    from routes.appointment_management_route import router as appointment_router
    app.include_router(appointment_router, prefix="/appointments", tags=["Appointments"])

    from routes.visit_log_route import router as visit_router
    app.include_router(visit_router, prefix="/visit_logs", tags=["Visit Logs"])

    from routes.referral_route import router as referral_router
    app.include_router(referral_router, prefix="/referral", tags=["Referrals"])

    from routes.chronic_disease_route import router as chronic_router
    app.include_router(chronic_router, prefix="/chronic", tags=["Chronic Diseases"])

    from routes.wearable_route import router as wearable_router
    app.include_router(wearable_router, prefix="/wearable", tags=["Wearable Data"])
    
    from routes.remote_patient_route import router as remote_patient_router
    app.include_router(remote_patient_router, prefix="/remote_patient", tags=["Remote Patients"])
    
    
except Exception as e:
    print(f"Error importing routes: {e}")

# Run the FastAPI app with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
