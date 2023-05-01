def caesar_cipher(text, key, encrypt=True):
    result = ""
    shift = key if encrypt else -key

    for char in text:
        if char.isalpha():  
            key_amount = shift % 26  
            new_char_code = ord(char) + key_amount

            if char.islower():   
                if new_char_code > ord('z'):  
                    new_char_code -= 26  
                    
                elif new_char_code < ord('a'):
                    new_char_code += 26
                    
                    
            else:  
                if new_char_code > ord('Z'):
                    new_char_code -= 26
                    
                elif new_char_code < ord('A'):
                    new_char_code += 26

            result += chr(new_char_code)
            
            
        else:  
            result += char

    return result