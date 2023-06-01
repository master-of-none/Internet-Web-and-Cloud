from flask import redirect, request, url_for, render_template, Flask
from flask.views import MethodView
import requests
from flask import Flask

app = Flask(__name__)

class Enter(MethodView):
    def get(self):
        return render_template('enter.html')

    def post(self):
        # Edamam API keys
        EDAMAM_API_ID = "ec4e4386"
        EDAMAM_API_KEY = "ff18d36a899d9fe39b9e4be092e30e02"

        # Spoonacular API key
        SPOONACULAR_API_KEY = "279e119500fd40b3bca3dd8e6a3ef7aa"

        # Function to analyze nutrients using Edamam API
        def analyze_nutrients(ingredient):
            url = "https://api.edamam.com/api/nutrition-data"
            params = {
                "app_id": EDAMAM_API_ID,
                "app_key": EDAMAM_API_KEY,
                "ingr": ingredient,
                "to": 1
            }
            response = requests.get(url, params=params)
            data = response.json()
            nutrients = data.get("totalNutrients", {})
            return nutrients

        # Function to search recipes using Edamam API
        def search_recipes(ingredients):
            url = "https://api.edamam.com/api/recipes/v2"
            params = {
                "type": "public",
                "q": ",".join(ingredients),
                "app_id": EDAMAM_API_ID,
                "app_key": EDAMAM_API_KEY,
                "limit": 1  # Number of recipes to retrieve
            }
            response = requests.get(url, params=params)
            data = response.json()
            hits = data.get("hits")
            if hits:
                return hits[:1]  # Return only the first recipe
            else:
                return []

        # Function to get nutritional info using Spoonacular API
        def get_nutritional_info(recipe_url):
            url = "https://api.spoonacular.com/recipes/extract"
            params = {
                "apiKey": SPOONACULAR_API_KEY,
                "url": recipe_url
            }
            response = requests.get(url, params=params)
            data = response.json()
            nutrients = data.get("nutrition", {}).get("nutrients", [])
            return data

        # Your code goes here
        ingredients = request.form.get("ingredients").split(",")

        # Search recipes
        recipes = search_recipes(ingredients)
        recipe_info = []

        # Analyze nutrients for each recipe
        for recipe in recipes:
            recipe_url = recipe["recipe"]["url"]
            nutritional_info = get_nutritional_info(recipe_url)
            ingredients = nutritional_info.get("extendedIngredients", [])
            nutrients = []
            for ingredient in ingredients:
                nutrient = analyze_nutrients(ingredient["name"])
                nutrients.append({
                    "name": ingredient["name"],
                    "amount": ingredient.get("amount", ""),
                    "unit": ingredient.get("unit", ""),
                    "nutrient": nutrient
                })
            recipe_info.append({
                "title": recipe["recipe"]["label"],
                "image": recipe["recipe"]["image"],
                "url": recipe_url,
                "nutrients": nutrients
            })
    
        return render_template("enter.html", recipes=recipe_info)
        



