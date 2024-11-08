import hashlib  # Import hashlib module to perform hashing operations

def crackHash(inputHashes):
    """
    Attempt to crack a list of hashes using a dictionary attack.
    The function reads a wordlist file and hashes each word to compare with the target hash.
    """
    print("Starting to crack hash...")

    try:
        # Iterate through each hash in the list of input hashes that need to be cracked
        for inputHash in inputHashes:
            print(f"Cracking hash: {inputHash}")  # Inform the user which hash is being worked on

            # Reopen the wordlist file for each hash to start from the beginning
            with open("wordlist.txt", "r") as passFile:
                print("File opened successfully.")  # Inform the user that the wordlist file was opened

                # Read through each word in the wordlist file one by one
                for password in passFile:
                    password = password.strip()  # Remove any extra whitespace or newline characters from the word

                    # Print the current password being tested for debugging purposes
                    print(f"Testing password: {password}")

                    # Hash the current password using MD5 (you can replace md5 with other algorithms like sha1 or sha256)
                    encPass = password.encode("utf-8")  # Convert the password string into bytes for hashing
                    digest = hashlib.md5(encPass).hexdigest()  # Generate MD5 hash of the password

                    # Print the generated hash for debugging purposes (to see the result of the hash operation)
                    print(f"Generated Hash: {digest}")

                    # Check if the generated hash matches the target hash
                    if digest == inputHash:
                        # If a match is found, print the password and return it
                        print(f"Password Found: {password}")
                        return password  # Return the password if it matches the hash

            # If no match is found for the current hash in the wordlist, print a message
            print(f"Password not found for hash: {inputHash}.")

        # After iterating through all hashes, if none were found, print this message
        print("Password not found in wordlist.")

    except FileNotFoundError:
        # Handle the case where the wordlist file does not exist
        print("Error: 'wordlist.txt' not found.")
    except Exception as e:
        # General error handling for any other exceptions
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    """
    Main function to set up the hashes and initiate the cracking process.
    This part defines the hashes to crack and calls the crackHash function to attempt to find the passwords.
    """
    # List of target MD5 hashes (the hashes for "password" and "cat" in this example)
    target_hashes = [
        "5f4dcc3b5aa765d61d8327deb882cf99",  # MD5 hash of the word "password"
        "742e5e7c8cb7b3f36d0bc0b600b5c020"   # MD5 hash of the word "cat"
    ]
    
    # Call the crackHash function with the list of target hashes
    crackHash(target_hashes)
