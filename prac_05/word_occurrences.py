user_string = str(input("Enter string: "))
user_list = user_string.split()
dict = {}

for word in user_list:
    word_count = user_list.count(word)
    dict[word] = word_count

word_count_list = []
for key in dict:
    word_count_list.append([key, dict[key]])
word_count_list.sort()

largest_word = max(user_list, key=len)
print(largest_word)
largest_word_length = len(largest_word)
print(largest_word_length)

for element in word_count_list:
    print("{:{}} : {}".format(element[0], largest_word_length, element[1]))