from eds.rsa_module import generate_keys, encrypt_file, decrypt_file

def test_rsa_functions_exist():
    assert callable(generate_keys)
    assert callable(encrypt_file)
    assert callable(decrypt_file)
