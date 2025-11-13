#!/usr/bin/env python3
import argparse
from eds import aes_module, rsa_module, hashing_module

def main():
    parser = argparse.ArgumentParser(description="Encryption & Decryption System")
    subparsers = parser.add_subparsers(dest="command")

    # AES commands
    aes_parser = subparsers.add_parser("aes")
    aes_parser.add_argument("action", choices=["encrypt","decrypt"])
    aes_parser.add_argument("--input", required=True)
    aes_parser.add_argument("--key-file", required=True)
    aes_parser.add_argument("--output", required=True)

    # RSA commands
    rsa_parser = subparsers.add_parser("rsa")
    rsa_parser.add_argument("action", choices=["generate-keys","encrypt","decrypt"])
    rsa_parser.add_argument("--input")
    rsa_parser.add_argument("--public-key")
    rsa_parser.add_argument("--private-key")
    rsa_parser.add_argument("--output")

    # Hash commands
    hash_parser = subparsers.add_parser("hash")
    hash_parser.add_argument("--input", required=True)
    hash_parser.add_argument("--algorithm", choices=["sha256"], default="sha256")

    args = parser.parse_args()
    print("CLI is ready. Modules will be called here.")  # Placeholder

if __name__ == "__main__":
    main()
