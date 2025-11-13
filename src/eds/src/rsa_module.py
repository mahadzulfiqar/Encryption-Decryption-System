from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_keys(private_file, public_file):
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    with open(private_file, "wb") as f:
        f.write(private_key)
    with open(public_file, "wb") as f:
        f.write(public_key)

def encrypt_file(input_file, public_key_file, output_file):
    with open(input_file, "rb") as f:
        data = f.read()
    with open(public_key_file, "rb") as f:
        key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(data)
    with open(output_file, "wb") as f:
        f.write(ciphertext)

def decrypt_file(input_file, private_key_file, output_file):
    with open(input_file, "rb") as f:
        ciphertext = f.read()
    with open(private_key_file, "rb") as f:
        key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(key)
    data = cipher.decrypt(ciphertext)
    with open(output_file, "wb") as f:
        f.write(data)
