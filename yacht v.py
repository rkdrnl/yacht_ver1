#yacht! ^^7
import pygame
import sys
import time
import random

pygame.init()
player_1_name = ""
player_2_name = ""
font = pygame.font.Font(None, 32)
sfont = pygame.font.Font(None, 45)
mfont = pygame.font.Font(None, 60)
bfont = pygame.font.Font(None, 100)
bbfont = pygame.font.Font(None, 130)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 50, 50)
green = (0, 125, 0)
gray = (130, 130, 130)
menu = False
lobby = False
gamestart = False
titleimg = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\yachttitle.png")
startimg = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\starticon.png")
quitimg = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\quiticon.png")
clickstartimg = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\clickedStartIcon.png")
clickquitimg = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\clickedQuitIcon.png")
helpimg = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\help.PNG")
clickhelpimg = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\help2.PNG")
game_start_buttonimg = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\yachtstart2.PNG")
click_game_start_buttonimg = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\clickedyachtstart.PNG")
backimg = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\back.PNG")
clickbackimg = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\clickedback.PNG")
inp_player_1_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\player 1 for inputbox.PNG")
inp_player_2_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\player 2 for inputbox.PNG")
dice1_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\dice1.PNG")
dice2_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\dice2.PNG")
dice3_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\dice3.PNG")
dice4_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\dice4.PNG")
dice5_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\dice5.PNG")
dice6_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\dice6.PNG")
s_dice1_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\s_dice1.PNG")
s_dice2_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\s_dice2.PNG")
s_dice3_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\s_dice3.PNG")
s_dice4_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\s_dice4.PNG")
s_dice5_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\s_dice5.PNG")
s_dice6_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\s_dice6.PNG")
choise_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\choise.PNG")
fkind_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\fkind.PNG")
fhouse_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\fhouse.PNG")
sstrate_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\sstrate.PNG")
lstrate_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\lstrate.PNG")
yacht_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\yacht.PNG")
keep_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\keep.PNG")
reroll_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\reroll.PNG")
clickeep_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\clickedkeep.PNG")
clickreroll_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\clickedreroll.PNG")
choosedice_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\choosedice.png")
choosedice2_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\choosedice2.png")
exit_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\exit.png")
clickexit_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\clickedexit.png")
dicelist_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\dicelist.png")
screenblind_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\screenblind.png")
turnover_img = pygame.image.load(r"C:\Users\user\Pictures\pygameimage\turnover.png")
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
Drollist = [0,0,0,0,0]
keeplist = [0,0,0,0,0]
selectlist = [1,1,1,1,1]
sumwidth = 10
rolled = 0
choosing = 0
turn = 0

###########################변수 지정####################################
                               
pygame.display.set_caption("yacht!")
clock = pygame.time.Clock()

class Button:
    def __init__(self, img_in ,x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            SCREEN.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(0.1)
                action()
        else:
            SCREEN.blit(img_in,(x,y))

class keepButton:
    def __init__(self, dkeep, img_in ,x, y, width, height, img_act, x_act, y_act, action = None):
        global sumkeep
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            SCREEN.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(0.1)
                sumkeep = dkeep
                action()
        else:
            SCREEN.blit(img_in,(x,y))

        

##################################################


def player_turn():
    time.sleep(1.5)
    sumptext = 800
    ptext = bbfont.render(str(player_1_name + "'s turn"),True,black)
    while sumptext + 650:
        SCREEN.blit(screenblind_img,(sumptext, 20))
        SCREEN.blit(ptext,(sumptext, 50))
        sumptext = sumptext - 5
        pygame.display.update()
        clock.tick(150)

    

def pedigree():
    print("pedigree")
def diceroll():
    global sumwidth
    time.sleep(1)  
    if selectlist[0] == 1:
        Drollist[0] = random.randrange(1,7)
    if selectlist[1] == 1:
        Drollist[1] = random.randrange(1,7)
    if selectlist[2] == 1:
        Drollist[2] = random.randrange(1,7)
    if selectlist[3] == 1:
        Drollist[3] = random.randrange(1,7)
    if selectlist[4] == 1:
        Drollist[4] = random.randrange(1,7)
    for i in Drollist:
        if i == 1: 
            SCREEN.blit(dice1_img, (sumwidth, 30))
            pygame.display.update()
            time.sleep(0.3)
            print(i)
        elif i == 2: 
            SCREEN.blit(dice2_img, (sumwidth, 30))
            pygame.display.update()
            time.sleep(0.3)
            print(i)
        elif i == 3:
            SCREEN.blit(dice3_img, (sumwidth, 30))
            pygame.display.update()
            time.sleep(0.3)
            print(i)
        elif i == 4: 
            SCREEN.blit(dice4_img, (sumwidth, 30))
            pygame.display.update() 
            time.sleep(0.3)
            print(i)
        elif i == 5: 
            SCREEN.blit(dice5_img, (sumwidth, 30))
            pygame.display.update()
            time.sleep(0.3)
            print(i)
        elif i == 6: 
            SCREEN.blit(dice6_img, (sumwidth, 30))
            pygame.display.update()
            time.sleep(0.3)
            print(i)
        sumwidth = sumwidth + 160

def keep():
    checkeep = 0
    sumkeep = 1
    global sumwidth
    sumwidth = 1
    for i in selectlist:
        if selectlist[checkeep] == 1:
            choosediceButton = keepButton(sumkeep, choosedice_img, sumwidth,21,150,200,choosedice_img,sumwidth,21,keeping) 
        else:
            choosediceButton2 = keepButton(sumkeep, choosedice2_img, sumwidth,21,150,200,choosedice2_img,sumwidth,21,keeped) 
        checkeep = checkeep + 1
        sumwidth = sumwidth + 160
        sumkeep = sumkeep + 1
def keeping():
    global sumkeep
    if sumkeep == 1:
        print("one")
        selectlist[0] = 0
    if sumkeep == 2:
        print("two")
        selectlist[1] = 0
    if sumkeep == 3:
        print("three")
        selectlist[2] = 0
    if sumkeep == 4:
        print("four")
        selectlist[3] = 0
    if sumkeep == 5:
        print("five")
        selectlist[4] = 0
    pygame.display.update()

def keeped():
    global sumkeep
    if sumkeep == 1:
        print("one")
        selectlist[0] = 1
    if sumkeep == 2:
        print("two")
        selectlist[1] = 1
    if sumkeep == 3:
        print("three")
        selectlist[2] = 1
    if sumkeep == 4:
        print("four")
        selectlist[3] = 1
    if sumkeep == 5:
        print("five")
        selectlist[4] = 1
    pygame.display.update()


def quitgame():
    time.sleep(1)
    pygame.quit()
    sys.exit()

    
def helping():
    print('help')




def mainmenu():
    menu = True
    while menu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        SCREEN.fill(white)
        titletext = SCREEN.blit(titleimg, (220, 50))
        startButton = Button(startimg,305,320,60,20,clickstartimg,298,317,lobbymenu)
        quitButton = Button(quitimg,470,320,60,20,clickquitimg,465,317,quitgame)
        helpButton = Button(helpimg,370,400,100,40,clickhelpimg,370,400,helping)

        pygame.display.update()
        clock.tick(15)
    


def lobbymenu():
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    global player_1_name
    global player_2_name
    global rolled
    global turn
    global selectlist
    selectlist = [1,1,1,1,1]
    turn = 0
    rolled = 0
    player_1_name = ""
    player_2_name = ""
    input_box = pygame.Rect(240, 370, 140, 32)
    inputbox_color = gray
    inputbox_active = False
    inputbox_text = 'insert player 1 name'
    lobby = True
    inputbox_saved = 0
    input_box2 = pygame.Rect(240, 440, 140, 32)
    inputbox_color2 = gray
    inputbox_active2 = False
    inputbox_text2 = 'insert player 2 name'
    inputbox_saved2 = 0
    while lobby == True:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    inputbox_active = not inputbox_active
                    inputbox_text = ''
                else:
                    inputbox_active = False
                inputbox_color = red if inputbox_active else gray
            if event.type == pygame.KEYDOWN:
                if inputbox_active:
                    if event.key == pygame.K_RETURN:
                        player_1_name = inputbox_text
                        print(inputbox_text)
                        inputbox_color = green
                        inputbox_text = 'saved! : ' + player_1_name
                        inputbox_saved = 1
                    elif event.key == pygame.K_BACKSPACE:
                        inputbox_text = inputbox_text[:-1]
                        inputbox_saved = 0
                    elif len(inputbox_text) > 13:
                        inputbox_text = inputbox_text[:-1]
                    else:
                        inputbox_text += event.unicode
                    if inputbox_text != "" and inputbox_saved == 0:
                        inputbox_color = red

######################################################################################## player 2 input box
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box2.collidepoint(event.pos):
                    inputbox_active2 = not inputbox_active2
                    inputbox_text2 = ''
                else:
                    inputbox_active2 = False
                inputbox_color2 = red if inputbox_active2 else gray
            if event.type == pygame.KEYDOWN:
                if inputbox_active2:
                    if event.key == pygame.K_RETURN:
                        player_2_name = inputbox_text2
                        print(inputbox_text2)
                        inputbox_color2 = green
                        inputbox_text2 = 'saved! : ' + player_2_name
                        inputbox_saved2 = 1
                    elif event.key == pygame.K_BACKSPACE:
                        inputbox_text2 = inputbox_text2[:-1]
                        inputbox_saved2 = 0
                    elif len(inputbox_text2) > 13:
                        inputbox_text2 = inputbox_text2[:-1]
                    else:
                        inputbox_text2 += event.unicode
                    if inputbox_text2 != "" and inputbox_saved2 == 0:
                        inputbox_color2 = red

                        
                    
        SCREEN.fill(white)
        inputbox_txt_surface = font.render(inputbox_text, True, inputbox_color)
        inputbox_width = max(200, inputbox_txt_surface.get_width()+10)
        input_box.w = inputbox_width
        SCREEN.blit(inputbox_txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(SCREEN, inputbox_color, input_box, 2)

###############################################################################
        
        inputbox_txt_surface2 = font.render(inputbox_text2, True, inputbox_color2)
        inputbox_width2 = max(200, inputbox_txt_surface2.get_width()+10)
        input_box2.w = inputbox_width2
        SCREEN.blit(inputbox_txt_surface2, (input_box2.x+5, input_box2.y+5))
        pygame.draw.rect(SCREEN, inputbox_color2, input_box2, 2)
        
        game_start_Button = Button(game_start_buttonimg,520,300,260,260,click_game_start_buttonimg,520,300,gamestartscreen)
        backButton = Button(backimg,50,530,80,35,clickbackimg,49,529,mainmenu)
        SCREEN.blit(inp_player_1_img, (35, 360))
        SCREEN.blit(inp_player_2_img, (31, 430))
        pygame.display.update()
        clock.tick(15)

def gamestartscreen():
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + 200))
    SCREEN.fill(white)
    turnsum = 65
    p1_score = 0
    p2_score = 0

    p1_subtotal = 0
    p2_subtotal = 0

    p1_score_select = 0
    p2_score_select = 0
###########################################################
    global player_1_name
    global player_2_name
    global Drollist
    global sumwidth
    global rolled
    global turn
    oneroll = False
    oneroll2 = False
    gamestart = True
    turn = turn + 1
    while gamestart == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if player_1_name == "" and player_2_name == "":
                player_1_name = "player 1"
                player_2_name = "player 2"
            if player_1_name == "":
                player_1_name = "player 1"
            if player_2_name == "":
                player_2_name = "player 2"
        sumwidth = 10
        if oneroll2 == False:
            SCREEN.blit(dicelist_img,(325, 183))
            oneroll2 = True
        if turn > 9:
            turnsum = 35
        player_1_scoretext = mfont.render(str(p1_score),True,gray)
        player_2_scoretext = mfont.render(str(p2_score),True,red)
        turn12text = bbfont.render("/12",True,black)
        turntext = bbfont.render(str(turn),True,black)
        categoriestext = sfont.render(str("categories"),True,black)
        player1text = sfont.render(str("player 1"),True,gray)
        player2text = sfont.render(str("player 2"),True,red)

        pygame.draw.rect(SCREEN, gray, [-80,288,390,120],3)
        pygame.draw.rect(SCREEN, red, [-80,542,390,120],3)
        SCREEN.blit(s_dice1_img, (335, 254))
        SCREEN.blit(s_dice2_img, (335, 299))
        SCREEN.blit(s_dice3_img, (335, 344))
        SCREEN.blit(s_dice4_img, (335, 389))
        SCREEN.blit(s_dice5_img, (335, 434))
        SCREEN.blit(s_dice6_img, (335, 479))
        SCREEN.blit(choise_img, (335, 524))
        SCREEN.blit(fkind_img, (335, 569))
        SCREEN.blit(fhouse_img, (335, 614))
        SCREEN.blit(sstrate_img, (335, 659))
        SCREEN.blit(lstrate_img, (335, 704))
        SCREEN.blit(yacht_img, (335, 749))
        SCREEN.blit(inp_player_1_img, (10, 323))
        SCREEN.blit(inp_player_2_img, (10, 578))
        SCREEN.blit(player_1_scoretext,(215, 330))
        SCREEN.blit(player_2_scoretext,(215, 585))
        SCREEN.blit(turn12text,(135, 435))
        SCREEN.blit(turntext,(turnsum, 435))
        SCREEN.blit(categoriestext,(335, 200))
        SCREEN.blit(player1text,(510, 200))
        SCREEN.blit(player2text,(657, 200))
        exitButton = Button(exit_img,80,710,200,50,clickexit_img,80,710,lobbymenu)
        pygame.display.update()
        clock.tick(15)


        if oneroll == False:
            player_turn()
            diceroll()
            rolled = rolled + 1
            oneroll = True
            
        if rolled < 3:
            rerollButton = Button(reroll_img,50,215,200,50,clickreroll_img,50,214,gamestartscreen)
            keep()
        if rolled > 2:
            print("done")
            turnoverButton = Button(turnover_img,30,210,200,50,turnover_img,30,210,gamestartscreen)
        pygame.display.update()
        clock.tick(15)
        
    

mainmenu()
pygame.display.flip()

pygame.quit()
