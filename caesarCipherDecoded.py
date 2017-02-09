#this code deciphers the Caesar Cipher message below (secret value)
alphabet = []
secret = "lbh zhfg hayrnea jung lbh unir yrnearq"
index = 13
real_message = ""

for i in range(26): #this loop produces the alphabet list with ASCII
    letter = chr(i+97) #letter = character represented by ASCII number (97 is a)
    alphabet.append(letter)

alphabet.extend(alphabet) #this line adds the alphabet list to itself

for char in secret:
    if char in alphabet: #checks if value is a letter (vs. punctuation, etc.)
        char_index = alphabet.index(char) + index
        #line 117 finds (first) index for char in the alphabet and then adds
        #13 to it (which is the index for the cipher)
        actual_letter = alphabet[char_index]
        #line 120 takes the char index and converts it to the corresponding
        #letter in the alphabet varialbe (which allows for it to run over into
        #the second alphabet that we appended above)
        real_message += actual_letter #adds actual letter to empty real message
        #string variable above.
    else:
        real_message += char #pushes everything else (non-letter strings) to
        #real_message variable
print real_message
