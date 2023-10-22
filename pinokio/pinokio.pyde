x=90



def setup():
    size (1000,1000)
    frameRate (10)
def draw():
    global x
    x=x+2
    strokeWeight (15)
    stroke (100,0,0)
    fill (100,0,0)
    rect (5,400,100,200)
    point (x,500)
    stroke (255)
    strokeWeight (25)
    point (75,450)
    stroke (0)
    strokeWeight (10)
    point (85,450)
