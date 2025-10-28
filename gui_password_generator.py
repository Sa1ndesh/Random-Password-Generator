import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import pyperclip

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Random Password Generator")
        self.root.geometry("450x500")
        self.root.resizable(False, False)
        
        # Configure style
        self.setup_styles()
        
        # Create GUI elements
        self.create_widgets()
        
        # Center the window
        self.center_window()

    def setup_styles(self):
        """Setup custom styles for the GUI"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure custom styles
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Heading.TLabel', font=('Arial', 10, 'bold'))
        style.configure('Generate.TButton', font=('Arial', 10, 'bold'))

    def create_widgets(self):
        """Create and arrange all GUI widgets"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="🔐 Random Password Generator", 
                               style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Password Length Section
        length_frame = ttk.LabelFrame(main_frame, text="Password Length", padding="10")
        length_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        ttk.Label(length_frame, text="Length:").grid(row=0, column=0, sticky=tk.W)
        self.length_var = tk.StringVar(value="12")
        length_spinbox = ttk.Spinbox(length_frame, from_=4, to=128, width=10, 
                                   textvariable=self.length_var)
        length_spinbox.grid(row=0, column=1, padx=(10, 0), sticky=tk.W)
        
        # Character Types Section
        char_frame = ttk.LabelFrame(main_frame, text="Character Types", padding="10")
        char_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        self.letters_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(char_frame, text="📝 Uppercase Letters (A-Z)", 
                       variable=self.uppercase_var).grid(row=0, column=0, sticky=tk.W, pady=2)
        ttk.Checkbutton(char_frame, text="📝 Lowercase Letters (a-z)", 
                       variable=self.lowercase_var).grid(row=1, column=0, sticky=tk.W, pady=2)
        ttk.Checkbutton(char_frame, text="🔢 Numbers (0-9)", 
                       variable=self.numbers_var).grid(row=2, column=0, sticky=tk.W, pady=2)
        ttk.Checkbutton(char_frame, text="🔣 Symbols (!@#$%^&*)", 
                       variable=self.symbols_var).grid(row=3, column=0, sticky=tk.W, pady=2)
        
        # Advanced Options Section
        advanced_frame = ttk.LabelFrame(main_frame, text="Advanced Options", padding="10")
        advanced_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        self.exclude_similar_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(advanced_frame, text="🚫 Exclude similar characters (0, O, l, I)", 
                       variable=self.exclude_similar_var).grid(row=0, column=0, sticky=tk.W, pady=2)
        
        self.exclude_ambiguous_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(advanced_frame, text="🚫 Exclude ambiguous symbols ({ } [ ] ( ) / \\ ' \" ~ , ; . < >)", 
                       variable=self.exclude_ambiguous_var).grid(row=1, column=0, sticky=tk.W, pady=2)
        
        # Generate Button
        generate_btn = ttk.Button(main_frame, text="🎲 Generate Password", 
                                command=self.generate_password, style='Generate.TButton')
        generate_btn.grid(row=4, column=0, columnspan=2, pady=(0, 15), sticky=(tk.W, tk.E))
        
        # Result Section
        result_frame = ttk.LabelFrame(main_frame, text="Generated Password", padding="10")
        result_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        self.result_var = tk.StringVar()
        result_entry = ttk.Entry(result_frame, textvariable=self.result_var, 
                               font=('Courier', 12), width=40, state='readonly')
        result_entry.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky=(tk.W, tk.E))
        
        # Buttons for result
        copy_btn = ttk.Button(result_frame, text="📋 Copy to Clipboard", 
                            command=self.copy_password)
        copy_btn.grid(row=1, column=0, padx=(0, 5), sticky=tk.W)
        
        clear_btn = ttk.Button(result_frame, text="🗑️ Clear", 
                             command=self.clear_password)
        clear_btn.grid(row=1, column=1, padx=(5, 0), sticky=tk.E)
        
        # Password Strength Indicator
        self.strength_var = tk.StringVar()
        self.strength_label = ttk.Label(main_frame, textvariable=self.strength_var, 
                                      font=('Arial', 10, 'bold'))
        self.strength_label.grid(row=6, column=0, columnspan=2, pady=(0, 10))
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        result_frame.columnconfigure(0, weight=1)
        result_frame.columnconfigure(1, weight=1)

    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def generate_password(self):
        """Generate a password based on user settings"""
        try:
            # Get password length
            length = int(self.length_var.get())
            if length <= 0:
                raise ValueError("Password length must be positive")
            
            # Build character set
            characters = ""
            
            if self.uppercase_var.get():
                characters += string.ascii_uppercase
            if self.lowercase_var.get():
                characters += string.ascii_lowercase
            if self.numbers_var.get():
                characters += string.digits
            if self.symbols_var.get():
                characters += string.punctuation
            
            # Apply exclusions
            if self.exclude_similar_var.get():
                similar_chars = "0Ol1I"
                characters = ''.join(c for c in characters if c not in similar_chars)
            
            if self.exclude_ambiguous_var.get():
                ambiguous_chars = "{}[]()/'\"~,;.<>"
                characters = ''.join(c for c in characters if c not in ambiguous_chars)
            
            # Validate character set
            if not characters:
                messagebox.showwarning("Selection Error", 
                                     "Please select at least one character type!")
                return
            
            # Generate password
            password = ''.join(random.choice(characters) for _ in range(length))
            
            # Display password
            self.result_var.set(password)
            
            # Update strength indicator
            strength = self.calculate_strength(password)
            self.update_strength_display(strength)
            
        except ValueError as e:
            messagebox.showerror("Invalid Input", 
                               f"Please enter a valid positive number for length!\nError: {e}")

    def calculate_strength(self, password):
        """Calculate password strength"""
        length = len(password)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in string.punctuation for c in password)
        
        # Count character types
        char_types = sum([has_upper, has_lower, has_digit, has_symbol])
        
        # Calculate strength
        if length < 8:
            return "Weak"
        elif length < 12:
            if char_types >= 3:
                return "Strong"
            elif char_types >= 2:
                return "Moderate"
            else:
                return "Weak"
        else:  # length >= 12
            if char_types >= 4:
                return "Very Strong"
            elif char_types >= 3:
                return "Strong"
            elif char_types >= 2:
                return "Moderate"
            else:
                return "Weak"

    def update_strength_display(self, strength):
        """Update the strength indicator with color coding"""
        colors = {
            "Very Strong": "green",
            "Strong": "blue",
            "Moderate": "orange",
            "Weak": "red"
        }
        
        icons = {
            "Very Strong": "🛡️",
            "Strong": "🔒",
            "Moderate": "⚠️",
            "Weak": "❌"
        }
        
        self.strength_var.set(f"{icons.get(strength, '❓')} Password Strength: {strength}")
        self.strength_label.configure(foreground=colors.get(strength, "black"))

    def copy_password(self):
        """Copy the generated password to clipboard"""
        password = self.result_var.get()
        if password:
            try:
                pyperclip.copy(password)
                messagebox.showinfo("Success", "Password copied to clipboard! 📋")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to copy to clipboard: {e}")
        else:
            messagebox.showwarning("No Password", "Generate a password first!")

    def clear_password(self):
        """Clear the password field"""
        self.result_var.set("")
        self.strength_var.set("")

def main():
    """Main function to run the GUI application"""
    try:
        root = tk.Tk()
        app = PasswordGeneratorGUI(root)
        root.mainloop()
    except ImportError:
        print("❌ Error: pyperclip library not found!")
        print("Please install it using: pip install pyperclip")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
