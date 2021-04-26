#   Declare a set to store five colours of your choice. Add Python program to add member(s) in a set.
#   Use iterator to display the contents of the set.

colors = ('yellow', 'blue', 'green', 'orange', 'black')


#   FUNCTION WILL TAKE IN A SET AND UPDATE IT
def update_set(set_to_update, new_value):
    #   CONVERT THE set_to_update TO A LIST
    set_list = list(set_to_update)
    #   ADD THE new_value TO THE set_list
    set_list.append(new_value)

    #   LOOP THROUGH THE set_list AND PRINT ITS CONTENTS
    for i in set_list:
        print(i)

    #   RETURN THE UPDATED SET
    return set(set_list)


update_set(colors, 'white')
