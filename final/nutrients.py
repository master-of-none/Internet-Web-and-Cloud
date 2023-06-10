"""
This file is used for another API which will display the nutrition when we give the ingredients and it will calculate the total energy count.
"""

from flask import redirect, request, url_for, render_template, Flask
from flask.views import MethodView
import requests
from flask import Flask
import json
import os

app = Flask(__name__)

"""
This is the nutrient class which contains the nutrients API.
"""
class Nutrients(MethodView):
    def get(self):
        return render_template('nutrients.html')

    def post(self):
    
        EDAMAM_API_ID = os.environ.get('EDAMAM_API_ID')
        EDAMAM_API_KEY = os.environ.get('EDAMAM_API_KEY')
        

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
            
            return results

        def print_values(data):
            output = []
            total_energy = 0
            total_protein_calories = 0
            total_fat_calories = 0
            total_carb_calories = 0

            # Accessing totalNutrientsKCal and its contents
            for nutrient_data in data:
                if 'totalNutrientsKCal' in nutrient_data:
                    total_nutrients = nutrient_data['totalNutrientsKCal']

                    # Accessing individual nutrient information
                    for nutrient_name, nutrient_info in total_nutrients.items():
                        label = nutrient_info['label']
                        quantity = nutrient_info['quantity']
                        unit = nutrient_info['unit']

                        output.append({
                            'nutrient': nutrient_name,
                            'label': label,
                            'quantity': f"{quantity} {unit}"
                        })

                        # Calculate sum for ENERC_KCAL (Energy)
                        if nutrient_name == 'ENERC_KCAL':
                            total_energy += quantity

                        # Calculate sum for PROCNT_KCAL (Calories from protein)
                        if nutrient_name == 'PROCNT_KCAL':
                            total_protein_calories += quantity

                        # Calculate sum for FAT_KCAL (Calories from fat)
                        if nutrient_name == 'FAT_KCAL':
                            total_fat_calories += quantity

                        # Calculate sum for CHOCDF_KCAL (Calories from carbohydrates)
                        if nutrient_name == 'CHOCDF_KCAL':
                            total_carb_calories += quantity

            return output, total_energy, total_protein_calories, total_fat_calories, total_carb_calories

        ingredients = request.form.get("ingredients").split(",")

        
        # Analyze the nutrients
        recipes = analyze_nutrients(ingredients)
        if recipes is None:
            error_message = "Nutritional value not found"
            return render_template("nutrients.html", error_message=error_message)

        output, total_energy, total_protein_calories, total_fat_calories, total_carb_calories = print_values(recipes)

        return render_template("nutrients.html", output=output, total_energy=total_energy,
                               total_protein_calories=total_protein_calories,
                               total_fat_calories=total_fat_calories,
                               total_carb_calories=total_carb_calories)  
        
