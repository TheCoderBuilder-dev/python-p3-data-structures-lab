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
    # Return list of just the names
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    # Return foods with heat_level > 5
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    # Print each food in format: Name (Cuisine) | Heat Level: 🌶 * heat_level
    for food in spicy_foods:
        heat = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Return first food with matching cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    # Use get_spiciest_foods and print_spicy_foods to print only spicy ones
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    # Calculate average heat_level (integer)
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    count = len(spicy_foods)
    return total_heat // count if count > 0 else 0

def create_spicy_food(spicy_foods, spicy_food):
    # Append new spicy_food dict to list and return list
    spicy_foods.append(spicy_food)
    return spicy_foods
