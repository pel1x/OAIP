from sort import sort_tuples

def main():
    tuples_list = [("apple", 3, "banana"), ("cherry", 2, "banana"), ("date", 1, "apple"), ("elderberry", 5, "banana"), ("fig", 2, "apple")]
    sorted_list = sort_tuples(tuples_list)
    print(sorted_list)

    

if __name__ == '__main__':
    main()