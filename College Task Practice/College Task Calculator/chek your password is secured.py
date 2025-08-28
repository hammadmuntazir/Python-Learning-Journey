import string

while True:
    psw = input("Enter your password: ")
    
    # Check if all characters in the password are printable
    is_printable = all(char in string.printable for char in psw)
    
    # Check password length
    is_length_valid = len(psw) >= 8
    
    # Check if password contains at least one digit
    has_digit = any(char.isdigit() for char in psw)
    
    # Check if password contains at least one uppercase letter
    has_upper = any(char.isupper() for char in psw)
    
    # Check if password contains at least one lowercase letter
    has_lower = any(char.islower() for char in psw)
    
    # Check if password contains at least one special character
    has_special = any(char in string.punctuation for char in psw)
    
    # Validate all conditions
    if is_printable and is_length_valid and has_digit and has_upper and has_lower and has_special:
        print("Your password is secure.")
        break
    else:
        print("Your password is not secure. Please ensure it meets the following criteria:")
        print("- At least 8 characters long")
        print("- Contains at least one digit")
        print("- Contains at least one uppercase letter")
        print("- Contains at least one lowercase letter")
        print("- Contains at least one special character")
        print(" ")