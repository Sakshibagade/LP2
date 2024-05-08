from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def encrypt(plain_texot, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plain_text = plain_text + ' ' * (8 - len(plain_text) % 8)  # Pad the plaintext if needed
    return cipher.encrypt(padded_plain_text.encode())

def decrypt(cipher_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(cipher_text).decode()
    return decrypted_text.rstrip()  # Remove padding

# Example usage:
plain_text = "Hello, DES!"
key = get_random_bytes(8)  # DES key size is 8 bytes
cipher_text = encrypt(plain_text, key)
print("Encrypted:", cipher_text.hex())
decrypted_text = decrypt(cipher_text, key)
print("Decrypted:", decrypted_text)
