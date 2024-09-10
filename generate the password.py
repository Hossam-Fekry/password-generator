import random
import string

def generate_random_string(length): 
    # Define the characters to choose from (letters, digits, and punctuation)
    all_chars = string.ascii_letters + string.digits + string.punctuation
    # Generate a random string
    random_string = ''.join(random.choice(all_chars) for _ in range(length))
    return random_string

# Generate a random string of length 8
random_text = generate_random_string(8)
print(f"Random text: {random_text}")
