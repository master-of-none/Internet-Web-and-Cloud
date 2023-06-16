"""
This file contains the the api which gives the recipe based on ingredients.
"""

from flask import redirect, request, url_for, render_template, Flask
from flask.views import MethodView
import requests
from flask import Flask
import json
import os
import random
import gbmodel

app = Flask(__name__)

"""
This class is used to Enter the ingridients and and get it from the form.
"""
class Enter(MethodView):
    def get(self):
        return render_template('enter.html')

    def post(self):
        
        def search_recipes(ingredients):
           
            # Take the spoonacular API Key
            SPOONACULAR_API_KEY = os.environ.get('SPOONACULAR_API_KEY')
            api_key = SPOONACULAR_API_KEY
            
            # Acces the API URL and get the random recipe, we can change the number as desired, currently we are setting it to 20
            url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={api_key}&number=20'
            response = requests.get(url)
            data = json.loads(response.text)
            
            # This is used to test the json data which is returned
            with open("data.json", "w") as file:
                json.dump(data, file)

            if data:
                random_recipe = random.choice(data)
                #print(random_recipe)
                return random_recipe
            else:
                return None
        
        # Get the ingredients from html file
        ingredients = request.form.get("ingredients").split(",")
        
        # Search recipes
        recipes = search_recipes(ingredients)
        
        if recipes is None:
            error_message = "No recipe found"
            return render_template("enter.html", error_message=error_message)
        
        equip_id = recipes['id']

        print(recipes['id'])
        print(recipes['title'])
        SPOONACULAR_API_KEY = os.environ.get('SPOONACULAR_API_KEY')
        api_key = SPOONACULAR_API_KEY
  
        # Another API endpoint to display the equpment required to prepare the recipe
        image_url = f"https://api.spoonacular.com/recipes/{equip_id}/equipmentWidget.png?apiKey={api_key}"
        
        # This was primarily used for testing purposes
        response = requests.get(image_url)
        if response.status_code == 200:
            with open('image.png', 'wb') as file:
                file.write(response.content)
        else:
            print("image error")
            return render_template("enter.html", recipe=recipes)
            
        
        return render_template("enter.html", recipe=recipes,image_url=image_url)
        
"""
This class is used add the recipe to Favorites
"""
class Favorites(MethodView):
    def post(self):
        recipe_id = request.form.get("recipe_id")
        recipe_title = request.form.get("recipe_title")
        print(recipe_id)
        print(recipe_title)
        
        id = recipe_id
        title = recipe_title

        model = gbmodel.get_model()
        model.insert(id, title)
        added_to_favorites = True
        return render_template("enter.html",added_to_favorites=added_to_favorites)

