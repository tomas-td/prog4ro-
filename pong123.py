import random

import pyglet
from pyglet import gl
from pyglet.window import key

"""
Toto je jednoduchá implementácia hry pong.
Jedná sa o už vypracovanú verziu s vyplnenými TODOS:
"""

"""
------------------------------
Konštanty pre našu hru
------------------------------
"""
#WINDOW_SIZE
WIDTH = 1200
HEIGHT = 800

BALL_SIZE = 20
BAD_THICKNESS = 10
BAD_WIDTH = 100
SPEED = 500 #px/s
BAD_SPEED = SPEED * 1 #px/s

MID_LINE_WIDTH = 20
FONT_SIZE= 42 #px
FONT_PADDING = 30

"""
-------------------------------------
Stavové premenné pre našu hru
-------------------------------------
"""
bats_pozicions=[HEIGHT / 2, HEIGHT / 2] #Vertical pozicion of both bats
ball_pozition = [0, 0] #Ball position x and y
ball_speed = [0,0] #x-speed of ball, y-speed of ball
pressed_keyboards = set() # set of pressed keyboards
score= [0,0] #Both player score

"""
------------------------------------------------
Funkcie hry
------------------------------------------------
"""

"""
Draw rectangle on coordinates
Diagram:
    y2 - +-----+
         |/////|
    y1 - +-----+
         :     :
        x1    x2
"""
def draw_rectangle(x1,y1,x2,y2):

    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(int(x1), int(y1))
    gl.glVertex2f(int(x1), int(y2))
    gl.glVertex2f(int(x2), int(y2))
    gl.glVertex2f(int(x2), int(y1))

    gl.glEnd()



"""
Draw actual state of game
"""
def draw_game():
    #Todo: for students - implement this
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # smaz obsah okna (vyfarbi na cierno)
    gl.glColor3f(1, 1, 1)  # nastav barvu kresleni na bielu

    # Vykreslenie lopty

    draw_rectangle(
        ball_pozition[0] - BALL_SIZE // 2,
        ball_pozition[1] - BALL_SIZE // 2,
        ball_pozition[0] + BALL_SIZE // 2,
        ball_pozition[1] + BALL_SIZE // 2)

    # palky - urobime si zoznam souradnic palok a pre kazdu dvojicu souradnic
    # v tom zozname palku vykreslime
    for x, y in [(0, bats_pozicions[0]), (WIDTH, bats_pozicions[1])] :
        draw_rectangle(
            x - BAD_THICKNESS,
            y - BAD_WIDTH// 2,
            x + BAD_THICKNESS,
            y + BAD_WIDTH // 2)

    # prerusovana puliaca ciara - zlozena z viac malych obdlznickov
    for y in range(MID_LINE_WIDTH // 2, HEIGHT, MID_LINE_WIDTH * 2):
        draw_rectangle(
            WIDTH // 2 - 1,
            y,
            WIDTH // 2 + 1,
            y + MID_LINE_WIDTH
        )

    # A nakoniec vypiseme skore oboch hracov
    draw_text(str(score[0]),
                  x=FONT_PADDING,
                  y=HEIGHT - FONT_PADDING - FONT_SIZE,
                  pozice_x='left')

    draw_text(str(score[1]),
                  x=WIDTH - FONT_PADDING,
                  y=HEIGHT - FONT_PADDING - FONT_SIZE,
                  pozice_x='right')


"""Nakresli dany text na danu poziciu

Argument ``pozice_x`` muze byt "left" nebo "right", udava na kterou stranu
bude text zarovnany
"""
def draw_text(text, x, y, pozice_x):
    napis = pyglet.text.Label(
        text,
        font_name='League Gothic',
        font_size=FONT_SIZE,
        x=x, y=y, anchor_x=pozice_x)
    napis.draw()

def key_press(symbol, modifikatory):
    if symbol == key.W:
        pressed_keyboards.add(('nahoru', 0))
    if symbol == key.S:
        pressed_keyboards.add(('dolu', 0))
    if symbol == key.UP:
        pressed_keyboards.add(('nahoru', 1))
    if symbol == key.DOWN:
        pressed_keyboards.add(('dolu', 1))

def key_release(symbol, modifikatory):
    if symbol == key.W:
        pressed_keyboards.discard(('nahoru', 0))
    if symbol == key.S:
        pressed_keyboards.discard(('dolu', 0))
    if symbol == key.UP:
        pressed_keyboards.discard(('nahoru', 1))
    if symbol == key.DOWN:
        pressed_keyboards.discard(('dolu', 1))


def obnov_stav(dt):
    for cislo_palky in (0, 1):
        # pohyb podle klaves (viz funkce `stisk_klavesy`)
        if ('nahoru', cislo_palky) in pressed_keyboards:
            bats_pozicions[cislo_palky] += BAD_SPEED * dt
        if ('dolu', cislo_palky) in pressed_keyboards:
            bats_pozicions[cislo_palky] -= BAD_SPEED * dt

        # dolni zarazka - kdyz je palka prilis dole, nastavime ji na minimum
        if bats_pozicions[cislo_palky] < BAD_WIDTH / 2:
            bats_pozicions[cislo_palky] = BAD_WIDTH / 2
        # horni zarazka - kdyz je palka prilis nahore, nastavime ji na maximum
        if bats_pozicions[cislo_palky] > HEIGHT - BAD_WIDTH / 2:
            bats_pozicions[cislo_palky] = HEIGHT - BAD_WIDTH / 2

    # POHYB MICKU
    ball_pozition[0] += ball_speed[0] * dt
    ball_pozition[1] += ball_speed[1] * dt

    # Odraz micku od sten
    if ball_pozition[1] < BALL_SIZE // 2:
        ball_speed[1] = abs(ball_speed[1])
    if ball_pozition[1] > HEIGHT - BALL_SIZE // 2:
        ball_speed[1] = -abs(ball_speed[1])

    palka_min = ball_pozition[1] - BALL_SIZE / 2 - BAD_WIDTH / 2
    palka_max = ball_pozition[1] + BALL_SIZE / 2 + BAD_WIDTH / 2

    # odrazeni vlevo Todo: dorobiť
    if ball_pozition[0] < BAD_THICKNESS + BALL_SIZE / 2:
        if palka_min < bats_pozicions[0] < palka_max:
            ball_speed[0] = abs(ball_speed[0])
        else:
            score[1] += 1
            reset()
    # odrazeni vpravo Todo: dorobiť
    if ball_pozition[0] > WIDTH - (BAD_THICKNESS + BALL_SIZE / 2):
        if palka_min < bats_pozicions[1] < palka_max:
            ball_speed[0] = -abs(ball_speed[0])
        else:
            score[0] += 1
            reset()


def reset():
    """
        Todo: implelemntujte reset lopticky
    """
    #Vrat loptu dostredu
    ball_pozition[0] = WIDTH // 2
    ball_pozition[1] = HEIGHT // 2

    # x-ova rychlost - bud vpravo, nebo vlevo (nahodne)
    if random.randint(0, 1):
        ball_speed[0] = SPEED
    else:
        ball_speed[0] = -SPEED

    # y-ova rychlost - uplne nahodna

ball_speed[1] = random.uniform(-1, 1) * SPEED
"""
Hrawwwwwwwww
"""
# nastavit vychozi stav pro start hry


reset()

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)
window.push_handlers(
    on_draw=draw_game,
    on_key_press=key_press,
    on_key_release=key_release,)
pyglet.clock.schedule(obnov_stav)
pyglet.app.run()  # all is set, the game can start