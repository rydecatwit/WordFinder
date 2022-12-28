def find_words(letters):
    result = []

    #convert our word to a set of letters
    let_set=set(letters)

    #goes through each word in our dictionary
    for word in open('res/dictionary.txt'):
        #trim and hyphons, apostrophes, etc
        trimmed = ''.join(filter(str.isalnum, word))
        if all(x in let_set for x in set(trimmed.strip())):
            result.append(word.strip())

    return result


def main():
    letters = input('Enter you characters as a single string: ')
    print(letters)

    list_of_possible_words = find_words(letters)
    print(list_of_possible_words)
    print('End of program')

if __name__ == '__main__':
    main()