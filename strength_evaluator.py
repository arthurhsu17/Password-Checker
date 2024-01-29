import string


def evaluate_strength(password):
    length = len(password)
    score = 0

    # i will create the different variables for the different types of characters
    # and then i will add them together to get the total strength of the password

    has_uppercase = any(character.isupper() for character in password)
    has_lowercase = any(character.islower() for character in password)
    has_numbers = any(character.isdigit() for character in password)
    has_symbols = any(character in string.punctuation for character in password)

    # i will create the scoring for the strength of characters
    if length > 8: 
        score += 1
    if length > 12: 
        score += 2
    if length > 16:
        score += 3

    if has_uppercase:
        score += 1
    if has_lowercase: 
        score += 1
    if has_numbers: 
        score += 1
    if has_symbols:
        score += 1

    if has_lowercase and has_uppercase:
        score += 1
    if has_numbers and (has_lowercase or has_uppercase):
        score += 1
    if has_symbols and (has_lowercase or has_uppercase):
        score += 1

    if "123" or "abc" in password:
        score -= 1
        
    return score

def calculate_score(score):
    if score >= 10:
        return "Very Strong"
    elif score >= 7:
        return "Strong"
    elif score >= 5:
        return "Decent"
    elif score >= 2:
        return "Weak"
    else:
        return "Very Weak"
