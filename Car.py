from cmu_graphics import *
import math

def onAppStart(app):
    app.middleX = app.height / 2
    app.middleY = app.width / 2
    app.carX = 200
    app.carY = 200
    app.carRotation = 180
    
    # Keys
    app.aBeingPressed = False
    app.dBeingPressed = False
    app.wBeingPressed = False
    app.sBeingPressed = False
    app.upBeingPressed = False
    app.downBeingPressed = False
    
    app.timeOnTrack = 0
    app.timeTotal = 1
    
    # Movement
    app.dm = 1
    app.rotationChange = 8

def redrawAll(app):
    # Background
    drawRect(0,0,app.width,app.height,fill='lightgreen') # Grass
    drawOval(app.middleX, app.middleY, 300, 300, fill=None, border='gray', borderWidth=40) # Road
    drawOval(app.middleX, app.middleY, 260, 260, fill=None, border='yellow', borderWidth=5, dashes=True) # Lines
    drawOval(app.middleX, app.middleY, 300, 300, fill=None, border='red', borderWidth=5, dashes=False) # Outside Border
    drawOval(app.middleX, app.middleY, 220, 220, fill=None, border='red', borderWidth=5, dashes=False) # Inside Border
    
    # Label
    drawLabel('Car Simulator',200, 24, size=24, bold=True)
    drawLabel(f'Precent of time spent on track: {(app.timeOnTrack / app.timeTotal) * 100 // 1}%', 200,380,bold=True)
    
    # Car
    drawCar(app)

def drawCar(app):
    drawRect(app.carX, app.carY, 20,15, fill=None, border='black',borderWidth=2, rotateAngle=app.carRotation, align='center') # Wheels
    drawRect(app.carX, app.carY, 10,17,fill='white', align='center', rotateAngle=app.carRotation) # Cut out wheels
    drawRect(app.carX, app.carY, 20,10,fill='lightgreen', align='center', rotateAngle=app.carRotation) # Cut out wheels
    drawRect(app.carX, app.carY, 20, 10, fill='darkorange', rotateAngle=app.carRotation, align='center') # Body
    drawRect(app.carX, app.carY, 5, 10, fill='blue', align='center', rotateAngle=app.carRotation) # Windsheild

def insideTrack(app):
    xDist = abs(200-app.carX)
    yDist = abs(200-app.carY)
    
    distance = math.sqrt(xDist**2 + yDist**2)
    if 220/2 <= distance <= 300/2:
        return True
    return False

def checkPositionInisdeApp(app, position):
    if not (0 <= position[0] <= app.width and 0 <= position[1] <= app.height):
        return False
    return True

def takeStep(app):
    app.timeTotal += 1
    if (insideTrack(app)):
        app.timeOnTrack += 1
        
    if app.aBeingPressed:
        app.carRotation -= app.rotationChange
    elif app.dBeingPressed:
        app.carRotation += app.rotationChange
    if app.upBeingPressed:
        app.dm += 0.1
    elif app.downBeingPressed:
        app.dm -= 0.1
        if app.dm < 0:
            app.dm = 0
    if app.wBeingPressed:
        newPostition = getRadiusEndpoint(app.carX, app.carY, app.dm, -app.carRotation)
        if not checkPositionInisdeApp(app, newPostition):
            return
        app.carX = newPostition[0]
        app.carY = newPostition[1]
    elif app.sBeingPressed:
        newPostition = getRadiusEndpoint(app.carX, app.carY, -app.dm, -app.carRotation)
        if not checkPositionInisdeApp(app, newPostition):
            return
        app.carX = newPostition[0]
        app.carY = newPostition[1]
    
        
def onStep(app):
    takeStep(app)
    
def getRadiusEndpoint(cx, cy, r, theta):
    return (cx + r*math.cos(math.radians(theta)),
            cy - r*math.sin(math.radians(theta)))

def onKeyPress(app, key):
    match key:
        case 'a':
            app.aBeingPressed = True
        case 'd':
            app.dBeingPressed = True
        case 'w':
            app.wBeingPressed = True
        case 's':
            app.sBeingPressed = True
        case 'up':
            app.upBeingPressed = True
        case 'down':
            app.downBeingPressed = True
            
def onKeyRelease(app, key):
    match key:
        case 'a':
            app.aBeingPressed = False
        case 'd':
            app.dBeingPressed = False
        case 'w':
            app.wBeingPressed = False
        case 's':
            app.sBeingPressed = False
        case 'up':
            app.upBeingPressed = False
        case 'down':
            app.downBeingPressed = False

    
def main():
    runApp()

main()