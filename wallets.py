pip install requests pycryptodome
import os
from bitcoin import *

# Function to create a new temporary wallet
def generate_wallet():
    private_key = random_key() # Generate a random private key
    public_key = privtopub(private_key) # Generate public key
    address = pubtoaddr(public_key) # Generate address based on public key

    return {
        “private_key": private_key,
        “public_key": public_key,
        “address": address
    }

# Generate multiple temporary wallets
def create_temp_wallets(number):
    wallets = []
    For _ in range(number):
        wallet = generate_wallet()
        wallets.append(wallet)
    return wallets

# Saving wallets to a file
def save_wallets(wallets, filename=“wallets.txt”):
    with open(filename, “w”) as file:
        For wallet in wallets:
            file.write(f “Address: {wallet[‘address’]}\n”)
            file.write(f “Private Key: {wallet[‘private_key’]}\n”)
            file.write(f “Public Key: {wallet[‘public_key’]}\n\n”)

# Generate 5 temporary wallets
temp_wallets = create_temp_wallets(5)
save_wallets(temp_wallets)
print(“Wallets created and saved in wallets.txt”)

Translated with www.DeepL.com/Translator (free version)
