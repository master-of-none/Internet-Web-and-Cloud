from flask import redirect, request, url_for, render_template, Flask
from flask.views import MethodView
import requests
from flask import Flask
import json
import os
import random

app = Flask(__name__)

class Enter(MethodView):
    def get(self):
        return render_template('enter.html')

    def post(self):
        # Spoonacular API key
        #SPOONACULAR_API_KEY = os.environ.get('SPOONACULAR_API_KEY')
        
        def search_recipes(ingredients):
            SPOONACULAR_API_KEY = os.environ.get('SPOONACULAR_API_KEY')
            api_key = SPOONACULAR_API_KEY
            #url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={api_key}'
            #url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={api_key}&number=2&random=true'
            url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={api_key}&number=20'
            response = requests.get(url)
            data = json.loads(response.text)
            with open("data.json", "w") as file:
                json.dump(data, file)

            if data:
                random_recipe = random.choice(data)
                #print(random_recipe)
                return random_recipe
            else:
                return None

        ingredients = request.form.get("ingredients").split(",")
        
        # # Search recipes
        recipes = search_recipes(ingredients)
        
        if recipes is None:
            error_message = "No recipe found"
            return render_template("enter.html", error_message=error_message)

        print(recipes['id'])
        print(recipes['title'])

        
        return render_template("enter.html", recipe=recipes)
        

class Favorites(MethodView):
    def post(self):
        recipe_id = request.form.get("recipe_id")
        recipe_title = request.form.get("recipe_title")
        print(recipe_id)
        print(recipe_title)
        added_to_favorites = True
        return render_template("enter.html",added_to_favorites=added_to_favorites)

