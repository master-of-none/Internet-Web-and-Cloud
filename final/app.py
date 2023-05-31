from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Initally passing the API keys here then will pass via environment variables

# Edamam api key and id
EDAMAM_API_ID = ""
EDAMAM_API_KEY = ""

# Spoonacular API credentials
SPOONACULAR_API_KEY = ""

# Function to search the recepies
def search_recipes(ingredients):
    url = "https://api.edamam.com/api/recipes/v2"
    params = {
        "type": "public",
        "q": ",".join(ingredients),
        "app_id": EDAMAM_API_ID,
        "app_key": EDAMAM_API_KEY,
        "limit": 5  # Number of recipes to retrieve
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["hits"]

# Get nutrition info
def get_nutritional_info(recipe_url):
    url = "https://api.spoonacular.com/recipes/extract"
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "url": recipe_url
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        ingredients = request.form.get("ingredients").split(",")

        recipes = search_recipes(ingredients)
        recipe_info = []

        for recipe in recipes:
            recipe_url = recipe["recipe"]["url"]
            nutritional_info = get_nutritional_info(recipe_url)
            recipe_info.append({
                "title": recipe["recipe"]["label"],
                "image": recipe["recipe"]["image"],
                "url": recipe_url,
                "nutrients": nutritional_info["nutrition"]["nutrients"]
            })

        return render_template("index.html", recipes=recipe_info)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
