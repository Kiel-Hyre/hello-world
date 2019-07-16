'''
Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible reconstruction,
return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox',
and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
'''

dict_arr = ['quick','brown','the','fox']
the_string = 'thequickbrownfox'
bank = []

def dc22(dict_arr,the_string):
    while the_string :
        for i in dict_arr :
            if the_string.startswith(i) :
                bank.append(i)
                the_string = the_string[len(i):]

    if bank is None :
        return None
    return bank

print(dc22(dict_arr,the_string))
