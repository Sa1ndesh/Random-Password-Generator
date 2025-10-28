#!/usr/bin/env python3
"""
Demonstration script for the Random Password Generator
Shows examples of both command-line and GUI functionality
"""

import random
import string
import sys
import os

def demo_password_generation():
    """Demonstrate password generation with different settings"""
    print("🔐 Random Password Generator - Demo")
    print("=" * 50)
    print()
    
    # Demo configurations
    configs = [
        {
            "name": "🔒 Basic Security (8 chars, letters + numbers)",
            "length": 8,
            "chars": string.ascii_letters + string.digits,
            "count": 3
        },
        {
            "name": "🛡️ High Security (12 chars, all types)",
            "length": 12,
            "chars": string.ascii_letters + string.digits + string.punctuation,
            "count": 3
        },
        {
            "name": "🏰 Maximum Security (16 chars, all types)",
            "length": 16,
            "chars": string.ascii_letters + string.digits + string.punctuation,
            "count": 3
        },
        {
            "name": "📱 PIN Code (4 digits)",
            "length": 4,
            "chars": string.digits,
            "count": 5
        }
    ]
    
    for config in configs:
        print(f"{config['name']}")
        print("-" * len(config['name']))
        
        for i in range(config['count']):
            password = ''.join(random.choice(config['chars']) for _ in range(config['length']))
            strength = calculate_demo_strength(password, config['chars'])
            print(f"  {i+1}. {password} ({strength})")
        
        print()

def calculate_demo_strength(password, charset):
    """Calculate strength for demo purposes"""
    length = len(password)
    has_letters = any(c in string.ascii_letters for c in charset)
    has_numbers = any(c in string.digits for c in charset)
    has_symbols = any(c in string.punctuation for c in charset)
    
    char_types = sum([has_letters, has_numbers, has_symbols])
    
    if length < 6:
        return "Very Weak"
    elif length < 8:
        return "Weak"
    elif length < 12:
        if char_types >= 3:
            return "Strong"
        elif char_types >= 2:
            return "Moderate"
        else:
            return "Weak"
    else:
        if char_types >= 3:
            return "Very Strong"
        elif char_types >= 2:
            return "Strong"
        else:
            return "Moderate"

def show_features():
    """Show available features"""
    print("✨ Available Features:")
    print("=" * 30)
    print()
    
    print("📋 COMMAND-LINE VERSION (main.py):")
    features_cli = [
        "Interactive password length selection",
        "Choose character types (letters, numbers, symbols)",
        "Password strength indicator",
        "Generate multiple passwords in one session",
        "Input validation and error handling",
        "User-friendly prompts and feedback"
    ]
    
    for feature in features_cli:
        print(f"  ✅ {feature}")
    
    print()
    print("🖥️ GUI VERSION (gui_password_generator.py):")
    features_gui = [
        "All command-line features plus:",
        "Graphical user interface with tkinter",
        "Separate uppercase/lowercase letter options",
        "Advanced exclusion options (similar/ambiguous chars)",
        "Copy to clipboard functionality",
        "Color-coded password strength indicator",
        "Spinbox for easy length selection (4-128)",
        "Real-time password generation",
        "Clear and regenerate options"
    ]
    
    for feature in features_gui:
        print(f"  ✅ {feature}")
    
    print()

def show_usage_examples():
    """Show usage examples"""
    print("🚀 Usage Examples:")
    print("=" * 25)
    print()
    
    print("💻 Command-Line Usage:")
    print("  python main.py")
    print("  # Follow the interactive prompts")
    print()
    
    print("🖥️ GUI Usage:")
    print("  python gui_password_generator.py")
    print("  # Use the graphical interface")
    print()
    
    print("🧪 Run Tests:")
    print("  python test_generator.py")
    print("  # Verify all functionality works")
    print()
    
    print("⚡ Quick Launch (Windows):")
    print("  run_cli.bat  # Command-line version")
    print("  run_gui.bat  # GUI version")
    print()

def main():
    """Main demo function"""
    print("🎯 Welcome to the Random Password Generator Demo!")
    print()
    
    while True:
        print("Choose an option:")
        print("1. 🎲 Generate demo passwords")
        print("2. ✨ Show features")
        print("3. 🚀 Show usage examples")
        print("4. 🏃 Launch command-line version")
        print("5. 🖥️ Launch GUI version")
        print("6. 🚪 Exit")
        print()
        
        try:
            choice = input("Enter your choice (1-6): ").strip()
            print()
            
            if choice == '1':
                demo_password_generation()
            elif choice == '2':
                show_features()
            elif choice == '3':
                show_usage_examples()
            elif choice == '4':
                print("🏃 Launching command-line version...")
                os.system("python main.py")
            elif choice == '5':
                print("🖥️ Launching GUI version...")
                os.system("python gui_password_generator.py")
            elif choice == '6':
                print("👋 Thanks for using the Random Password Generator!")
                break
            else:
                print("❌ Invalid choice. Please enter 1-6.")
            
            print()
            
        except KeyboardInterrupt:
            print("\n\n👋 Thanks for using the Random Password Generator!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
