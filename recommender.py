# recommender.py

def recommend_crops(weather):
    temp = weather["temperature"]
    humidity = weather["humidity"]

    if humidity > 60 and temp < 30:
        return ["Beans", "Cassava", "Sweet Potatoes"]
    elif humidity < 40:
        return ["Sorghum", "Millet", "Groundnuts"]
    elif temp > 35:
        return ["Pearl Millet", "Cowpeas"]
    else:
        return ["Maize", "Tomatoes", "Okra"]
