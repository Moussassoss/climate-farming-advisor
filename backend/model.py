# backend/model.py
def recommend_crops(temp, humidity, rain):
    if temp > 30 and humidity < 40 and rain < 5:
        return ["Sorghum", "Millet", "Groundnuts"]

    # Warm and humid with some rain
    elif 20 <= temp <= 30 and humidity >= 50 and rain >= 5:
        return ["Maize", "Beans", "Sweet Potatoes"]

    # Cool and moist
    elif temp < 20 and humidity >= 60:
        return ["Potatoes", "Peas", "Barley"]

    # Moderate conditions
    else:
        return ["Cassava", "Yams", "Cowpeas"]

