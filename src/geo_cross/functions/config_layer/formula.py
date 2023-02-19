# from layer import get_thickness

# determination of formula
def formula_determination(diameter, distance):
    if diameter < 45:
        thickness = sharpton(diameter, distance)
    elif diameter >= 45 and diameter <= 300:
        thickness = housen(diameter, distance)
    else:
        thickness = faset(diameter, distance)
    return thickness

# Sharpton - <45 km
def sharpton(diameter, distance):
    thickness = 3.95 * ((diameter * 500) ** 0.399) * (distance / (diameter * 500)) ** -3
    return thickness


# Hausen - 45-300 km
def housen(diameter, distance):
    thickness = 0.0078 * (diameter * 500) * (distance / (diameter * 500)) ** -2.61
    return thickness


# Faset - >300 km
def faset(diameter, distance):
    thickness = 2900 * (distance / (diameter * 500)) ** -2.8
    return thickness

