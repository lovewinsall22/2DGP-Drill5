from pico2d import *

open_canvas()

ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
frame = 0

character_x, character_y = 400, 300

while running:
    clear_canvas()
    ground.draw(800 // 2, 600 // 2, 800, 600)
    character.clip_draw(frame * 100, 100, 100, 100, character_x, character_y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)


close_canvas()