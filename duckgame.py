import pyglet
import random
window = pyglet.window.Window(850,650, "утки // очки: 0")
duck = pyglet.shapes.Rectangle(x=400, y=300, width=60, height=60, color=(255, 223, 0))
speed_x = 8
speed_y = 8
score = 0
@window.event
def on_mouse_press(x, y, button, modifiers):
    global score
    if button == pyglet.window.mouse.LEFT:
        if duck.x <= x <= duck.x + 60 and duck.y <= y <= duck.y + 60:
            score += 1
            print("[HIT] Точное попадание! Фраг засчитан! текущий счет: {score} 💥")
            window.set_caption(f"утки // очки: {score}")
            
            duck.x = random.randint(0, 850 - 60)
            duck.y = random.randint(0, 650 - 60)
@window.event
def on_draw():
    window.clear()
    duck.draw()
def update(dt):
    global speed_x,speed_y
    duck.x += speed_x
    duck.y += speed_y

    if duck.x <= 0 or duck.x >= 850 - 60:
        speed_x= -speed_x
    if duck.y <= 0 or duck.y >= 650 - 60:
        speed_y= -speed_y
pyglet.clock.schedule_interval(update, 1/60.0)

pyglet.app.run()