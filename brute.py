
from cryptography.fernet import Fernet
import base64
import hashlib
import argparse

def decrypt_file(file_to_decrypt, user_defined_password):
    salt = b'salt_value'
    key = hashlib.pbkdf2_hmac('sha256', user_defined_password.encode(), salt, 100000)
    cipher_suite = Fernet(base64.urlsafe_b64encode(key))

    with open(file_to_decrypt, 'rb') as file:
        encrypted_data = file.read()

    try:
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        return decrypted_data
    except Exception as e:
        return None

def main():
    parser = argparse.ArgumentParser(description="Decrypt a file using Fernet encryption with multiple passwords")
    parser.add_argument('--file', required=True, help="Input file to decrypt")
    args = parser.parse_args()

    file_to_decrypt = args.file

    with open('combinations.txt', 'r') as combo_file:
        passwords = combo_file.read().splitlines()

    for password in passwords:
        print(f"Trying password: {password}")
        decrypted_data = decrypt_file(file_to_decrypt, password)
        
        if decrypted_data is not None:
            # Extract the original file name from the encrypted file name
            original_file_name = file_to_decrypt[:-len(".cryptomesh")]
            output_file = f"{original_file_name}_decrypted.txt"

            with open(output_file, 'wb') as file:
                file.write(decrypted_data)

            print(f"Success! File '{file_to_decrypt}' decrypted with password '{password}' and saved as '{output_file}'.")
            break
        else:
            print("Failed to decrypt with the current password.")

if __name__ == "__main__":
    main()

