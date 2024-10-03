import requests, json
import Category

# API base URL
BASE_URL = "https://www.themealdb.com/api/json/v1/1"


def getCategories():
    """
    Get all meal categories from themealdb
    """
    url = f'{BASE_URL}/categories.php'
    r = requests.get(url)
    categories = []

    if r.status_code == 200:
        #[TODO]
        print("200")
        json = r.json()
        for c in json['categories']:
            #print(f'{c['idCategory']}', c['strCategory'], c['strCategoryDescription'])
            category = Category.Category(c['idCategory'], c['strCategory'], c['strCategoryDescription'])
            print(category)
    else:
        print("error")

getCategories()