import os
import json
import hashlib
from cryptography.fernet import Fernet
from getpass import getpass

class DigitalLocker:
    def __init__(self):
        self.locker_dir = "locker_data"
        self.users_file = os.path.join(self.locker_dir, "users.json")
        self.current_user = None
        self.setup_directories()
    
    def setup_directories(self):
        if not os.path.exists(self.locker_dir):
            os.makedirs(self.locker_dir)
    
    def hash_pin(self, pin):
        return hashlib.sha256(pin.encode()).hexdigest()
    
    def generate_key(self, pin):
        return Fernet.generate_key()
    
    def load_users(self):
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save_users(self, users):
        with open(self.users_file, 'w') as f:
            json.dump(users, f)
    
    def register_user(self, username, pin):
        users = self.load_users()
        if username in users:
            return False, "User already exists"
        
        key = self.generate_key(pin)
        users[username] = {
            "pin_hash": self.hash_pin(pin),
            "key": key.decode()
        }
        self.save_users(users)
        
        user_dir = os.path.join(self.locker_dir, username)
        os.makedirs(user_dir, exist_ok=True)
        return True, "User registered successfully"
    
    def authenticate(self, username, pin):
        users = self.load_users()
        if username not in users:
            return False
        
        return users[username]["pin_hash"] == self.hash_pin(pin)
    
    def login(self, username, pin):
        if self.authenticate(username, pin):
            self.current_user = username
            return True
        return False
    
    def get_user_key(self):
        users = self.load_users()
        return Fernet(users[self.current_user]["key"].encode())
    
    def store_file(self, filename, content):
        if not self.current_user:
            return False, "Not logged in"
        
        fernet = self.get_user_key()
        encrypted_content = fernet.encrypt(content.encode())
        
        user_dir = os.path.join(self.locker_dir, self.current_user)
        file_path = os.path.join(user_dir, filename)
        
        with open(file_path, 'wb') as f:
            f.write(encrypted_content)
        
        return True, f"File '{filename}' stored successfully"
    
    def retrieve_file(self, filename):
        if not self.current_user:
            return False, "Not logged in"
        
        user_dir = os.path.join(self.locker_dir, self.current_user)
        file_path = os.path.join(user_dir, filename)
        
        if not os.path.exists(file_path):
            return False, "File not found"
        
        fernet = self.get_user_key()
        with open(file_path, 'rb') as f:
            encrypted_content = f.read()
        
        try:
            decrypted_content = fernet.decrypt(encrypted_content)
            return True, decrypted_content.decode()
        except:
            return False, "Failed to decrypt file"
    
    def list_files(self):
        if not self.current_user:
            return []
        
        user_dir = os.path.join(self.locker_dir, self.current_user)
        if os.path.exists(user_dir):
            return os.listdir(user_dir)
        return []
    
    def delete_file(self, filename):
        if not self.current_user:
            return False, "Not logged in"
        
        user_dir = os.path.join(self.locker_dir, self.current_user)
        file_path = os.path.join(user_dir, filename)
        
        if os.path.exists(file_path):
            os.remove(file_path)
            return True, f"File '{filename}' deleted successfully"
        return False, "File not found"

def main():
    locker = DigitalLocker()
    
    while True:
        if not locker.current_user:
            print("\n=== Digital Locker ===")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            
            choice = input("Choose option: ").strip()
            
            if choice == "1":
                username = input("Username: ").strip()
                pin = getpass("PIN: ")
                success, message = locker.register_user(username, pin)
                print(message)
            
            elif choice == "2":
                username = input("Username: ").strip()
                pin = getpass("PIN: ")
                if locker.login(username, pin):
                    print(f"Welcome, {username}!")
                else:
                    print("Invalid credentials")
            
            elif choice == "3":
                break
        
        else:
            print(f"\n=== Locker - {locker.current_user} ===")
            print("1. Store file")
            print("2. Retrieve file")
            print("3. List files")
            print("4. Delete file")
            print("5. Logout")
            
            choice = input("Choose option: ").strip()
            
            if choice == "1":
                filename = input("Filename: ").strip()
                content = input("Content: ")
                success, message = locker.store_file(filename, content)
                print(message)
            
            elif choice == "2":
                filename = input("Filename: ").strip()
                success, content = locker.retrieve_file(filename)
                if success:
                    print(f"Content: {content}")
                else:
                    print(content)
            
            elif choice == "3":
                files = locker.list_files()
                if files:
                    print("Files:", ", ".join(files))
                else:
                    print("No files found")
            
            elif choice == "4":
                filename = input("Filename: ").strip()
                success, message = locker.delete_file(filename)
                print(message)
            
            elif choice == "5":
                locker.current_user = None
                print("Logged out")

if __name__ == "__main__":
    main()