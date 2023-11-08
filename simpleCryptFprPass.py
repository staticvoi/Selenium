import pandas as pd
from seleniumbase import encryption
import time

def main():
        
            print("\nEnter password: ")
            password = input()

            print('Encrypted Password')
            encrypted_password = encryption.decrypt(password)
            print(encrypted_password)
            time.sleep(0.2)
            
            
            print('Decrypted Password')
            depassword = encryption.decrypt(encrypted_password)
            print(depassword)
            time.sleep(0.2)

if __name__ == "__main__":
    main()

