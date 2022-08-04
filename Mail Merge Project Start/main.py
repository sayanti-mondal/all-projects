# #TODO: Create a letter using starting_letter.txt
letter_list = []
with open("./Input/Letters/starting_letter.txt") as starting_letter:
     contents = starting_letter.read()
     with open("./Input/Names/invited_names.txt") as invited_names:
     # Replace the [name] placeholder with the actual name.
         for invitee in invited_names:
             for name in invitee.split():
                #print(contents)
                 new_content = contents.replace('[name]', name)
                 #print(new_content)
                 letter_list.append(new_content)

#for letter in letter_list:
with open("./Output/ReadyToSend/1st_letter", 'w') as letter1:
    letter1.write(letter_list[0])

with open("./Output/ReadyToSend/2nd_letter", 'w') as letter2:
    letter2.write(letter_list[1])

#
#
# text = 'Dear [name],'
# x = text.replace('[name]', 'A')
# print(x)


    #print(starting_letter)

    #print(starting_letter.readline())
    #print(contents)


#
#
#
#


#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp