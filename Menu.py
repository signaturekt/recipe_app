import Request, sys

def print_main_menu():
    s = '-'*30
    print(s)
    print("Command Menu")
    print(s)
    print('1 - List all Categories')
    print('2 - List all Meals by Category')
    print('3 - Search Meal by Name')
    print('4 - Random Meal')
    print('6 - List all Areas')
    print('7 - List all Meals by Area')
    print('0 - Exit')

#import request
def opt1():
    s = '-'*30
    print("{}\nList all categories\n{}".format(s,s))
    categories = Request.get_categories()
    for category in categories:
        print(category)
    print(s)

def opt2():
    s = '-'*30
    print("{}\nList all meals by categories\n{}".format(s,s))
    categories = Request.get_categories()
    for category in categories:
        print(f"{category.get_name()}:")
        for meal in Request.get_meal_by_category(category):
            print(meal)
    print(s)

def opt3():
    s = '-'*30
    print("{}\nSearch meal by name\n{}".format(s,s))
    while True:
        name = input("What meal would you like to search: ")
        recipe = Request.get_meal_by_name(name)
        if recipe is not None:
            break
    print(recipe)

def opt4():
    s = '-'*30
    print("{}\nSearch a random meal\n{}".format(s,s))
    recipe = Request.get_random_meal()
    print(recipe)

def opt5():
    pass
def opt6():
    pass

def opt7():
    exit()

def main_menu():
    while True:
        print_main_menu()
        option = int(input('Enter your choice: '))
        if option == 1:
            print("1")
            opt1()
        elif option == 2:
            opt2()
        elif option == 3:
            opt3()
        elif option == 4:
            opt4()
        else:
            break

if __name__ == '__main__':
    sys.exit(main_menu())