# backend/model.py
def recommend_crops(temp, humidity):
    if temp > 30 and humidity < 40:
        return ["Sorghum", "Millet", "Groundnuts"]
    elif 20 <= temp <= 30 and humidity >= 50:
        return ["Maize", "Beans", "Sweet Potatoes"]
    elif temp < 20:
        return ["Potatoes", "Peas", "Barley"]
    else:
        return ["Cassava", "Yams", "Cowpeas"]
