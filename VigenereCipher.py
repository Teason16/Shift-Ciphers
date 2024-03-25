def vigenereCipher(message, key, direction):
    key_index = 0
    encrypted_text = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in message.lower():
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return encrypted_text

encryption = vigenereCipher('Welcome to python', 'python', 1)
decryption = vigenereCipher(encryption, 'python', -1)
print(f'{encryption} \n{decryption}')
