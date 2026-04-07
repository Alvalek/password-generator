import random
import string
def generate_password(size=12):
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ".join(random.choice(characters) for_in
range(size))
    return password

print("Password generated:", generate_password())
