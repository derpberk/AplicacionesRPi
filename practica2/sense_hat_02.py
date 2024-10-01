from sense_hat import SenseHat

sense = SenseHat()
x,y = 4,4

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

color=[200, 200, 0]
sense.clear()
sense.set_pixel(x,y,color)
bucle = True

while bucle:
    # Obtenemos los eventos del joystick 
    events = sense.stick.get_events()
    
    for event in events:
        if event.direction  == "down" and event.action != "released":
            y = clamp(y + 1)
        if event.direction  == "up"and event.action != "released":
            y = clamp(y - 1)
        if event.direction  == "left"and event.action != "released":
            x = clamp(x - 1)
        if event.direction  == "right"and event.action != "released":
            x = clamp(x + 1)
        if event.direction  == "middle":
            bucle=False
            
        sense.clear()
        sense.set_pixel(x,y,color)
sense.clear()