#!/usr/bin/env python
import requests
import textwrap
from colorama import Fore, init

init(strip=False)

URL = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
data = requests.get(url=URL).json()

drink = data["drinks"][0]
name = f"{Fore.GREEN}{drink['strDrink']}{Fore.RESET}"
category = f"{Fore.YELLOW}:::{drink['strCategory']}{Fore.RESET}"
instructions = "\n".join(textwrap.wrap(drink["strInstructions"], width=75, initial_indent=" ", subsequent_indent=" "))

ingredients_list = []
for index in range(1, 16):
    if drink[f"strIngredient{index}"]:
        ingredient = drink[f"strIngredient{index}"]
        measure = drink[f"strMeasure{index}"] or "by ear"
        entry = f"  {Fore.GREEN}°{Fore.RESET} {ingredient} {Fore.GREEN}~ {Fore.RESET}{measure}"
        ingredients_list.append(entry)
ingredients = "\n".join(ingredients_list)

print(f"{name} {category}\n{instructions}\n\n{ingredients}")