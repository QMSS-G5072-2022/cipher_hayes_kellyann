from cipher_kh3117 import cipher_kh3117
import pytest


@pytest.mark.parametrize("text, shift",
    [('cat', 1),
     ('cat', 2),
     ('cat', 3),
     ('Dog', 4),
     ('Dog', 5),
     ('Mouse', 6),
     ('Mouse', 7),
     ('RAT', 8),
     ('Rat', 9),
     ('Snake', 10)])

def test_encrypt(text, shift):
    result_encrypt = cipher_kh3117.cipher(text, shift)
    result_decrypt = cipher_kh3117.cipher(result_encrypt, shift, encrypt=False)
    assert result_decrypt == text
    