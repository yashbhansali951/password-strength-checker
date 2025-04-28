import re
import hashlib
import requests
import random
import string
import math

class PasswordChecker:
    def check_strength(self, password):
        if len(password) < 8:
            print ("Password is too short. Minimum length is 8 characters.")

        issues = []
        if not any(char.isupper() for char in password):
            issues.append("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in password):
            issues.append("Password must contain at least one lowercase letter.")
        if not any(char.isdigit() for char in password):
            issues.append("Password must contain at least one digit.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            issues.append("Password must contain at least one special character.")

        if not issues:
            strength = "Password is strong."
        elif len(issues) <= 2:
            strength = "Password is moderate."
        else:
            strength = "Password is weak."

        print(strength)
        for issue in issues:
            print(issue)

        # Hash the password using SHA-1
        sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        first5, tail = sha1_password[:5], sha1_password[5:]

        # Check against the Pwned Passwords database
        try:
            url = f"https://api.pwnedpasswords.com/range/{first5}"
            res = requests.get(url, timeout=5)

            if res.status_code != 200:
                raise RuntimeError(f"Error fetching: {res.status_code}")

            found = False
            hashes = (line.split(':') for line in res.text.splitlines())
            for h, count in hashes:
                if h == tail:
                    print(f"⚠️  Password found {count} times! Choose a stronger one.")
                    found = True
                    break
            if not found:
                print("✅ Password not found. Good to go!")
        except requests.RequestException as e:
            print(f"Network error occurred: {e}")
    
    def suggest_password(self, length=16):
        if length < 8:
            length = 8  # Minimum 8 characters for security

        characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Suggested password: {password}")

    def calculate_entropy(self, password):
        charset = 0
        if any(c.islower() for c in password):
            charset += 26
        if any(c.isupper() for c in password):
            charset += 26
        if any(c.isdigit() for c in password):
            charset += 10
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            charset += 32  # Approximate count of common special symbols

        if charset == 0:
            return 0  # No valid characters

        entropy = len(password) * math.log2(charset)
        return round(entropy, 2)

if __name__ == "__main__":
    checker = PasswordChecker()
    password = input("Enter a password to check: ")
    checker.check_strength(password)
    suggest = input("\nWould you like a strong password suggestion? (yes/no): ").strip().lower()
    if suggest in ('yes', 'y'):
        checker.suggest_password()
    else:
        print("No password suggestion provided.")
    
    entropy = checker.calculate_entropy(password)
    print(f"Password entropy: {entropy} bits.")
    
    API_SOURCE = "https://haveibeenpwned.com/"
    print(f"Source: {API_SOURCE}")
