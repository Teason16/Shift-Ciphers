text = "Hello World" 
shift = 3

def caesarCipher(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for char in message.lower():
        # append non-alpha characters without modification
        if not char.isalpha():
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('Plan Text:', message, '\nEncrypted Text:', encrypted_text)

caesarCipher("Winnies Big Adventure", 5)

