import hashlib

def hash_file(input_file, algorithm="sha256"):
    with open(input_file, "rb") as f:
        data = f.read()
    if algorithm == "sha256":
        h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()
