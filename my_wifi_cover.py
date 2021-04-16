from drawtool import DrawTool
import math

dt = DrawTool()
dt.set_XY_range(0,1000, 0,1000)
dt.set_aspect('equal')

def distance(x1, y1, x2, y2):
    return math.sqrt( (x1-x2)**2 + (y1-y2)**2 )

def draw_intersection():
    dt.draw_line(0,400, 1000,400)
    dt.draw_line(0,600, 1000,600)

def draw_lampposts(X, n):
    dt.set_color('r')
    for i in range(n):
        dt.draw_filled_circle(X[i], 400, 10)
        dt.draw_filled_circle(X[i], 600, 10)

def make_lamppost_list(n):
    L = []
    x_incr = 1000 / (n-1)
    x = 0
    for i in range(n):
        L.append(x)
        x += x_incr
    return L

def draw_wifi_circles(X, R):
    dt.set_color('g')
    for x in X:
        dt.draw_circle(x,400, R)

def get_uncovered(LX, WX, R):
    # NOTE: LX has the x coordinates of all north-side lampposts
    # WX has x coordinates of all south-side lampposts with receivers
    # R is the radius

    uncovered = []

    # WRITE CODE HERE to add to the list uncovered all those
    # x values of the lampposts in upper side that are not
    # within any circle.
    for post in LX:
        post_covered = False
        for receiver in WX:
            if distance(post, 600, receiver, 400) <= R:
                post_covered = True
                break
        if not post_covered:
            uncovered.append(post)

    return uncovered

R = 210
num_lampposts = 21
draw_intersection()
L = make_lamppost_list(num_lampposts)
draw_lampposts(L, num_lampposts)

# Place south-side receivers at these lampposts, as indicated by
# their x-coordinates.
WX = [100, 400, 600, 900]
draw_wifi_circles(WX, 220)
uncovered_list = get_uncovered(L, WX, R)
print('Not covered:', uncovered_list)
# Should print: 
# Not covered: [0, 200.0, 250.0, 300.0, 500.0, 700.0, 750.0, 800.0, 1000.0]

dt.display()

#!!!ATTENTION EMERSON!!!
# Not sure if this works, I dont have drawtool on my machine so I cant 
# test it but in theory it should work lmk if it doesnt