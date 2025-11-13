from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_file(input_file, key_file, output_file):
    with open(input_file, "rb") as f:
        data = f.read()
    key = get_random_bytes(16)  # 128-bit key
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    with open(output_file, "wb") as f:
        f.write(cipher.iv + ct_bytes)
    with open(key_file, "wb") as f:
        f.write(key)

def decrypt_file(input_file, key_file, output_file):
    with open(input_file, "rb") as f:
        iv_ct = f.read()
    with open(key_file, "rb") as f:
        key = f.read()
    iv = iv_ct[:16]
    ct = iv_ct[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    with open(output_file, "wb") as f:
        f.write(pt)
