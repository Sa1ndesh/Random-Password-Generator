@echo off
echo 🔐 Starting Random Password Generator (GUI Version)
echo ==================================================
echo Installing dependencies if needed...
pip install pyperclip >nul 2>&1
echo Starting GUI...
python gui_password_generator.py
pause
