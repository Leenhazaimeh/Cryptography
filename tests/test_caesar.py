from caesar_cipher.caesar_cipher import crack,encrypt,decrypt

def test_encrypt():
    word = 'nope10'
    k = 5
    actual = encrypt(word,5)
    expected = 'stuj65'
    assert actual == expected

def test_decrypt():
    word = 'mffo'
    k = 5
    actual = decrypt(word,5)
    expected = 'leen'
    assert actual != expected


def test_crack():
    word = 'mffo'
    actual = crack(word)
    expected = 'leen'
    assert actual != expected