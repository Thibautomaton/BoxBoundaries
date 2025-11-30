WIDTH = 1080
HEIGHT = 720

TARGET_FPS = 60
PPM = 10.0
STEP = 1/TARGET_FPS


def coordPixelsToWorld(P):
    world_x = P[0]/PPM
    world_y = (HEIGHT-P[1])/PPM
    return world_x, world_y

def coordWorldToPixel(P):
    screen_x = P[0]*PPM
    screen_y = -P[1]*PPM + HEIGHT
    return screen_x, screen_y

def scalarWorldToPixel(val):
    return val*PPM

def scalarPixelToWorld(val):
    return val/PPM


