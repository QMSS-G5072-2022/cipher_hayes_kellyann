def cipher(text, shift, encrypt=True):
    """
    
    Encrypts and decrypts strings based on Caesar's Cipher technique. 
    
    Parameters
    ----------
    text : String
        The string of text that is to be encrypted or decrypted. 
        Can include spaces and non-alphabet symbols.
    shift : Integer, positive or negative
        Chosen amount of spaces letters in string will shift during en/decryption
    encrypt : Boolean, optional
        DESCRIPTION. The default is True, which will encrypt; False will decrpyt

    Returns
    -------
    new_text : String
        Encrypted or decrypted result.

    Examples
    --------
    Encryption: 
    >>> from cipher_kh3117 import cipher_kh3117
    >>> text = "Cat"
    >>> shift = 2
    >>> encrypt = True
    >>> cipher_kh3117.cipher(text, shift, encrypt)
    "Ecv"
    
    Decryption:
    >>> from cipher_kh3117 import cipher_kh3117
    >>> text = "Ecv"
    >>> shift = 2
    >>> encrypt = False
    >>> cipher_kh3117.cipher(text, shift, encrypt)
    "Cat"
        
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text