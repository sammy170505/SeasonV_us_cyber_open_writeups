# oracle.py
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

BLOCK_SIZE = 16
FLAG_PATH = "./flag.txt"

with open(FLAG_PATH, "rb") as f:
    FLAG = f.read().strip()

KEY = os.urandom(16)

def encrypt_oracle(user_bytes: bytes) -> bytes:
    plaintext = user_bytes + FLAG
    padded = pad(plaintext, BLOCK_SIZE)
    cipher = AES.new(KEY, AES.MODE_ECB)
    return cipher.encrypt(padded)
