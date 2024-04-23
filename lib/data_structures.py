spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
   names = [food['name'] for food in spicy_foods]
   return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food.get('heat_level', 0) > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food.get('heat_level', 0)
        emojis = '🌶' * heat_level
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get('cuisine') == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food.get('heat_level', 0)
        if heat_level > 5:
            emojis = '🌶' * heat_level
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emojis}")

def get_average_heat_level(spicy_foods):
    total_heat = sum(food.get('heat_level', 0) for food in spicy_foods)
    average_heat = total_heat / len(spicy_foods)
    return average_heat

def create_spicy_food(spicy_foods, spicy_food):
   new_spicy_food = {
            'name': 'Griot',
            'cuisine': 'Haitian',
            'heat_level': 10,
        }
   updated_spicy_foods = spicy_foods + [new_spicy_food]
   return updated_spicy_foods