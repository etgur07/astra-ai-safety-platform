"""
Astra - Data Models (Prototype)
"""

class User:
    def __init__(self, user_id, full_name, role):
        self.user_id = user_id
        self.full_name = full_name
        self.role = role


class SafetyContact:
    def __init__(self, user_id, name, phone):
        self.user_id = user_id
        self.name = name
        self.phone = phone


class PanicAlert:
    def __init__(self, user_id, lat, lng, status="active"):
        self.user_id = user_id
        self.lat = lat
        self.lng = lng
        self.status = status


class CheckIn:
    def __init__(self, user_id, status, due_at):
        self.user_id = user_id
        self.status = status
        self.due_at = due_at


class RiskScore:
    def __init__(self, user_id, score, level):
        self.user_id = user_id
        self.score = score
        self.level = level
