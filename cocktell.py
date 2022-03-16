#!/usr/bin/env python
import requests
from colorama import Fore, init

init()

URL = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
r = requests.get(url=URL)
data = r.json()

drink = data["drinks"][0]
name = drink["strDrink"]
category = drink["strCategory"]
instructions = drink["strInstructions"].replace(". ", ".\n ")

ingredient_list = []

index = 1
while True:
    if drink[f"strIngredient{index}"] and index <= 15:
        ingredient = drink[f"strIngredient{index}"]
        measure = drink[f"strMeasure{index}"] or "by ear"
        entry = f"{ingredient} {Fore.GREEN}~ {Fore.RESET}{measure}"
        ingredient_list.append(entry)
        index += 1
    else:
        break

print(f"{Fore.GREEN}{name}{Fore.RESET} {Fore.YELLOW}::: {category}{Fore.RESET}\n {instructions}")
for ingredient in ingredient_list:
    print(f"  {Fore.GREEN}°{Fore.RESET} {ingredient}")