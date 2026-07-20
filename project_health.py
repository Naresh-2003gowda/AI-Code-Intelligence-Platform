def calculate_health(bugs, security_issues, complexity):

    score = 100

    score -= len(bugs) * 5
    score -= len(security_issues) * 10

    score = min(score, complexity["score"])

    score = max(score, 0)

    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "D"

    return {
        "score": score,
        "grade": grade
    }