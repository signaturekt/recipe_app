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
    # catagories = Request.get_categories()
    categories = Request.get_catagories()
    for category in categories:
        print(category)
    print(s)

def main_menu():
    while(True):
        print_main_menu()
        option = int(input('Enter your choice: '))
        if option == 1:
            print("1")
            opt1()
        elif option == 2:
            print("2 - List all Meals by Category")
        else:
            break


if __name__ == '__main__':
    sys.exit(main_menu())