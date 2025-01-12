import random
import string

def generate_password(length=12, include_symbols=True, include_numbers=True):
    letters = string.ascii_letters  # Uppercase and lowercase letters
    digits = string.digits if include_numbers else ""
    symbols = string.punctuation if include_symbols else ""
    
    all_characters = letters + digits + symbols
    
    if not all_characters:
        raise ValueError("At least one type of character must be included!")
    
    password = [
        random.choice(letters),
        random.choice(digits) if include_numbers else "",
        random.choice(symbols) if include_symbols else ""
    ]
    
    password += random.choices(all_characters, k=length - len(password))
    
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("Password Generator")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        include_symbols = input("Include symbols? (y/n, default y): ").strip().lower() != "n"
        include_numbers = input("Include numbers? (y/n, default y): ").strip().lower() != "n"
        
        password = generate_password(length, include_symbols, include_numbers)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
