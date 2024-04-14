def caesarCipher():

    methodv=int(input("Enter method: 0 for encrption and 1 for decryption: "))  
    method={0: 'Encryption', 1: 'Decryption'}  
    text=input(f"Enter the String to {method[methodv]}: ")
    key=int(input(f"Enter Key for {method[methodv]}: "))  
    if (methodv==0):
        data=[chr(ord(i)+key) for i in text]
        print(''.join(data))
    else:
            data=[chr(ord(i)-key) for i in text]
            print(''.join(data))

quit=input("To Quit Press q and any value to Continue: ")

if(quit!='q'):
    
    caesarCipher()
    quit=input("To Quit Press q and any value to Continue: ")

  