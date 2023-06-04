from flask import redirect, request, url_for, render_template, Flask
from flask.views import MethodView
import requests
from flask import Flask
import json
import os

app = Flask(__name__)

class Nutrients(MethodView):
    def get(self):
        return render_template('nutrients.html')

    def post(self):
        # Edamam API keys
        # EDAMAM_API_ID = "ec4e4386"
        # EDAMAM_API_KEY = "ff18d36a899d9fe39b9e4be092e30e02"
        EDAMAM_API_ID="012b51a7"
        EDAMAM_API_KEY="fd4db16491f7dd7864d821e2b8645900"

    
        # EDAMAM_API_ID = os.environ.get('EDAMAM_API_ID')
        # EDAMAM_API_KEY = os.environ.get('EDAMAM_API_KEY')
        
        # Spoonacular API key
        SPOONACULAR_API_KEY = os.environ.get('SPOONACULAR_API_KEY')

        # Function to analyze nutrients using Edamam API
        def analyze_nutrients(ingredients):
            url = "https://api.edamam.com/api/nutrition-data"
            results = []
            for ingredient in ingredients:
                params = {
                    "app_id": EDAMAM_API_ID,
                    "app_key": EDAMAM_API_KEY,
                    "nutrition-type" : "logging",
                    "ingr": ingredient,
                    "to": 1
                }
                response = requests.get(url, params=params)
                data = response.json()
                results.append(data)
                with open("data1.json", "w") as file:
                    json.dump(results, file)
            
            total_nutrients = data['totalNutrientsKCal']
            return total_nutrients

        ingredients = request.form.get("ingredients").split(",")
        
        # # Search recipes
        recipes = analyze_nutrients(ingredients)
        print(recipes)

        return render_template("nutrients.html",recipes=recipes)

