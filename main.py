from ursina import *
from PIL import Image
import sys

black = (0,0,0)
green = (34, 177, 76)

try:
    save = open("savefile", "r").read()
    print(save)
except FileNotFoundError:
    save = "1"


level = "levels/" + save + ".png"

app = Ursina()


image = Image.open(level)
width, height = image.size
print (width, height)
window.windowed_size = (width, height)
window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True
camera.orthographic = True

bg = Entity(model='quad', texture=level, scale_x=width/height)
bg.scale *= 40
bg.aspect_ratio = bg.scale_x / bg.scale_y


def update():
    try:
        x = round((mouse.position[0] + 0.5) * width)
        y = round((abs(mouse.position[1] - 0.5)) * height)
        #print(x,y,image.getpixel((x, y)))
        print(mouse.position)
        if image.getpixel((x, y)) == black:
            open("savefile", "w").write(str(1))
            quit()
            
        if image.getpixel((x, y)) == green:
            print("congrats")
            open("savefile", "w").write(str(int(save) + 1))
            quit()

        
    except:
        pass

app.run()
