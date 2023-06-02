from flask import redirect, request, url_for, render_template, Flask
from flask.views import MethodView
import requests
from flask import Flask
import json

app = Flask(__name__)

class Enter(MethodView):
    def get(self):
        return render_template('enter.html')

    def post(self):
        # Edamam API keys
        EDAMAM_API_ID = "ec4e4386"
        EDAMAM_API_KEY = "ff18d36a899d9fe39b9e4be092e30e02"

    
        EDAMAM_API_ID1 = "012b51a7"
        EDAMAM_API_KEY1 = "fd4db16491f7dd7864d821e2b8645900"
        
        # Spoonacular API key
        SPOONACULAR_API_KEY = "279e119500fd40b3bca3dd8e6a3ef7aa"

        # Function to analyze nutrients using Edamam API
        def analyze_nutrients(ingredient):
            url = "https://api.edamam.com/api/nutrition-data"
            params = {
                "app_id": EDAMAM_API_ID1,
                "app_key": EDAMAM_API_KEY1,
                "ingr": ingredient,
                "to": 1
            }
            response = requests.get(url, params=params)
            data = response.json()

            with open("data1.json", "w") as file:
                json.dump(data, file)

            nutrients = data.get("totalNutrients", {})
            return nutrients

        
        def search_recipes(ingredients):
            url = "https://api.spoonacular.com/recipes/findByIngredients"
            params = {
                "apiKey": SPOONACULAR_API_KEY,
                "ingredients": ingredients,
                "number": 1
            }
            response = requests.get(url, params=params)
            data = response.json()

            with open("data.json", "w") as file:
                json.dump(data, file)

            original_lines = [ingredient["original"] for ingredient in data[0]["usedIngredients"] + data[0]["missedIngredients"]]
            original_text = "\n".join(original_lines)
            return original_text
        # Your code goes here
        
        ingredients = request.form.get("ingredients").split(",")
        
        # # Search recipes
        recipes = search_recipes(ingredients)
        # recipe_info = []
        print(recipes)
    
        return render_template("enter.html")
        



