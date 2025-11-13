# Encryption & Decryption System 🔐

A Python CLI/GUI-based system to securely encrypt and decrypt data using **AES**, **RSA**, and hashing algorithms.  
Designed for educational purposes, secure storage, and practicing cryptography concepts.

---

## 🔍 Overview

This project provides:

- AES (Advanced Encryption Standard) for symmetric encryption
- RSA (Rivest-Shamir-Adleman) for asymmetric encryption
- SHA-256 hashing for integrity verification
- CLI interface for encrypting/decrypting files or strings

> ⚠️ Use responsibly. This system is for educational and personal projects only.

---

## 🛠 Features

- AES encryption/decryption (CBC mode)
- RSA key generation and encryption/decryption
- SHA-256 hashing
- Easy-to-use CLI
- Cross-platform (Windows/Linux/macOS)

---

## 📁 Repository Structure

encryption-system/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── examples/
│ └── sample_input.txt
├── src/
│ └── eds/
│ ├── init.py
│ ├── cli.py
│ ├── aes_module.py
│ ├── rsa_module.py
│ ├── hashing_module.py
│ └── utils.py
└── tests/
├── test_aes.py
├── test_rsa.py
└── test_hashing.py

yaml
Copy code

---

## ⚡ Installation

```bash
git clone https://github.com/<your-username>/encryption-system.git
cd encryption-system
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
🚀 Usage
bash
Copy code
# AES
python -m src.eds.cli aes encrypt --input examples/sample_input.txt --key-file keys/aes.key --output encrypted_file.enc
python -m src.eds.cli aes decrypt --input encrypted_file.enc --key-file keys/aes.key --output decrypted.txt

# RSA
python -m src.eds.cli rsa generate-keys --private keys/private.pem --public keys/public.pem
python -m src.eds.cli rsa encrypt --input examples/sample_input.txt --public-key keys/public.pem --output encrypted_rsa.enc
python -m src.eds.cli rsa decrypt --input encrypted_rsa.enc --private-key keys/private.pem --output decrypted_rsa.txt

# Hashing
python -m src.eds.cli hash --input examples/sample_input.txt --algorithm sha256


🧪 Testing

bash
Copy code
pytest -q
ruff check src tests\

🤝 Contributing

Fork the repository and create a feature branch: feature/<your-feature>
Write tests for your changes.
Follow conventional commits: feat:, fix:, docs:, chore:.
Open a pull request with a description.

📜 License
MIT License — see LICENSE file.

📞 Contact
Created by Mahad Zulfiqar. Open an issue for support or questions.
