from cryptography.fernet import Fernet
import base64
import hashlib
import argparse

parser = argparse.ArgumentParser(description="Decrypt a file using Fernet encryption")
parser.add_argument('--file', required=True, help="Input file to decrypt")
args = parser.parse_args()

user_defined_password = # No Chance

# Use the same salt value as in the encryption script
salt = b'salt_value'

# Derive the key using PBKDF2-HMAC-SHA256
key = hashlib.pbkdf2_hmac('sha256', user_defined_password.encode(), salt, 100000)

# Create a Fernet cipher suite using the derived key
cipher_suite = Fernet(base64.urlsafe_b64encode(key))

file_to_decrypt = args.file
with open(file_to_decrypt, 'rb') as file:
    encrypted_data = file.read()

# Decrypt the encrypted data
decrypted_data = cipher_suite.decrypt(encrypted_data)

# Extract the original file name from the encrypted file name
original_file_name = file_to_decrypt[:-len(".cryptomesh")]

output_file = original_file_name + "_decrypted.txt"

with open(output_file, 'wb') as file:
    file.write(decrypted_data)

print(f"File '{file_to_decrypt}' has been decrypted and saved as '{output_file}'.")

