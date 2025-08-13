from digital_locker import DigitalLocker

def test_digital_locker():
    print("=== Testing Digital Locker ===")
    
    # Create locker instance
    locker = DigitalLocker()
    
    # Test user registration
    print("\n1. Testing user registration...")
    success, message = locker.register_user("testuser", "1234")
    print(f"Registration: {message}")
    
    # Test login
    print("\n2. Testing login...")
    if locker.login("testuser", "1234"):
        print("Login successful!")
    else:
        print("Login failed!")
    
    # Test storing a file
    print("\n3. Testing file storage...")
    success, message = locker.store_file("secret.txt", "This is my secret message!")
    print(f"Store file: {message}")
    
    # Test listing files
    print("\n4. Testing file listing...")
    files = locker.list_files()
    print(f"Files in locker: {files}")
    
    # Test retrieving a file
    print("\n5. Testing file retrieval...")
    success, content = locker.retrieve_file("secret.txt")
    if success:
        print(f"Retrieved content: {content}")
    else:
        print(f"Error: {content}")
    
    # Test storing another file
    print("\n6. Testing multiple files...")
    locker.store_file("notes.txt", "My important notes")
    files = locker.list_files()
    print(f"All files: {files}")
    
    # Test deleting a file
    print("\n7. Testing file deletion...")
    success, message = locker.delete_file("notes.txt")
    print(f"Delete file: {message}")
    files = locker.list_files()
    print(f"Remaining files: {files}")
    
    print("\n=== Test Complete ===")

if __name__ == "__main__":
    test_digital_locker()