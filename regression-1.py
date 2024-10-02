import json

with open('D:\\Uni\\Year2\\Linear\\oil.json', 'r') as file:
    oil_data = json.load(file)
    
oil_prices = [
    item["Data 3: Regular All Areas All Formulations"]
    for item in oil_data
    if any(year in item.get("Back to Contents", "") for year in ["2021", "2022", "2023"])
    and item["Data 3: Regular All Areas All Formulations"].replace('.', '', 1).isdigit() 
]

oil_prices = [float(price) for price in oil_prices]

#--------------------------------------------------------------------------------------#



