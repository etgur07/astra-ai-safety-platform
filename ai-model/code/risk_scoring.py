def calculate_risk(user_data):
    risk_score = 0

    # Missed check-in
    if user_data["check_in_status"] == "no_response":
        risk_score += 40

    # Inactivity (no movement)
    if user_data["movement_speed"] < 0.5:
        risk_score += 20

    # Late night movement
    if user_data["hour"] >= 23 or user_data["hour"] <= 5:
        risk_score += 15

    # Safety mode active
    if user_data["safety_mode"]:
        risk_score += 10

    return risk_score


def evaluate_risk(user_data):
    score = calculate_risk(user_data)

    if score > 60:
        return "HIGH_RISK"
    elif score > 30:
        return "MEDIUM_RISK"
    else:
        return "LOW_RISK"
