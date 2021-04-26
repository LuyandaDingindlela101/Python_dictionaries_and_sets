#   Write a program to count the number of times a character appears in a given string.

#   FUNCTION TO CHECK THE APPEARANCE OF A GIVEN LETTER IN A STRING
def check_appearance(letter, word):
    #   appearances WILL HOLD THE AMOUNT OF APPEARANCES
    appearances = 0

    #   LOOP THROUGH THE word
    for i in word:
        if i == letter:
            #   IF THEY MATCH, INCREASE appearances BY 1
            appearances = appearances + 1

    return appearances


print(check_appearance('e', 'everywhere'))
