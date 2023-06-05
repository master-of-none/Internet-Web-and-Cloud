import json

# Assuming the JSON data is stored in a file called "data.json"
with open("data1.json", "r") as file:
    data = json.load(file)

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

            print(f"Nutrient: {nutrient_name}")
            print(f"Label: {label}")
            print(f"Quantity: {quantity} {unit}")

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

        # Accessing ingredient information (from the list)
        if nutrient_data.get('text'):
            ingredient_text = nutrient_data['text']
            print(f"Ingredient: {ingredient_text}")

        print()

print(f"Total Energy: {total_energy}")
print(f"Total Calories from Protein: {total_protein_calories}")
print(f"Total Calories from Fat: {total_fat_calories}")
print(f"Total Calories from Carbohydrates: {total_carb_calories}")

