import random
import string

def generate_random_username(length=8):
    """Generate a fun random username with numbers and letters."""
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def check_username_availability(username):
    """Simulate checking if a username is available (always returns True for fun)."""
    return True

# Generate and check 5 random usernames
print("🎲 Random Username Generator")
print("-" * 30)
for i in range(5):
    username = generate_random_username()
    available = check_username_availability(username)
    status = "✅ Available" if available else "❌ Taken"
    print(f"{i+1}. @{username} - {status}")
