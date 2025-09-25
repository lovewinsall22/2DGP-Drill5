from pico2d import *

open_canvas()

ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True




while running:
    clear_canvas()
    ground.draw(800 // 2, 600 // 2, 800, 600)
    update_canvas()
    delay(0.05)


close_canvas()