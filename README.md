# Password Strength Checker 🔒

A Python-based tool to evaluate password strength based on structure, entropy, and exposure to known breaches using the HaveIBeenPwned API.

---

## Features
- ✅ Checks password length and complexity (uppercase, lowercase, digits, symbols).
- ✅ Rates password as **Strong**, **Moderate**, or **Weak**.
- ✅ Calculates password **entropy** (security strength in bits).
- ✅ Verifies if the password has been leaked in known data breaches.
- ✅ Provides detailed feedback on missing elements.

---

## How it Works

- The password is evaluated for:
  - Minimum length (8 characters).
  - Presence of uppercase, lowercase, digits, and special characters.
- Password is **hashed with SHA-1** and checked against the [Pwned Passwords API](https://haveibeenpwned.com/API/v3#PwnedPasswords).
- Displays whether your password is **safe** or has been **compromised**.
  
---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/password-strength-checker.git
    ```
2. Navigate to the project directory:
    ```bash
    cd password-strength-checker
    ```
3. Install the required Python libraries:
    ```bash
    pip install requests
    ```

---

## Usage

Run the script:
```bash
python password_checker.py
