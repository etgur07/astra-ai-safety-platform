from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Astra Safety API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/panic-alert")
def panic_alert():
    return {"status": "alert_sent"}

@app.post("/share-location")
def share_location():
    return {"status": "location_shared"}

@app.post("/safety-checkin")
def safety_checkin():
    return {"status": "checkin_recorded"}
