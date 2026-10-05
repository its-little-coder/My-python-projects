import math                                                    

def get_bearing(x1, y1, x2, y2):  
    dx = x2 - x1
    dy = y2 - y1
    bearing = math.degrees(math.atan2(dx, dy)) 
    if bearing < 0:
        bearing += 360
    return bearing

def get_direction(bearing):
    if bearing < 22.5 or bearing >= 337.5:
        return "N"
    elif bearing < 67.5:
        return "NE"
    elif bearing < 112.5:
        return "E"
    elif bearing < 157.5:
        return "SE"
    elif bearing < 202.5:
        return "S"
    elif bearing < 247.5:
        return "SW"
    elif bearing < 292.5:
        return "W"
    else:
        return "NW"
        
def distance(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    distance = math.sqrt(dx**2+dy**2)
    return distance

x2, x1 = 46, 60
y2, y1 = 30, 45
    
bearing = get_bearing(x1, y1, x2, y2)
print(f"bearing: {bearing}")
direction = get_direction(bearing)
print(f"direction: {direction}")
distance = distance(x1, y1, x2, y2)
print(f"distance: {distance}")