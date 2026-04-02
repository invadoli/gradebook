def parse_grade(value):
    try:
        grade = int(value)
    except (TypeError, ValueError):
        raise ValueError(f"Grade must be a number. Received: '{value}'")
    
    if not (0 <= grade <= 100):
        raise ValueError(f"Grade must be between 0 and 100. Received: {grade}")
    
    return grade