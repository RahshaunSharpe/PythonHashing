# PythonHashing
python scripts for identifying and cracking hashes 

# Id Hash Type

  # Must have Python3 installed 
    Usage: python3 ./hashid.py 
  # Script Will prompt you to Inter a hash or a file containting multiple hashes
    Enter a single hash value or the path to a file containing hashes: 

  # If file is in current local directory then you can just call file such as:
    Enter a single hash value or the path to a file containing hashes: hash.txt

    Results from file:
      5eb63bbbe01eeed093cb22bb8f5acdc3: MD5 (Hash) MD5
      $BLAKE2$296c269e70ac5f0095e6fb47693480f0f7b97ccd0307f5c3bfa4df8f5ca5c9308a0e7108e80a0a9c0ebb715e8b7109b072046c6cd5e155b4cfd2f27216283b1e: BLAKE2b (Hash) BLAKE2b        
      127e6fbfe24a750e72930c220a8e138275656b8e5d8f48a98c3c92df2caba935: SHA256 (Hash) SHA256
      $2a$05$LhayLxezLhK1LhWvKxCyLOj0j1u.Kj0jZ0pEmm134uzrQlFvQJLF6: Not a hash
