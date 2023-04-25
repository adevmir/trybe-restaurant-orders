import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path) as file:
            csv_file = csv.DictReader(file)
            menu = list(csv_file)
        dishes = {}

        for item in menu:
            if item["dish"] not in dishes:
                dishes[item['dish']] = Dish(item['dish'], float(item['price']))
            ingredient = Ingredient(item['ingredient'])
            amount = float(item['recipe_amount'])
            dishes[item['dish']].add_ingredient_dependency(ingredient, amount)
        self.dishes = set(dishes.values())
