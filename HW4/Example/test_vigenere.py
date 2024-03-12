from vigenere_cipher import VigenereCipher
from unittest.mock import patch, Mock
import pytest

@pytest.fixture()
def train_cipher():
    return VigenereCipher("TRAIN")

def test_init(train_cipher):
    assert hasattr(train_cipher, "keyword")
    assert train_cipher.keyword == "TRAIN"

def test_encode(train_cipher):
    encoded = train_cipher.encode("ENCODEDINPYTHON")
    assert encoded == "XECWQXUIVCRKHWA"

def test_decode(train_cipher):
    decoded = train_cipher.decode("XECWQXUIVCRKHWA")
    assert decoded == "ENCODEDINPYTHON"

def test_encode_character(train_cipher):
    encoded = train_cipher.encode("E")
    assert encoded == "X"

def test_encode_spaces(train_cipher):
    encoded = train_cipher.encode("ENCODED IN PYTHON") 
    assert encoded == "XECWQXUIVCRKHWA"

def test_encode_lowercase():
    cipher = VigenereCipher("TRain")
    encoded = cipher.encode("encodedinPython")
    assert encoded == "XECWQXUIVCRKHWA"

def test_extend_keyword(train_cipher):
    extended = train_cipher._extend_keyword(16)
    assert extended == "TRAINTRAINTRAINT"
    extended = train_cipher._extend_keyword(15)
    assert extended == "TRAINTRAINTRAIN"
    single_letter_cipher = VigenereCipher("H")
    extended = single_letter_cipher._extend_keyword(15)
    assert extended == "H"*15

def test_rotate_right():
    assert VigenereCipher._rotate("E", "T", 1) == "X"
    assert VigenereCipher._rotate("N", "R", 1) == "E"

def test_rotate_left():
    assert VigenereCipher._rotate("X", "T", -1) == "E"
    assert VigenereCipher._rotate("E", "R", -1) == "N"

def test_code_mocked(train_cipher): 
    with patch.object(train_cipher, "_extend_keyword") as extend:
        with patch.object(train_cipher, "_rotate") as rotate:
            extend.return_value = "TRA"
            rotate.return_value = "/ join_test /"
            assert train_cipher._code("ENC", 1) == "/ join_test // join_test // join_test /"
            extend.assert_called_once_with(len("ENC"))
            rotate.assert_any_call("E", "T", 1)
            rotate.assert_any_call("N", "R", 1)
            rotate.assert_called_with("C", "A", 1)


