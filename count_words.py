import sys

filename = sys.argv[1]
   
text_file = open(filename)
words_dic = {}

for line in text_file:
    for word in line.lower().split():
        word = word.strip("'?,.;!-/\"")
        if word not in words_dic:
            words_dic[word] = 0
        words_dic[word] = words_dic[word] + 1

text_file.close()

print("List of words in the file with number of times each appears.")
word_list = sorted(words_dic)
for word in word_list:
    print(words_dic[word], word)
