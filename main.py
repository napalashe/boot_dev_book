

with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    print(file_contents)


words = file_contents.split()

word_count = len(words)


print(f'The file length is {word_count}!')


my_word = ''