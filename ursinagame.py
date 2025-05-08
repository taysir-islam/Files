from ursina import *

app = Ursina()

window.title = 'Shadowlight: Rift of Echoes'
window.borderless = False
window.fullscreen = False
camera.orthographic = True
camera.fov = 20

# Add a Sky entity for the background
background = Entity(model='quad', scale=(40, 20), z=10, color=color.cyan)  # Default to light mode

player = Entity(model='quad', color=color.yellow, scale=(1, 1), collider='box', position=(0, 2))
shadow = Entity(model='quad', color=color.rgb(128, 0, 128).tint(0.3), scale=(1, 1), position=(0, 2), enabled=True)

GRAVITY = 0.3
JUMP_FORCE = 0.22
ground_y = -3
level_index = 0
world_mode = 'light'
velocity_y = 0
on_ground = False
score = 0

levels = [
    {
        'platforms': [(-3, -2), (3, -1), (7, -1)],
        'coins': [(3, 0), (7, 0)],
        'enemies': [(4, -0.5)],
        'width': 12
    },
    {
        'platforms': [(0, -2), (4, -1), (8, -1)],
        'coins': [(4, 0), (8, 0)],
        'enemies': [(5, -0.5)],
        'width': 13
    },
    {
        'platforms': [(0, -2), (5, -1), (10, 0)],
        'coins': [(5, 0), (10, 1)],
        'enemies': [(6, -0.5)],
        'width': 15
    }
]

platforms = []
coins = []
enemies = []

coin_sound = Audio('sounds/coin.mp3', autoplay=False)
hurt_sound = Audio('sounds/hurt.mp3', autoplay=False)

def load_level(i):
    global level_index, platforms, coins, enemies
    # Destroy all existing entities
    for entity in platforms + coins + enemies:
        destroy(entity)

    level = levels[i]
    platforms = [Entity(model='cube', collider='box', scale=(3, 0.5), position=p, color=color.black if world_mode == 'light' else color.white) for p in level['platforms']]
    coins = [Entity(model='circle', color=color.yellow, scale=0.5, position=c) for c in level['coins']]
    enemies = [Entity(model='quad', color=color.red, scale=0.5, position=e, collider='box') for e in level['enemies']]
    camera.position = (0, 0)
    player.position = (-5, 2)  # Reset player position
    shadow.position = player.position

load_level(level_index)

def input(key):
    global world_mode
    if key == 'shift':
        # Toggle world mode
        world_mode = 'shadow' if world_mode == 'light' else 'light'
        
        # Update platform colors
        for p in platforms:
            p.color = color.black if world_mode == 'light' else color.white
        
        # Update background color
        background.color = color.cyan if world_mode == 'light' else color.dark_gray  # Day for light mode, night for shadow mode

def update():
    global velocity_y, on_ground, score, level_index

    dx = held_keys['d'] - held_keys['a']
    player.x += dx * time.dt * 5
    shadow.position = player.position + Vec3(0.2, -0.2, -0.1)  # Adjust shadow position and set z to -0.1

    velocity_y -= GRAVITY * time.dt
    player.y += velocity_y
    on_ground = False

    for plat in platforms:
        if player.intersects(plat).hit and velocity_y < 0:
            player.y = plat.y + 0.75
            velocity_y = 0
            on_ground = True

    if player.y <= ground_y:
        player.y = ground_y
        velocity_y = 0
        on_ground = True

    if held_keys['space'] and on_ground:
        velocity_y = JUMP_FORCE

    for c in coins:
        if c.enabled and distance(player.position, c.position) < 0.6:
            c.enabled = False
            coin_sound.play()
            score += 1
            score_text.text = f'Score: {score}'

    for e in enemies:
        if player.intersects(e).hit:
            hurt_sound.play()
            score = 0
            score_text.text = f'Score: {score}'
            level_index = 0
            load_level(level_index)

    if player.x > levels[level_index]['width']:
        level_index += 1
        if level_index >= len(levels):
            level_index = 0
        load_level(level_index)

    camera.x = lerp(camera.x, player.x, time.dt * 4)

score_text = Text(text=f'Score: {score}', position=(-0.85, 0.45), scale=2, origin=(0, 0))

def late_update():
    score_text.text = f'Score: {score}'

app.run()
