import requests, json, random
from random import Random
from Category import Category
from Meal import Meal
from Recipe import Recipe

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

def get_meal_by_category(category : Category):
    """
    Get all meal by category from themealdb
    """
    url = f'{BASE_URL}/filter.php?c={category.get_name()}'
    r = requests.get(url)

    meals = []
    if r.status_code == 200:
        json = r.json()
        for m in json['meals']:
            meal = Meal(m['idMeal'], m['strMeal'])
            meals.append(meal)
    else:
        print('An error has occured')
    return meals

def get_meal_by_name(name):
    """
    Get meal by name from themealdb
    """
    url = f'{BASE_URL}/search.php?s={name}'
    r = requests.get(url)

    if r.status_code == 200:
        json = r.json()
        m = json['meals']
        i = 1
        ingredients = []
        measures = []
        try:
            while m[0][f'strIngredient{i}'] != "":
                ingredients.append(m[0][f'strIngredient{i}'])
                measures.append(m[0][f'strMeasure{i}'])
                i += 1
            instructions = m[0]['strInstructions']
            meal = m[0]['strMeal']
            cateorgy = m[0]['strCategory']
            id = m[0]['idMeal']
            image_URL = m[0]['strMealThumb']
            recipe = Recipe(id, meal, cateorgy, instructions, ingredients, measures, image_URL)
        except TypeError:
            print("Meal is not found!")
            return None
    else:
        print('an error has occured')
    return recipe

def get_random_meal():
    """
    Get random meal from themealdb
    """
    url = f'{BASE_URL}/random.php'
    r = requests.get(url)

    if r.status_code == 200:
        json = r.json()
        m = json['meals']
        i = 1
        ingredients = []
        measures = []
        try:
            while m[0][f'strIngredient{i}'] != "":
                ingredients.append(m[0][f'strIngredient{i}'])
                measures.append(m[0][f'strMeasure{i}'])
                i += 1
            instructions = m[0]['strInstructions']
            meal = m[0]['strMeal']
            cateorgy = m[0]['strCategory']
            id = m[0]['idMeal']
            image_URL = m[0]['strMealThumb']
            recipe = Recipe(id, meal, cateorgy, instructions, ingredients, measures, image_URL)
        except TypeError:
            print("Meal is not found!")
            return None
    else:
        print('an error has occured')
    return recipe