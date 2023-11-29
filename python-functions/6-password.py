def validate_password(password):
    if len(password) < 8:  
        return False  
    if any(char.isupper() for char in password):
        return False
    if any(char.islower() for char in password):
        return False
    if any(char.isdigit() for char in password):
        return False


    