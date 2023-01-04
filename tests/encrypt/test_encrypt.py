from challenges.challenge_encrypt_message import encrypt_message
import pytest

def test_encrypt_message():
    invalid_key1 = encrypt_message("ABCD", 20)
    assert invalid_key1 == "DCBA"

    invalid_key2 = encrypt_message("ABBCCA", 4)
    assert invalid_key2 == "AC_CBBA"

    invalid_key3 = encrypt_message("ABCD", 2)
    assert invalid_key3 == "DC_BA"

    with pytest.raises(TypeError):
        encrypt_message("AABBCC", None)
    
    with pytest.raises(TypeError):
        encrypt_message(None, 3)
