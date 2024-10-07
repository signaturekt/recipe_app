class Recipe:
    def __init__(self, ID, name, category, instruction, ingredients, measures, image_URL):
        self.ID = ID
        self.name = name
        self.category = category
        self.instruction = instruction
        self.ingredients = ingredients
        self.measures = measures
        self.image_URL = image_URL

    def __str__(self):
        name = f'{self.ID} - {self.name} - {self.category}'
        instructions = self.instruction
        ingredients_measurements = []

        i = 0
        for ingredient in self.ingredients:
            ingredients_measurements.append(f'{ingredient} - {self.measures[i]}')
            i += 1
        
        recipe_string = f"\n{name}\n\nINSTRUCTIONS:\n{instructions}\n\nINGREDIENTS:\n"
        recipe_string += "\n".join(ingredients_measurements)
        return recipe_string