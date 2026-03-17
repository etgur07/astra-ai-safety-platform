def calculate_risk(route_deviation, missed_checkin, inactivity_minutes):
    score = 0

    if route_deviation:
        score += 2

    if missed_checkin:
        score += 3

    if inactivity_minutes > 10:
        score += 2

    if score >= 5:
        return "HIGH"
    elif score >= 3:
        return "MEDIUM"
    else:
        return "LOW"
