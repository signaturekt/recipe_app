def print

#import request
def opt1():
    s = '-'*30
    print("{}\nList all categories\n{}".format(s,s))
    # catagories = Request.get_categories()
    categories = get_catagories()
    for categories