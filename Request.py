import requests, json
from Category import Category

# API base URL
BASE_URL = "https://www.themealdb.com/api/json/v1/1"


def get_catagories():
    """
    Get all meal categories from themealdb
    """
    url = f'{BASE_URL}/categories.php'
    r = requests.get(url)
    categories = []

    if r.status_code == 200:
        json = r.json()
        for c in json['categories']:
            category = Category(c['idCategory'], c['strCategory'], c['strCategoryDescription'])
            categories.append(category)            
    else:
        print("error")
    return categories