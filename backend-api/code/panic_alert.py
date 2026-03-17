from datetime import datetime


def evaluate_risk():
    """
    Simulated AI risk evaluation.
    In real system, this would call the Python risk model.
    """
    return "HIGH_RISK"


def trigger_panic(user_id, latitude, longitude, message=None):
    """
    Simulates a panic alert being triggered by a user.
    """

    # Step 1: AI risk evaluation
    risk_level = evaluate_risk()

    print(f"AI Risk Level: {risk_level}")

    # Step 2: Only escalate if high risk
    if risk_level != "HIGH_RISK":
        print("Risk not high → no escalation")
        return {
            "success": False,
            "reason": "Risk level too low"
        }

    # Step 3: Create alert
    alert = {
        "user_id": user_id,
        "latitude": latitude,
        "longitude": longitude,
        "message": message,
        "status": "active",
        "created_at": datetime.utcnow().isoformat()
    }

    # Step 4: Simulated safety contacts
    contacts = [
        {"name": "Mom", "phone": "+123456789"},
        {"name": "Friend", "phone": "+987654321"}
    ]

    print("🚨 PANIC ALERT TRIGGERED")
    print(f"User: {user_id}")
    print(f"Location: {latitude}, {longitude}")
    print(f"Contacts notified: {len(contacts)}")

    return {
        "success": True,
        "alert": alert,
        "contacts_notified": len(contacts),
        "risk_level": risk_level
    }


if __name__ == "__main__":
    result = trigger_panic(
        user_id="user_001",
        latitude=40.7128,
        longitude=-74.0060,
        message="I feel unsafe"
    )
    print(result)
