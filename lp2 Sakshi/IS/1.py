#Write a Java/C/C++/Python program to perform encryption and decryption using the method of Transposition technique




def encrypt(message, key):
    # Remove spaces from the message
    message = message.replace(" ", "")
    # Calculate the number of columns needed
    num_columns = len(message) // key + int(len(message) % key != 0)
    # Create a matrix to hold the message
    matrix = [''] * key
    for i in range(key):
        matrix[i] = [''] * num_columns
    # Fill the matrix with the message characters
    index = 0
    for col in range(num_columns):
        for row in range(key):
            if index < len(message):
                matrix[row][col] = message[index]
                index += 1
            else:
                break
    # Construct the encrypted text
    encrypted_text = ''
    for row in range(key):
        encrypted_text += ''.join(matrix[row])
    return encrypted_text

def decrypt(encrypted_text, key):
    # Calculate the number of columns needed
    num_columns = len(encrypted_text) // key + int(len(encrypted_text) % key != 0)
    # Create a matrix to hold the encrypted text
    matrix = [''] * key
    for i in range(key):
        matrix[i] = [''] * num_columns
    # Fill the matrix with the encrypted text characters
    index = 0
    for row in range(key):
        for col in range(num_columns):
            matrix[row][col] = encrypted_text[index]
            index += 1
            if index >= len(encrypted_text):
                break
    # Construct the decrypted message
    decrypted_message = ''
    for col in range(num_columns):
        for row in range(key):
            decrypted_message += matrix[row][col]
    return decrypted_message

# Example usage:
message = "Hello, World!"
key = 4
encrypted_text = encrypt(message, key)
print("Encrypted:", encrypted_text)
decrypted_message = decrypt(encrypted_text, key)
print("Decrypted:", decrypted_message)