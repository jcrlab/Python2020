def encrypt (text, key):
    ciphertext = ""
    for c in text:
        if 'a' <= c <= 'z':
            ciphertext += chr(ord('a')+((ord(c)-ord('a'))+key)%26)
        elif 'A'<=c<='Z':
            ciphertext += chr(ord('A')+((ord(c)-ord('A'))+key)%26)
        else:
            ciphertext += c
    return ciphertext

text = input()
key = int(input())
ciphertext = encrypt (text, key)
print(ciphertext)

