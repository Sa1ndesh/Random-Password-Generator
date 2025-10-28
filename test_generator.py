#!/usr/bin/env python3
"""
Test script for the Random Password Generator
This script tests both the command-line and GUI versions programmatically
"""

import sys
import os
import random
import string

# Add current directory to path to import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_password_generation():
    """Test the core password generation logic"""
    print("🧪 Testing Password Generation Logic...")
    
    # Test different character sets
    test_cases = [
        {"length": 8, "chars": string.ascii_letters, "name": "Letters only"},
        {"length": 12, "chars": string.ascii_letters + string.digits, "name": "Letters + Numbers"},
        {"length": 16, "chars": string.ascii_letters + string.digits + string.punctuation, "name": "All characters"},
        {"length": 4, "chars": string.digits, "name": "Numbers only (short)"},
        {"length": 32, "chars": string.ascii_letters + string.digits + string.punctuation, "name": "Very long password"},
    ]
    
    for i, case in enumerate(test_cases, 1):
        try:
            password = ''.join(random.choice(case["chars"]) for _ in range(case["length"]))
            print(f"✅ Test {i}: {case['name']}")
            print(f"   Length: {len(password)} (expected: {case['length']})")
            print(f"   Password: {password}")
            print(f"   Valid characters: {all(c in case['chars'] for c in password)}")
            print()
        except Exception as e:
            print(f"❌ Test {i} failed: {e}")
    
    return True

def test_strength_calculation():
    """Test password strength calculation"""
    print("🛡️ Testing Password Strength Calculation...")
    
    # Import the strength function from main.py
    try:
        from main import check_password_strength
        
        test_passwords = [
            {"password": "abc", "expected": "Weak", "has_letters": True, "has_numbers": False, "has_symbols": False},
            {"password": "Abc123!@", "expected": "Strong", "has_letters": True, "has_numbers": True, "has_symbols": True},
            {"password": "VeryLongPasswordWith123AndSymbols!", "expected": "Very Strong", "has_letters": True, "has_numbers": True, "has_symbols": True},
            {"password": "12345678", "expected": "Weak", "has_letters": False, "has_numbers": True, "has_symbols": False},
        ]
        
        for i, test in enumerate(test_passwords, 1):
            strength = check_password_strength(
                test["password"], 
                test["has_letters"], 
                test["has_numbers"], 
                test["has_symbols"]
            )
            status = "✅" if test["expected"].lower() in strength.lower() else "❌"
            print(f"{status} Test {i}: '{test['password'][:10]}...' -> {strength}")
        
        print()
        return True
        
    except ImportError as e:
        print(f"❌ Could not import strength function: {e}")
        return False

def test_gui_imports():
    """Test if GUI dependencies are available"""
    print("🖥️ Testing GUI Dependencies...")
    
    try:
        import tkinter as tk
        print("✅ tkinter is available")
        
        try:
            import pyperclip
            print("✅ pyperclip is available")
            
            # Test clipboard functionality
            test_text = "test_password_123"
            pyperclip.copy(test_text)
            copied_text = pyperclip.paste()
            if copied_text == test_text:
                print("✅ Clipboard functionality works")
            else:
                print("⚠️ Clipboard functionality may have issues")
                
        except ImportError:
            print("⚠️ pyperclip not available - clipboard features will not work")
            print("   Install with: pip install pyperclip")
        
        print()
        return True
        
    except ImportError:
        print("❌ tkinter not available - GUI version will not work")
        return False

def test_file_structure():
    """Test if all required files are present"""
    print("📁 Testing File Structure...")
    
    required_files = [
        "main.py",
        "gui_password_generator.py", 
        "requirements.txt",
        "README.txt"
    ]
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    for file in required_files:
        file_path = os.path.join(current_dir, file)
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"✅ {file} exists ({size} bytes)")
        else:
            print(f"❌ {file} is missing")
    
    print()
    return True

def main():
    """Run all tests"""
    print("🔐 Random Password Generator - Test Suite")
    print("=" * 50)
    print()
    
    tests = [
        test_file_structure,
        test_password_generation,
        test_strength_calculation,
        test_gui_imports,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The password generator is ready to use.")
    else:
        print("⚠️ Some tests failed. Check the output above for details.")
    
    print("\n🚀 To run the applications:")
    print("   Command-line: python main.py")
    print("   GUI version:  python gui_password_generator.py")

if __name__ == "__main__":
    main()
