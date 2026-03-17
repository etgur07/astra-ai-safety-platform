"""
Astra - Panic Alert Prototype

This module simulates the core panic alert logic of the Astra safety system.
"""

from datetime import datetime


def trigger_panic(user_id, latitude, longitude, message=None):
    """
    Simulates a panic alert being triggered by a user.
    """

    alert = {
        "user_id": user_id,
        "latitude": latitude,
        "longitude": longitude,
        "message": message,
        "status": "active",
        "created_at": datetime.utcnow().isoformat()
    }

    # Simulated safety contacts
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
        "contacts_notified": len(contacts)
    }


if __name__ == "__main__":
    result = trigger_panic(
        user_id="user_001",
        latitude=40.7128,
        longitude=-74.0060,
        message="I feel unsafe"
    )
    print(result)


# AI risk evaluation simulation
risk_level = "HIGH_RISK"

if risk_level == "HIGH_RISK":
    print("AI detected high risk → escalating alert")
