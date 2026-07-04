WIDTH =800
HEIGHT = 800

ball_x = 400
ball_y = 700

velocity = 0
gravity = 0.5

def draw():
    screen.clear()
    screen.draw.filled_circle((ball_x, ball_y),20 ,"yellow")
    
def update():
    global ball_y, velocity
    
    velocity += gravity
    ball_y += velocity
    
    if ball_y > HEIGHT:
        reset_game()
        
def on_key_down(key):
    global velocity
    if key == keys.SPACE:
        velocity = -10
        
def reset_game():
    global ball_y, velocity
    ball_y = 300
    velocity = 0