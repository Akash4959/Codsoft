import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
   
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''

   
    all_chars = lowercase + uppercase + digits + special_chars
    
    if not all_chars:
        raise ValueError("At least one character set must be selected.")

    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4): "))
            if length < 4:
                print("Password length must be at least 4.")
                continue
            
            use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

            password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
            print(f"\nGenerated Password: {password}\n")

            if input("Generate another password? (y/n): ").lower() != 'y':
                break

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
