word_list = []

for i in range(5):
    user_input = input('Enter a word: ')
    word_list.append(user_input)
print('Words: ',word_list)

for j in range(5):
    print(word_list[j], end=" ")

