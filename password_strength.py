import re

def password_strength(password: str) -> str:
    score = 0
    
    # Length check
    if len(password) >= 8:
        score += 1
    
    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    
    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    
    # Digit check
    if re.search(r"[0-9]", password):
        score += 1
    
    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    
    # Strength levels
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

pw = input("Enter a password: ")
print("Password Strength:", password_strength(pw))
