#This is hazards.py

def get_hazard_color(aqi):
    if aqi == "N/A":
        return "gray"
    aqi = int(aqi)

    if aqi <= 50:
        return "green"  # good
    elif aqi <= 100:
        return "yellow"  # moderate
    elif aqi <= 150:
        return "orange"  # unhealthy for sensitive groups
    elif aqi <= 200:
        return "red"  # unhealthy
    elif aqi <= 300:
        return "purple"  # very unhealthy
    else:
        return "maroon"  # hazardous
