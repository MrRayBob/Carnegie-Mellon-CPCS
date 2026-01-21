from cmu_graphics import *
import random
import math
# Place your creative task here!

# Be clever, be creative, have fun!
def onAppStart(app):
    app.sunX = app.width / 2
    app.sunY = app.height / 2
    app.starBuffer = 20
    app.redoStars = True

    app.notScaleX = 340
    app.notScaleY = 370
    
    app.paused = False
    
    # Mercury
    app.mercuryRot = 0 # Ordbit
    app.mercuryRad = 60 # Ordbit
    app.mercuryColor = rgb(151, 151, 159)
    app.mercurySize = 4.6
    
    # Venus
    app.venusRot = 0 # Ordbit
    app.venusRad = 100 # Ordbit
    app.venusColor = rgb(146, 133, 144)
    app.venusSize = 11.4
    
    # Earth
    app.earthRot = 0 # Ordbit
    app.earthRad = 140 # Ordbit
    app.earthColor = 'blue'
    app.earthSize = 12
    
    # Mars
    app.marsRot = 0 # Ordbit
    app.marsRad = 180 # Ordbit
    app.marsColor = rgb(173, 98, 66)
    app.marsSize = 6.63
    
    # Orbit
    app.orbitLineWidth = 2
    app.timeForOneOrbit = 500
    
    # Orbits
    app.venusOrbitTime = app.timeForOneOrbit * 0.65
    app.mercuryOrbitTime = app.timeForOneOrbit * 0.24
    app.marsOrbitTime = app.timeForOneOrbit * 1.88
    
    # Time
    app.currentStep = 0
    app.stepsPerSecond = 60
    
    # Key presses
    app.upPressed = False
    app.downPressed = False
    app.changePerKeyPress = 5
    
    # Speed
    app.earthRotsASec = (app.timeForOneOrbit / app.stepsPerSecond) * 2
    
    # Stars
    app.starPositions = []
    i = 0
    for y in range(math.floor(app.height / app.starBuffer)):
        heightRangeTop = y * app.starBuffer
        heightRangeBottom = heightRangeTop + app.starBuffer
        for x in range (math.floor(app.width / app.starBuffer)):
            widthRangeTop = x * app.starBuffer
            widthRangeBottom = widthRangeTop + app.starBuffer
            
            xCord = random.randrange(widthRangeTop, widthRangeBottom, 1)
            yCord = random.randrange(heightRangeTop, heightRangeBottom, 1)
            
            app.starPositions.append((xCord, yCord))
            i += 1

def redrawAll(app):
    # Space
    drawRect(0, 0, app.width, app.height, fill='black')
    
    # Stars
    for position in app.starPositions:
        if not isinstance(position, tuple):
            break
        
        x = position[0]
        y = position[1]
        r = random.randrange(2,4,1)
        drawStar(x, y, r, 6, fill='white')
        
    # Sun
    drawCircle(app.sunX, app.sunY, 40, fill=rgb(255,204,51), border=rgb(255,216,56), borderWidth=6)
    
    # Mercury
    drawCircle(app.sunX, app.sunY, app.mercuryRad, fill=None, border='gray', borderWidth=app.orbitLineWidth, dashes=True) # Path
    x, y = getRadiusEndpoint(app.sunX, app.sunY, app.mercuryRad, app.mercuryRot)
    drawCircle(x,y,app.mercurySize, fill=app.mercuryColor)
    
    # Venus
    drawCircle(app.sunX, app.sunY, app.venusRad, fill=None, border='gray', borderWidth=app.orbitLineWidth, dashes=True) # Path
    x, y = getRadiusEndpoint(app.sunX, app.sunY, app.venusRad, app.venusRot)
    drawCircle(x,y,app.venusSize, fill=app.venusColor)
    
    # Earth
    drawCircle(app.sunX, app.sunY, app.earthRad, fill=None, border='gray', borderWidth=app.orbitLineWidth, dashes=True) # Path
    x, y = getRadiusEndpoint(app.sunX, app.sunY, app.earthRad, app.earthRot)
    drawCircle(x,y,app.earthSize, fill=app.earthColor)
    
     # Mars
    drawCircle(app.sunX, app.sunY, app.marsRad, fill=None, border='gray', borderWidth=app.orbitLineWidth, dashes=True) # Path
    x, y = getRadiusEndpoint(app.sunX, app.sunY, app.marsRad, app.marsRot)
    drawCircle(x,y,app.marsSize, fill=app.marsColor)
    
    # Not to scale
    drawRect(app.notScaleX, app.notScaleY, 80, 15, align='center', fill='black')
    drawLabel('*Not to Scale', app.notScaleX, app.notScaleY, fill='white', bold=True)
    
    # Solar System
    drawLabel('Solar System', 200, 40, fill='white', bold=True, size=24)
    
    # Labels
    drawRect(200, 60, 280, 10, align='center', fill='black')
    drawLabel('Press Up/Down to change speed, P to pause/unpause', 200, 60, fill="white", bold=True, size=12)
    
    drawRect(120, 370, 110, 25, align='center', fill='black')
    drawLabel(f"Sec / Earth Rotation: {pythonRound(app.earthRotsASec, 2)}", 120, 370, fill='white', bold=True, size=12)

def takeStep(app):
    if not app.paused:
        if (app.upPressed):
            changeOrbitTime(app, app.timeForOneOrbit - app.changePerKeyPress)
        elif (app.downPressed):
            changeOrbitTime(app, app.timeForOneOrbit + app.changePerKeyPress)
        else:
            app.currentStep += 1
            app.mercuryRot += (app.currentStep / app.mercuryOrbitTime) * 360 - app.mercuryRot
            app.venusRot += (app.currentStep / app.venusOrbitTime) * 360 - app.venusRot
            app.earthRot += (app.currentStep / app.timeForOneOrbit) * 360 - app.earthRot
            app.marsRot += (app.currentStep / app.marsOrbitTime) * 360 - app.marsRot
            #print(app.timeForOneOrbit)

def changeOrbitTime(app, newTime):
    if (newTime < 200): return None
    if (newTime > 800): return None
    app.timeForOneOrbit = newTime

    app.venusOrbitTime = app.timeForOneOrbit * 0.65
    app.mercuryOrbitTime = app.timeForOneOrbit * 0.24
    app.marsOrbitTime = app.timeForOneOrbit * 1.88
    
    app.earthRotsASec = (app.timeForOneOrbit / app.stepsPerSecond) * 2

def onKeyPress(app, key):
    match(key):
        case 'up':
            app.upPressed = True
        case 'down':
            app.downPressed = True
        case 'p':
            app.paused = not app.paused

def onKeyRelease(app, key):
    match(key):
        case 'up':
            app.upPressed = False
        case 'down':
            app.downPressed = False

def onStep(app):
    takeStep(app)

def getRadiusEndpoint(cx, cy, r, theta):
    return (cx + r*math.cos(math.radians(theta)),
            cy - r*math.sin(math.radians(theta)))


def main():
    runApp()


main()