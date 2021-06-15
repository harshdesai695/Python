import pygame as py
import random
import os
import sys
py.init()
gw=py.display.set_mode((500,500))
py.display.set_caption("SNAKES")


#clock to control fps
clock=py.time.Clock()
fps=45


#color
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

font=py.font.SysFont(None,40)


def Score(text,color,x,y):
    screen_text=font.render(text,True,color)
    gw.blit(screen_text,[x,y])


def plot(gw,color,s_l,s_size):
    for x,y in s_l:
        py.draw.rect(gw,color,[x,y,s_size,s_size])
        
    

def gameloop():
    #game specific variable
    exit_game=False
    game_over=False
    vel=5
    s_x=45
    s_y=55
    v_x=0
    v_y=0
    f_x=random.randint(20,250)
    f_y=random.randint(20,250)
    s_size=10
    score=0
    s_l=[]
    slen=1
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt","r") as f:
        hiscore=f.read()

    #mainloop
    while not exit_game:
        if exit_game:
             py.QUIT()
             sys.Exit()
        if game_over:
            f=open("highscore.txt","w")
            f.write(str(score))
            gw.fill(white)
            Score("GAME OVER!",red,5,100)
            Score("score:"+str(score)+" HIGHSCORE:"+str(hiscore),red,5,200)
            for event in py.event.get():
                if event.type==py.QUIT:
                    exit_game=True
        else:    
            for event in py.event.get():
                if event.type==py.QUIT:
                    exit_game=True
                if event.type == py.KEYDOWN:
                    if event.key == py.K_LEFT:
                        v_x=-vel
                        v_y=0
                    if event.key == py.K_RIGHT:
                        v_x=vel
                        v_y=0
                    if event.key == py.K_UP:
                        v_y=-vel
                        v_x=0
                    if event.key == py.K_DOWN:
                        v_y=vel
                        v_x=0
                    if event.key == py.K_SPACE:
                        s_x=s_x+30
            s_x=s_x+v_x
            s_y=s_y+v_y

            if abs(s_x - f_x)<6 and abs(s_y - f_y)<6:
                score+=10
                f_x=random.randint(20,250)
                f_y=random.randint(20,250)
                slen+=5
            gw.fill(white)
            Score("score:"+str(score)+" HIGHSCORE:"+str(hiscore),red,5,5)
            py.draw.rect(gw,red,[f_x,f_y,s_size,s_size]) #FOOD

            h=[]
            h.append(s_x)
            h.append(s_y)
            s_l.append(h)

            if len(s_l)>slen:
                del s_l[0]
            if s_x<0 or s_x>500 or s_y>500 or s_y<0:
                game_over=True
            if h in s_l[:-1]:
                game_over=True
            if score>int(hiscore):
                hiscore=score
            
            plot(gw,black,s_l,s_size)#SNAKE

        py.display.update()
        clock.tick(fps)

gameloop()

