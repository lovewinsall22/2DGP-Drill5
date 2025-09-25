from pico2d import *

open_canvas()

ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
frame = 0

character_x, character_y = 400, 300
dirX, dirY = 0, 0
ifRight = 1

def character_boundary():
    global character_x, character_y

    if character_x > 750: character_x = 750
    if character_x < 50: character_x = 50
    if character_y > 550: character_y = 550
    if character_y < 50: character_y = 50

def handle_events():
    global running
    global character_x, character_y, dirX, dirY, ifRight

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: # button
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:  # esc
                running = False
            elif event.key == SDLK_RIGHT:
                dirX += 1; ifRight = 1
            elif event.key == SDLK_LEFT:
                dirX -= 1; ifRight = 0
            elif event.key == SDLK_UP:
                dirY += 1; ifRight = 1
            elif event.key == SDLK_DOWN:
                dirY -= 1; ifRight = 0
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1; ifRight = 3
            elif event.key == SDLK_LEFT:
                dirX += 1; ifRight = 2
            elif event.key == SDLK_UP:
                dirY -= 1; ifRight = 3
            elif event.key == SDLK_DOWN:
                dirY += 1; ifRight = 2




while running:
    clear_canvas()
    ground.draw(800 // 2, 600 // 2, 800, 600)
    character.clip_draw(frame * 100, ifRight * 100 , 100, 100, character_x, character_y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    character_x += dirX * 10
    character_y += dirY * 10
    character_boundary()
    delay(0.05)


close_canvas()