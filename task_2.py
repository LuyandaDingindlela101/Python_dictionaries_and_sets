#   Write a function to convert a number entered by the user into its corresponding number in words.
#   For example, if the input is 145 then the output should be ‘One Four Five.


#   FUNCTION TO CONVERT NUMBERS TO WORDS
def number_to_word(numbers):
    numbers = str(numbers)
    #   STRING TO CONTAIN THE CONVERTED NUMBER
    result = ''
    #   LIST TO HOLD THE WORD FORM OF THE NUMBERS
    numbers_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    #   LOOP THROUGH THE GIVEN numbers
    for number in numbers:
        #   TAKE result AND APPEND THE WORD AT THE SAME INDEX AS THE CURRENT number
        result = result + ' ' + numbers_list[int(number)]

    #   RETURN THE result
    return result


print(number_to_word(789))
