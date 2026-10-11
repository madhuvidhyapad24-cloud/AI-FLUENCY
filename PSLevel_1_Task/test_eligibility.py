def check_exam_eligibility(attendance):
    if attendance < 0 or attendance > 100:
        return "Invalid attendance"
    if attendance >= 75:
        return f"Eligible: {attendance}%"
    return f"Not eligible: {attendance}%"

for attendance in [82, 70, 50, 120]:
    print(check_exam_eligibility(attendance))
