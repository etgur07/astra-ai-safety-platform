"""
Astra - Check-in Monitor Prototype

This module simulates monitoring overdue safety check-ins.
"""

from datetime import datetime, timedelta


def check_overdue_checkins(check_ins):
    """
    Detects overdue check-ins and triggers escalation logic.
    """

    now = datetime.utcnow()
    overdue = []

    for check in check_ins:
        due_time = check["due_at"]

        if check["status"] == "no_response" and due_time < now:
            overdue.append(check)

    print(f"⚠️ Overdue check-ins: {len(overdue)}")

    return overdue


if __name__ == "__main__":
    sample_checkins = [
        {
            "user_id": "user_001",
            "status": "no_response",
            "due_at": datetime.utcnow() - timedelta(minutes=10)
        },
        {
            "user_id": "user_002",
            "status": "safe",
            "due_at": datetime.utcnow()
        }
    ]

    result = check_overdue_checkins(sample_checkins)
    print(result)
