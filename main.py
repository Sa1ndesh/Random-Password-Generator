import random
import string

def generate_password_cli():
    """
    Command-line version of the Random Password Generator
    """
    print("=== Random Password Generator ===")
    print("Welcome to the Random Password Generator!")
    print("-" * 40)

    try:
        # Get password length from user
        length = int(input("Enter password length: "))
        if length <= 0:
            print("❌ Password length must be positive.")
            return

        # Get character type preferences
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Build character set based on user preferences
        characters = ""
        if use_letters:
            characters += string.ascii_letters
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        # Validate that at least one character type is selected
        if not characters:
            print("❌ You must select at least one character type!")
            return

        # Generate password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display results
        print("\n" + "=" * 40)
        print(f"✅ Generated Password: {password}")
        print("=" * 40)
        
        # Show password strength info
        strength = check_password_strength(password, use_letters, use_numbers, use_symbols)
        print(f"🛡️  Password Strength: {strength}")
        
        # Ask if user wants to generate another password
        another = input("\nGenerate another password? (y/n): ").lower()
        if another == 'y':
            print("\n")
            generate_password_cli()

    except ValueError:
        print("❌ Invalid input! Please enter numeric values for length.")
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for using Random Password Generator!")

def check_password_strength(password, has_letters, has_numbers, has_symbols):
    """
    Check the strength of the generated password
    """
    length = len(password)
    
    if length < 8:
        return "Weak (too short)"
    elif length >= 8 and length < 12:
        if has_letters and has_numbers and has_symbols:
            return "Strong"
        elif (has_letters and has_numbers) or (has_letters and has_symbols):
            return "Moderate"
        else:
            return "Weak (limited character types)"
    else:  # length >= 12
        if has_letters and has_numbers and has_symbols:
            return "Very Strong"
        elif (has_letters and has_numbers) or (has_letters and has_symbols):
            return "Strong"
        else:
            return "Moderate"

if __name__ == "__main__":
    try:
        generate_password_cli()
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("Please try again.")
