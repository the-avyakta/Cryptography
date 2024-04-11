#Encryption
text=input("Enter the String to encrypt")
key=1
data=[chr(ord(i)+key) for i in text]
print(''.join(data))


#Decryption
text=input("Enter the String to encrypt")
key=1
data=[chr(ord(i)-key) for i in text]
print(''.join(data))