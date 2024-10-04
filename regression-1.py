import json

with open('oil.json', 'r') as file:
    oil_data = json.load(file)
    
oil_prices = [
    item["Data 3: Regular All Areas All Formulations"]
    for item in oil_data
    if any(year in item.get("Back to Contents", "") for year in ["2021", "2022", "2023"])
    and item["Data 3: Regular All Areas All Formulations"].replace('.', '', 1).isdigit() 
]

oil_prices = [float(price) for price in oil_prices]


#--------------------------------------------------------------------------------------#

with open('gold.json' , 'r') as file2:
    gold_data = json.load(file2)
    
oil_dates = set(
    item["Back to Contents"] for item in oil_data 
    if any(year in item["Back to Contents"] for year in ["2021", "2022", "2023"])
)
gold_price = [
    float(i["USD"].replace(',', ''))
    for i in gold_data
    if i["date"] in oil_dates
]



