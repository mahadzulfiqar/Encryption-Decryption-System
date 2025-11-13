from eds.hashing_module import hash_file

def test_hashing_function_exists():
    assert callable(hash_file)
