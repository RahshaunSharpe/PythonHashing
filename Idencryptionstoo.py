import base64
import binascii
import os
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives.serialization import load_der_private_key, load_der_public_key
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec

def identify_input(input_value):
    # Check if the input is a base64-encoded string
    try:
        decoded_bytes = base64.b64decode(input_value)
        decoded_text = decoded_bytes.decode('utf-8')
        return "Base64", "Not a hash (Base64 encoded)"
    except:
        pass

    # Check if the input is a hexadecimal string
    try:
        decoded_bytes = bytes.fromhex(input_value)
        return "Hexadecimal", "Not a hash (Hexadecimal encoded)"
    except:
        pass

    # Check if the input is a valid ASCII-armored format (e.g., PGP keys)
    if input_value.startswith("-----BEGIN ") and input_value.endswith("-----"):
        return "ASCII-armored", "Not a hash (ASCII-armored)"

    # Add more encoding or encryption checks here...

    return "Unknown", "Not a hash"

def identify_encryption(input_value):
    # Check if the input is a PEM-encoded private key
    try:
        load_pem_private_key(input_value.encode(), password=None)
        return "PEM Private Key", "Not a hash (PEM-encoded private key)"
    except:
        pass

    # Check if the input is a PEM-encoded public key
    try:
        load_pem_public_key(input_value.encode())
        return "PEM Public Key", "Not a hash (PEM-encoded public key)"
    except:
        pass

    # Check if the input is a DER-encoded private key
    try:
        load_der_private_key(input_value.encode(), password=None)
        return "DER Private Key", "Not a hash (DER-encoded private key)"
    except:
        pass

    # Check if the input is a DER-encoded public key
    try:
        load_der_public_key(input_value.encode())
        return "DER Public Key", "Not a hash (DER-encoded public key)"
    except:
        pass

    # Add more encryption checks here...

    return "Unknown", "Not an encryption key"

def identify_hashes_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            hash_value = line.strip()

            # Identify input type
            input_type, input_info = identify_input(hash_value)

            # Identify encryption type
            encryption_type, encryption_info = identify_encryption(hash_value)

            print(f"{hash_value}: Input Type: {input_type} ({input_info}), Encryption Type: {encryption_type} ({encryption_info})")

def main():
    user_input = input("Enter a single value: ")

    # Identify input type
    input_type, input_info = identify_input(user_input)
    print(f"Input Type: {input_type} ({input_info})")

    # Identify encryption type
    encryption_type, encryption_info = identify_encryption(user_input)
    print(f"Encryption Type: {encryption_type} ({encryption_info})")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()