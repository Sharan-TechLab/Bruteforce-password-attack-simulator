import time
import os
import hashlib
import sys

correct_password = "admin123"
max_attempts = 5
attempts = 0
file_path = r"D:\Project\Bruteforce password attack simulator\password.txt"

# Hash the correct password
correct_hash = hashlib.sha256(correct_password.encode()).hexdigest()

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "password.txt")

try:
    with open(file_path, "r") as file:
        for line in file:
            password = line.strip()
            attempts += 1

            print(f"Attempt {attempts}: Trying -> {password}")
            time.sleep(1)  #  Delay to slow brute force

            password_hash = hashlib.sha256(password.encode()).hexdigest()

            if password_hash == correct_hash:
                print("\n Password cracked successfully!")
                print("Total attempts:", attempts)
                break

            if attempts == max_attempts:
                print("\n Account locked due to too many attempts")
                break
except FileNotFoundError:
    print(f"Password file not found: {file_path}")
    print("Files in directory:", os.listdir(base_dir))
    sys.exit(1)
