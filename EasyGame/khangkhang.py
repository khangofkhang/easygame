import pyglet
import random
from pyglet.window import key, mouse
shits = []
# Global variables
window = pyglet.window.Window(800, 600)
gameover = False
Score = 0.0
startgame = 0
endGame = 1                     # check end game
mouse_pos = [0,0]                   # mouse's position
speed = 3
check_speed=0
shit_play = pyglet.resource.image('play.png') #start game
# Kich thuoc con tau
shit_play.height = 100
shit_play.width = 100
#vi tri play game
pos_play = pyglet.sprite.Sprite(shit_play,800//2-shit_play.width//2, 600//2 -shit_play.height//2)
img_playAgain= pyglet.resource.image('replay.png')
img_playAgain.height = 150
img_playAgain.width = 300
shit_imgplayAgain = pyglet.sprite.Sprite(img_playAgain,800//2-img_playAgain.width*0.45/2, 600//2-170)

image = pyglet.resource.image('star.png')
shit = pyglet.resource.image('shit.png')
plane = pyglet.resource.image('plan.png')
cloud = pyglet.resource.image('cloud.png')
animation = pyglet.image.load_animation('hihi.gif')
bin = pyglet.image.atlas.TextureBin()
animation.add_to_texture_bin(bin)
sprite2 = pyglet.sprite.Sprite(img=animation)

label_start = pyglet.text.Label('The First Game of Khang Khang', 
                          font_name='Vivaldi', 
                          font_size=36,
                          x=100, y=400, color = (0,255,0,255))

lbOver = pyglet.text.Label('',font_size=25, x=0,y=300, color = (0,255,0,255))
#Hien thi ket qua
label = pyglet.text.Label('', font_size=20, y=575, x=10, color = (0,255,0,255))


# Kich thuoc con tau
plane.height = 75
plane.width = 75
# set vi tri ban dau cho con tau
sprite = pyglet.sprite.Sprite(plane, 450,0)
sprite.dx = 500#background image
def setdefaultvalue():
    global Score
    global speed
    global sh
    global cl
    global gameover
    Score = 0.0
    speed = 3
    sh = 0
    cl = 0
    gameover = False
    plane.height = 75
    plane.width = 75
    img_playAgain.height = 150
    img_playAgain.width = 150
    shit_play.height = 100
    shit_play.width = 100
    



# tao 1 list cac vat
def makeList(img):
    img.width = 60
    img.height =60
    list = []
    global value
    value = random.randint(8, 12)
    for i in range(value):
        x = random.randint(0, 750)
        y = random.randint(0, 600)
        list.append( pyglet.sprite.Sprite(img, x,y))
    return list
# cap nhat cat vat the cho lan roi tiep theo
def update(_):
    global speed
    global Score
    global check_speed
    Score += 1/100
    label.text = "Play Time: "+ str(round(Score,2))
    for sh in shits:
        print(speed)
        sh.y -= speed
        if sh.y < -75:
            shits.remove(sh)
            x = random.randint(0, 750)
            shits.append(pyglet.sprite.Sprite(shit, x,600))
        if check_speed == 1 and int(Score) % 5 ==0 and int(Score)!=0:
            print(Score)
            speed = speed + 3
            check_speed = 0
        elif int(Score) % 5 !=0:
            check_speed = 1
    for cl in list1:
        cl.y -= speed
        if cl.y < -75:
            cl.y = 600
            cl.x = random.randint(0,750)

setdefaultvalue()
#Lay danh sach cac vat the
shits = makeList(shit)
list1 = makeList(cloud)

@window.event
def on_mouse_motion(x, y, button, modifiers):
    global mouse_pos
    mouse_pos = [x,y]


@window.event
def on_mouse_press(x, y, button, modifiers):
    global startgame
    global gameover
    global Score
    lbOver.text = ''
    if button == mouse.LEFT and  pos_play.x<= x <=pos_play.x+shit_play.width\
            and pos_play.y<=y<=pos_play.y+shit_play.height:
        startgame = 1
    if button == mouse.LEFT and  shit_imgplayAgain.x<= x <=shit_imgplayAgain.x+shit_play.width:
        setdefaultvalue()
        print('play again')

#Ham di chuyen con tau
@window.event
def on_text_motion(motion):
    if(motion == pyglet.window.key.MOTION_RIGHT):
        sprite.x +=10
    if(motion == pyglet.window.key.MOTION_LEFT):
        sprite.x -=10
    if sprite.x < 0:
        sprite.x = 0
    if sprite.x > 725:
        sprite.x = 725
# Event callbacks
@window.event
def on_draw():
    global startgame
    window.clear()
    if startgame == 0:
        sprite2.draw()
        pos_play.draw()
        label_start.draw()
    else:
        if gameover:
            window.clear()
            sprite2.draw()
            shit_imgplayAgain.draw()
        else:
            window.clear()
            image.blit(0, 0)
            sprite.draw()
            label.draw()
            for sh in shits:
                sh.draw()
            for cl in list1:
                cl.draw()
        lbOver.draw()

# Den thoi gian chay
def game_loop(_):
    global gameover
    if not gameover:
        for sh in shits:
           if sh.x > sprite.x -20 and sh.x<sprite.x +20 and sh.y <= 75 and sh.y > 0:
               lbOver.text = "You Lose! You survived for "+ str(round(Score, 2)) +" seconds"
               gameover = True


pyglet.clock.schedule_interval(update,1/60)   # called twice a second
pyglet.clock.schedule_interval(game_loop,1/60) # Dem thoi gian
pyglet.app.run()
