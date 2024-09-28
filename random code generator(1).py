import random
import string


symbols = string.ascii_letters

numbers = string.digits

punctations = string.punctuation


code = ""

for _ in range (8):
    
    rd_code=random.choice(symbols + numbers + punctations)
    
    code+=rd_code

print(code)
