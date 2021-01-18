if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats']

    # Augmented code, function list_print accepts a list parameter and prints each element with an added comma before each
    # except the last element which has an 'and' instead of the comma.
    def list_print(item):
        for thing in range(len(item)):
            if thing < len(item[:-1]):
                print(item[thing], end=", ")
            else:
                print("and " + item[thing])

    cities = ['New York', 'Chicago', 'Atlanta', 'Burlington', 'Philadelphia', 'Denver']

    # manipulate cities list here

    food = ['carrots', 'mango', 'avocado']

    # manipulate food list here
    list_print(spam)
    list_print(cities)
    list_print(food)