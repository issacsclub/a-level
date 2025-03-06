import string
letter = input()

alphabet = string.ascii_lowercase # 'abcdef...xyz'
index = alphabet.find(letter)

# Iterates from index in reverse order in steps of 2
letters_sung = alphabet[index::-2]

print(letters_sung)
        
 



