lst = ['yellow', 'red', 'green', 'black', 'brown', 'grey']
first_character = input()
print(list(filter(lambda x : x[0] == first_character, lst)))