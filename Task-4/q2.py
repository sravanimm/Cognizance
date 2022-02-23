given_string = input('Enter a string: ')

even_chars = []


for i in range(len(given_string)):
    if i % 2 == 0:
        even_chars.append(given_string[i])
        

print('Even characters: {}'.format(even_chars))
