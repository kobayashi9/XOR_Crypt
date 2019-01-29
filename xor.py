
def encrypt_xor(texts,keys):
    ct = []
    for text, key in zip(texts,keys):
       c = ord(text) ^ ord(key)
       ct.append(chr(c))
    cts = "".join(ct)
    return cts

def decrypt_xor(cipher_text, keys):
    ct = []
    for text, key in zip(cipher_text, keys):
        c = ord(text) ^ ord(key)
        ct.append(chr(c))
    cts = "".join(ct)
    return cts

plaintext = 'sample'
key = '1234'

#padding 
while(len(plaintext) > len(key)):
    key = key + '0'

cipher_text = encrypt_xor(plaintext, key)
dec_text = decrypt_xor(cipher_text, key)


print(cipher_text)

print(dec_text)
