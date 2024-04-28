import hashlib
import re
import subprocess
import os
import base64


def identify_hash(hash_value):
    hash_types = {
        # "MD2": r"^[a-fA-F0-9]{32}$",
        # "MD4": r"^[a-fA-F0-9]{32}$",
        "MD5": r"^[a-fA-F0-9]{32}$",
        "SHA1": r"^[a-fA-F0-9]{40}$",
        "SHA224": r"^[a-fA-F0-9]{56}$",
        "SHA256": r"^[a-fA-F0-9]{64}$",
        "SHA384": r"^[a-fA-F0-9]{96}$",
        "SHA512": r"^[a-fA-F0-9]{128}$",
        # "SHA512/224": r"^[a-fA-F0-9]{56}$",
        # "SHA512/256": r"^[a-fA-F0-9]{64}$",
        # "SHA3-512": r"^[a-fA-F0-9]{128}$",
        "BLAKE2b": r"^\$BLAKE2\$[a-zA-Z0-9]+$",
        # "BLAKE2s": r"^[a-fA-F0-9]{64}$",
        "Whirlpool": r"^\$Whirlpool\$[a-fA-F0-9]{128}$",
        "RIPEMD-160": r"^\$RIPEMD160\$[a-fA-F0-9]{40}$",
        # Add more hash types as needed
    }

    # Check if the hash value matches any known hash type
    for hash_type, pattern in hash_types.items():
        if re.match(pattern, hash_value):
            return hash_type, "Hash"

    # Check if the hash value is actually a base64-encoded string
    try:
        decoded_bytes = base64.b64decode(hash_value)
        decoded_text = decoded_bytes.decode('utf-8')
        return "Base64", "Not a hash (Base64 encoded)"
    except:
        pass

    return "Unknown", "Not a hash"



def identify_hashes_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            hash_value = line.strip()
            hash_type, info = identify_hash(hash_value)
            
            if hash_type != "Unknown":
                    # Print hash value and hash type in one line, with hash type in green
                print(f"{hash_value}: {hash_type} ({info})", end=" ")
                print_colored(hash_type, "green")  # Print hash type in green
            else:
                # Print "Not a Hash" in red
                print_colored(f"{hash_value}: {info}", "red")
            
            
def print_colored(text, color):
    colors = {
        "green": "\033[92m",  # Green color code
        "red": "\033[91m",
        # Add more colors if needed
    }
    end_color = "\033[0m"  # Reset color code

    if color in colors:
        print(colors[color] + text + end_color)
    else:
        print(text)
        
        
        

def main():
    user_input = input("Enter a single hash value or the path to a file containing hashes: ")

    if os.path.isfile(user_input):
        identify_hashes_from_file(user_input)
    else:
        hash_type, info = identify_hash(user_input)
      
        if hash_type != "Unknown":
                # Print hash value and hash type in one line, with hash type in green
            print(f"{user_input}: {hash_type} ({info})", end=" ")
            print_colored(hash_type, "green")  # Print hash type in green
        else:
            # Print "Not a Hash" in red
            print_colored(f"{user_input}: {info}", "red")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
