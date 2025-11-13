from eds.aes_module import encrypt_file, decrypt_file

def test_aes_functions_exist():
    assert callable(encrypt_file)
    assert callable(decrypt_file)
