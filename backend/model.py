# backend/model.py# backend/model.py

# Mock crop metadata (could later be replaced with DB or AI model)
CROP_DATABASE = {
    "Sorghum": {
        "planting_season": "May to July",
        "water_requirements": "Low (300-500 mm)",
        "confidence": 82,
        "reason": "Tolerant to heat and low rainfall."
    },
    "Millet": {
        "planting_season": "May to August",
        "water_requirements": "Very low (250-400 mm)",
        "confidence": 80,
        "reason": "Thrives in dry, hot climates."
    },
    "Groundnuts": {
        "planting_season": "June to September",
        "water_requirements": "Moderate (500-700 mm)",
        "confidence": 78,
        "reason": "Good for semi-arid regions."
    },
    "Maize": {
        "planting_season": "March to May",
        "water_requirements": "Moderate (600-800 mm)",
        "confidence": 85,
        "reason": "Ideal in warm, humid climates with rain."
    },
    "Beans": {
        "planting_season": "March to June",
        "water_requirements": "Moderate (500-700 mm)",
        "confidence": 82,
        "reason": "Require well-distributed rainfall."
    },
    "Sweet Potatoes": {
        "planting_season": "April to June",
        "water_requirements": "Moderate (500-700 mm)",
        "confidence": 80,
        "reason": "Grow well in warm, moist conditions."
    },
    "Potatoes": {
        "planting_season": "February to April",
        "water_requirements": "High (700-1000 mm)",
        "confidence": 78,
        "reason": "Cool, moist weather is ideal."
    },
    "Peas": {
        "planting_season": "January to March",
        "water_requirements": "Moderate (400-600 mm)",
        "confidence": 75,
        "reason": "Grow in cooler climates."
    },
    "Barley": {
        "planting_season": "February to April",
        "water_requirements": "Moderate (400-600 mm)",
        "confidence": 76,
        "reason": "Thrives in cooler temperatures."
    },
    "Cassava": {
        "planting_season": "March to May",
        "water_requirements": "Low (500-700 mm)",
        "confidence": 70,
        "reason": "Drought-resistant and suitable for moderate conditions."
    },
    "Yams": {
        "planting_season": "April to July",
        "water_requirements": "Moderate to high (700-1000 mm)",
        "confidence": 72,
        "reason": "Good for moderate temperature and moisture."
    },
    "Cowpeas": {
        "planting_season": "May to July",
        "water_requirements": "Low to moderate (300-600 mm)",
        "confidence": 68,
        "reason": "Tolerant to poor soil and moderate climates."
    },
}



def recommend_crops(temp, humidity, rain):
    if temp > 30 and humidity < 40 and rain < 5:
        crops = ["Sorghum", "Millet", "Groundnuts"]

    elif 20 <= temp <= 30 and humidity >= 50 and rain >= 5:
        crops = ["Maize", "Beans", "Sweet Potatoes"]

    elif temp < 20 and humidity >= 60:
        crops = ["Potatoes", "Peas", "Barley"]

    else:
        crops = ["Cassava", "Yams", "Cowpeas"]

    # Return full details for each crop
    return [ 
        {
            "name": crop,
            **CROP_DATABASE.get(crop, {})
        }
        for crop in crops
    ]
