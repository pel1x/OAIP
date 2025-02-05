from sort import sort_tuples
from stars import stars

def main():
    tuples_list = [("apple", 3, "banana"), ("cherry", 2, "banana"), ("date", 1, "apple"), ("elderberry", 5, "banana"), ("fig", 2, "apple")]
    sorted_list = sort_tuples(tuples_list)
    print(sorted_list)
    print()
    string = input("Введите строку слов разделённых пробелами: ")
    padded_words = stars(string)
    for word in padded_words:
        print(word)
    print()
    

if __name__ == '__main__':
    main()