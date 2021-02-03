# cesar godoy
import pygame, gamebox, random
camera = gamebox.Camera(800, 600)
# movables
ball = gamebox.from_image(400, 500, 'images/bola.png')
ball.scale_by(0.03)
gloves1 = gamebox.from_image(400, 400, 'images/luva.png')
gloves2 = gamebox.from_image(400, 400, 'images/luva.png')
gloves2.scale_by(0.128)
gloves1.scale_by(0.128)
# scenary
background = [gamebox.from_image(400, 300, 'images/estadio.jpg')]
flafans1 = gamebox.from_image(650, 250, 'images/urubu.png')
flafans1.scale_by(0.7)
emblema_fla = gamebox.from_image(680, 400, 'images/emblema_fla.png')
emblema_fla.scale_by(0.6)
riverfans1 = gamebox.from_image(150, 280, 'images/river_mascote.png')
riverfans1.scale_by(0.18)
emblema_river = gamebox.from_image(180, 400, 'images/emblema_river.png')
emblema_river.scale_by(0.25)
grefans1 = gamebox.from_image(150, 265, 'images/gremio_mascote.png')
emblema_gre = gamebox.from_image(180, 400, 'images/emblema_gre.png')
emblema_gre.scale_by(0.24)
# teams
fla = [flafans1, emblema_fla]
riv = [riverfans1, emblema_river, "FLA 2", "RIV "]
gre = [grefans1, emblema_gre, "FLA 6", "GRE "]
def StartScreen():
    '''
    builds the front screen
    '''
    x = 15
    start_screen = gamebox.from_image(400, 300, 'images/flamengo.jpg')
    start_screen.scale_by(0.8)
    camera.draw(start_screen)
    camera.draw(gamebox.from_text(400, 100, "LIBERTADORES DA AMERICA", 50, 'red', bold=True))
    camera.draw(gamebox.from_text(400, 130, "2019", 50, 'red', bold=True))
    camera.draw(gamebox.from_text(650, 450, 'By: Cesar A Godoy', 20, 'red'))
    camera.draw(gamebox.from_text(124, 210, 'GOAL', 20, 'red', bold=True))
    camera.draw(gamebox.from_text(124, 210 + x, 'Don’t let the other team win!', 20, 'red'))
    camera.draw(gamebox.from_text(124, 210 + 2 * x, 'use the arrow keys to', 20, 'red'))
    camera.draw(gamebox.from_text(124, 210 + 3 * x, 'Block the ball!', 20, 'red'))
    camera.draw(gamebox.from_text(124, 210 + 4 * x, 'Use the keys W S D A', 20, 'red'))
    camera.draw(gamebox.from_text(124, 210 + 5 * x, 'To control the second glove', 20, 'red'))
    camera.draw(gamebox.from_text(124, 210 + 6 * x, 'in multiplayer', 20, 'red'))
    camera.draw(gamebox.from_text(128, 210 + 8 * x, 'INSTRUCTIONS', 25, 'white', bold=True))
    camera.draw(gamebox.from_text(128, 210 + 9 * x, 'press key B to continue', 25, 'white'))
    camera.draw(gamebox.from_text(686, 210, 'Backstory', 20, 'red', bold=True))
    camera.draw(gamebox.from_text(686, 210 + x, 'Flamengo won the', 20, 'red'))
    camera.draw(gamebox.from_text(686, 210 + 2 * x, 'Libertadores Cup 2019', 20, 'red'))
    camera.draw(gamebox.from_text(686, 210 + 3 * x, '2 x 1 against River Plate !', 20, 'red'))
    camera.draw(gamebox.from_text(686, 210 + 4 * x, 'This is a celebratory game', 20, 'red'))
    camera.draw(gamebox.from_text(686, 210 + 5 * x, 'That gives you the chance', 20, 'red'))
    camera.draw(gamebox.from_text(686, 210 + 6 * x, "to impersonate Latin", 20, 'red'))
    camera.draw(gamebox.from_text(686, 210 + 7 * x, "America's best goal keeper", 20, 'red'))
    camera.draw(gamebox.from_text(686, 210 + 8 * x, "and help Flamengo conquer", 20, 'red'))
    camera.draw(gamebox.from_text(686, 210 + 9 * x, "this title for the first", 20, 'red'))
    camera.draw(gamebox.from_text(686, 210 + 10 * x, "time in 38 years !!", 20, 'red'))
def MenuScreen():
    '''
    builds the menu
    '''
    global adversary
    camera.draw(gamebox.from_text(400, 100, "LIBERTADORES DA AMERICA", 50, 'red', bold=True))
    camera.draw(gamebox.from_text(400, 130, "2019", 50, 'red', bold=True))
    camera.draw(gamebox.from_text(400, 170, "use your mouse to hover over the settings", 30, 'red', bold=True))
    camera.draw(gamebox.from_text(200, 210, 'DIFFICULTY', 35, 'red', bold=True))
    if game_mode=="easy":
        camera.draw(gamebox.from_text(200, 235, 'EASY', 30, 'white', bold=True))
        camera.draw(gamebox.from_text(200, 255, 'HARD', 30, 'red', bold=True))
    else:
        camera.draw(gamebox.from_text(200, 235, 'EASY', 30, 'red', bold=True))
        camera.draw(gamebox.from_text(200, 255, 'HARD', 30, 'white', bold=True))
    camera.draw(gamebox.from_text(200, 295, 'NUMBER OF PLAYERS', 35, 'red', bold=True))
    if glove_on:
        camera.draw(gamebox.from_text(200, 320, 'ONE', 30, 'red', bold=True))
        camera.draw(gamebox.from_text(200, 340, 'TWO', 30, 'white', bold=True))
    else:
        camera.draw(gamebox.from_text(200, 320, 'ONE', 30, 'white', bold=True))
        camera.draw(gamebox.from_text(200, 340, 'TWO', 30, 'red', bold=True))
    camera.draw(gamebox.from_text(600, 210, 'ADVERSARY', 35, 'red', bold=True))
    if adversary == riv:
        camera.draw(gamebox.from_text(600, 250, 'RIVER PLATE(final)', 30, 'white', bold=True))
        camera.draw(gamebox.from_text(600, 280, 'GREMIO(semi-final)', 30, 'red', bold=True))
    elif adversary == gre:
        camera.draw(gamebox.from_text(600, 250, 'RIVER PLATE(final)', 30, 'red', bold=True))
        camera.draw(gamebox.from_text(600, 280, 'GREMIO(semi-final)', 30, 'white', bold=True))
    fin = open("score.txt","r")
    camera.draw(gamebox.from_text(400, 400, "wins: "+str(fin.readline().strip()), 20, 'red', bold=True)) #shows how many times you've won
    camera.draw(gamebox.from_text(400, 420, "losses: "+str(fin.readline().strip()), 20, 'red', bold=True))#shows how many times you've lost
    fin.close()
    camera.draw(gamebox.from_text(400, 500, 'PRESS "S" TO CONTINUE', 35, 'red', bold=True))
def Scenary(adv_team):
    '''
    builds a scenary, given the adversary's info
    '''
    return background + fla + adv_team
def Restart():
    '''
    sets all variables that may change throughout the game
    its necessary to restart them to play again
    '''
    global timer, game_on, other_score, game_mode, timer, ball_speed, glove_speed, ball_direction, glove_on, menu, ready, adversary, scale, double_counting
    timer = 0
    game_on = 0
    ready = 0
    adversary = riv
    other_score = 0
    game_mode = 0
    glove_on = 0
    menu = 0
    ball_speed = 5
    scale = 0.9
    glove_speed = 15
    ball_direction = 0
    ball.x = 400
    ball.y = 500
    ball.full_size()
    ball.scale_by(0.03)
    double_counting = False #stop double counting victories and losses for the leadboard
def move_gloves(glove, keys, arr):
    '''
    :param glove: glove object
    :param keys: keyboard keys
    :param arr: keys that will define movement
    defines how gloves can move
    '''
    if arr[0] in keys:
        glove.x += glove_speed
    if arr[1] in keys:
        glove.x -= glove_speed
    if arr[2] in keys:
        glove.y += glove_speed
    if arr[3] in keys:
        glove.y -= glove_speed
    if glove.y >= 450:
        glove.y = 450
    if glove.y <= 350:
        glove.y = 350
def move_ball():
    '''
    defines ball movements
    '''
    global game_on, other_score, ball_direction, timer, ball_speed, scale
    if game_on:
        ball.move_speed()
        ball.scale_by(scale)
        ball.x += ball_direction
        ball.y -= ball_speed
        if ball.width < 25.5:
            if game_on and not ball.touches(gloves1) and not ball.touches(gloves2) and ball.y > 358 and ball.x > 285 and ball.x < 520 and ball.y < 500:
                other_score += 1
            ball.x = 400
            ball.y = 500
            ball.full_size()
            ball.scale_by(0.03)
            if game_mode == "easy":
                scale = 0.96
                ball_speed = [i for i in range(1, 5)][random.randint(0, 3)]
                ball_direction = [random.gauss(-2, 1.5), random.gauss(2, 1.5)][random.randint(0, 1)]
            else:
                scale = 0.93
                ball_speed = [i for i in range(2, 10)][random.randint(0, 7)]
                ball_direction = [random.gauss(-2, 2), random.gauss(2, 2)][random.randint(0, 1)]
            pygame.time.delay(50)
def draw(keys, adversary):
    '''
    draws everything: the scenary, the field, the emblems, the gloves, the ball.
    '''
    global game_mode
    for box in Scenary(adversary)[0:5]:
        camera.draw(box)
    camera.draw(gamebox.from_text(300, 50, Scenary(adversary)[6] + str(other_score), 50, "white", bold=True))
    camera.draw(gamebox.from_text(500, 50, Scenary(adversary)[5], 50, "red", bold=True))
    camera.draw(gamebox.from_text(700, 50, str(round(timer)), 40, "red"))
    arr1 = [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_DOWN, pygame.K_UP]
    arr2 = [pygame.K_d, pygame.K_a, pygame.K_s, pygame.K_w]
    move_gloves(gloves1, keys, arr1)
    move_ball()
    camera.draw(gloves1)
    if glove_on:
        camera.draw(gloves2)
        move_gloves(gloves2, keys, arr2)
    if not game_on:
        camera.draw(gamebox.from_text(400, 300, 'Press spacebar to start', 50, 'red'))
    camera.draw(ball)
def GameMode(keys):
    '''
    user input. defines game_mode(easy or hard), adversary...
    '''
    global game_mode, glove_on, menu, adversary, ready
    mouse = pygame.mouse.get_pos()
    if not game_on:
        if pygame.K_b in keys:
            menu = 1
    if menu:
        if 240 > mouse[0] > 160 and 330 > mouse[1] > 305:
            glove_on = 0
        elif 240 > mouse[0] > 160 and 355 > mouse[1] > 330:
            glove_on = 1
        if 240 > mouse[0] > 160 and 245 > mouse[1] > 220:
            game_mode = "easy"
        elif 240 > mouse[0] > 160 and 270 > mouse[1] > 245:
            game_mode = "hard"
        if 720 > mouse[0] > 480 and 265 > mouse[1] > 235:
            adversary = riv
        if 720 > mouse[0] > 480 and 295 > mouse[1] > 265:
            adversary = gre
        if pygame.K_s in keys:
            ready = 1
            menu = 0
def Timer(keys):
    '''
    user input for when to start shooting
    increments timer
    '''
    global game_on, timer
    if pygame.K_SPACE in keys:
        game_on = 1
    if game_on:
        timer += 0.3
def GameOver(keys, adversary):
    '''
    deals with everything once game is over: incrementing one point to either wins or losses on the scoreboard, call Restart() and prompt user to restart the game
    '''
    global game_on, menu, double_counting
    if int(Scenary(adversary)[5][-1]) <= other_score:
        camera.draw(gamebox.from_text(400, 300, "YOU ARE DEEMED UNWORTHY OF REPRESENTING FLAMENGO!", 35, 'red'))
        if not double_counting:
            double_counting = True
            fin = open("score.txt", "r")
            wins = fin.readline().strip()
            losses = int(fin.readline().strip())
            fin.close()
            with open("score.txt", "w") as fout:
                fout.write(wins+"\n"+str(losses+1))
            fout.close()
    else:
        camera.draw(gamebox.from_text(400, 300, "YOU ARE DEEMED WORTHY OF REPRESENTING FLAMENGO!", 35, 'red'))
        if not double_counting:
            double_counting = True
            fin = open("score.txt","r")
            wins = int(fin.readline())
            losses = fin.readline().strip()
            fin.close()
            with open("score.txt","w") as fout:
                fout.write(str(wins+1)+"\n"+losses)
            fout.close()
    camera.draw(gamebox.from_text(400, 370, "press spacebar to go back to menu", 35, 'red'))
    if pygame.K_SPACE in keys:
        Restart()
        menu = 1
        MenuScreen()
Restart()
def tick(keys):
    '''
    runs the game
    '''
    global game_on, game_mode, timer, menu, adversary, ready
    StartScreen()
    GameMode(keys)
    if menu:
        camera.clear("black")
        MenuScreen()
    if ready:
        Timer(keys)#global adversary
        draw(keys, adversary)
    if round(timer) > 89:
        camera.clear("black")
        game_on = 0
        GameOver(keys, adversary)#global adversary
    camera.display()
gamebox.timer_loop(40, tick)