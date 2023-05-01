def caesar_cipher(text, key, encrypt=True):
    result = ""
    shift = key if encrypt else -key

    for char in text:
        if char.isalpha():  # when char == alphabet
            key_amount = shift % 26  # when key > 26
            new_char_code = ord(char) + key_amount

            if char.islower():  # when char == lowercase                
                if new_char_code > ord('z'):  # ord(char) → num
                    new_char_code -= 26  # for in range of alphabets
                    
                elif new_char_code < ord('a'):
                    new_char_code += 26
                    
                    
            else:  # when char == uppercase                
                if new_char_code > ord('Z'):
                    new_char_code -= 26
                    
                elif new_char_code < ord('A'):
                    new_char_code += 26

            result += chr(new_char_code)
            
            
        else:  # when char == space
            result += char

    return result


text = "Caesar salad"
key = 4


encrypted_text = caesar_cipher(text, key, encrypt=True)
print("Encrypted text:", encrypted_text)


decrypted_text = caesar_cipher(encrypted_text, key, encrypt=False)
print("Decrypted text:", decrypted_text)