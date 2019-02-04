
def enc_decrypt_xor(texts,keys):
    ct = []
    for text, key in zip(texts,keys):
       c = ord(text) ^ ord(key)
       ct.append(chr(c))
    cts = "".join(ct)
    return cts

plaintext = 'sample'
key = '1234'

#padding 
while(len(plaintext) > len(key)):
    key = key + '0'

cipher_text = enc_decrypt_xor(plaintext, key)
dec_text = enc_decrypt_xor(cipher_text, key)


print(cipher_text)

print(dec_text)
