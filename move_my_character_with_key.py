from pico2d import *

open_canvas()

ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
frame = 0

character_x, character_y = 400, 300
dir = 0

def handle_events():
    global running
    global character_x, character_y, dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: # button
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE: # esc
                running = False
            elif event.key == SDLK_RIGHT:
                character_x += 10
                dir = 1
            elif event.key == SDLK_LEFT:
                character_x -= 10
                dir = 0
            elif event.key == SDLK_UP:
                character_y += 10
                dir = 1
            elif event.key == SDLK_DOWN:
                character_y -= 10
                dir = 0
        elif event.type == SDL_KEYUP:
            if dir == 1: dir = 3
            elif dir == 0: dir = 2




while running:
    clear_canvas()
    ground.draw(800 // 2, 600 // 2, 800, 600)
    character.clip_draw(frame * 100, dir * 100 , 100, 100, character_x, character_y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)


close_canvas()