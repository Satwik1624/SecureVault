from digital_locker import DigitalLocker

def demo_registration():
    print("=== Digital Locker - Registration Demo ===")
    
    locker = DigitalLocker()
    
    # Simulate selecting option 1 (Register)
    print("You selected: 1. Register")
    
    # Demo registration
    username = "alice_smith"
    pin = "5678"
    
    print(f"Username: {username}")
    print(f"PIN: {'*' * len(pin)}")
    
    success, message = locker.register_user(username, pin)
    print(f"\nResult: {message}")
    
    if success:
        print(f"\nUser '{username}' can now login and use the digital locker!")
        
        # Show what happens after registration
        if locker.login(username, pin):
            print(f"[SUCCESS] Login test successful for {username}")
            
            # Store a sample file
            locker.store_file("welcome.txt", "Welcome to your secure digital locker!")
            files = locker.list_files()
            print(f"Files in {username}'s locker: {files}")

if __name__ == "__main__":
    demo_registration()