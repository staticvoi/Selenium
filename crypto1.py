from cryptography.fernet import Fernet
key = Fernet.generate_key()
# opening the key
with open('filekey.key', 'rb') as filekey:
	key = filekey.read()

# using the generated key
fernet = Fernet(key)

# opening the original file to encrypt
with open('msg1.txt', 'rb') as file:
	original = file.read()
	
# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
with open('msg2.txt', 'wb') as encrypted_file:
	encrypted_file.write(encrypted)

