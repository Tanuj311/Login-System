import pygame
pygame.init()

WIN_WIDTH = 350
WIN_HEIGHT = 250

win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
clock = pygame.time.Clock() #clock fps

master_pass = ''  #setting up master password
again_master_pass = ''

user_input = '' #checking for master password

name = '' #saving name, email and password
email = ''
password = ''

name_open = '' #to open associated email and password 
open_pass = ''

#bool values
saving = False
chosen = False
opened = False
show = False
details = False

alpha = 'abcdefghijklmnopqrstuvwxyz' 
char_list = ['$231fs','&&9dasja',')i9auiad121%3','%q@R(@2','^A&21d','*A8@)@','UAdyaw7','%Wd5w','8d8','wa7','1310303!)!',':2w1w2','13!)#Iw','d18&:@','^W29*3t','(d!)#w1',"13O0w1w","w!i)#1d","21d!)#i",'w1)@(!#*','1w(8','&7dw!)@1dad','%W61','W&1!)#','aw819','^w1*(W!',] #used to encrypt password

a_list = [] #alphabet list
for i in alpha:
    a_list.append(i)

p_list = [] #password list
p1_list = [] #password list
p1 = '' #password string

m_list = [] #master pass list
m1_list = [] #''
m_string = '' #master pass string
m1_string = '' #''

u_list = [] #user input list 
u1_list = []
u_string = ''

open_list = [] #open password list
open1_list = [] #''
open_s = '' #open password string

def setup():
    global master_pass, again_master_pass
    pygame.draw.rect(win,(230,230,230),(55,WIN_HEIGHT-50,230,40))
    pygame.draw.rect(win, (160,160,160), (55, WIN_HEIGHT-50,230,40),3)
    setup_str = 'SET MASTER PASSWORD'
    font = pygame.font.Font(None,25)
    text = font.render(setup_str, True,(0,0,0))
    win.blit(text,(65,WIN_HEIGHT-35))

    pygame.draw.rect(win,(200,200,200), (140,50,180,30))
    pygame.draw.rect(win,(150,150,150), (140,50,180,30), 3)
    pygame.draw.rect(win, (200,200,200), (140,115,180,30))
    pygame.draw.rect(win, (150,150,150), (140,115,180,30), 3)

    text1 = font.render('PASSWORD', True, (0,0,0))
    text2 = font.render('CONFIRM', True, (0,0,0))
    win.blit(text1, (20,50))
    win.blit(text2, (20,100))
    win.blit(text1, (20,130))

    font1 = pygame.font.Font(None, 35)
    master_text = font1.render('*' * len(master_pass), True, (0,0,0))
    win.blit(master_text, (145,55))

    again_master_text = font1.render('*' * len(again_master_pass),True,(0,0,0))
    win.blit(again_master_text, (145, 120))

    text3 = font.render('CREATE MASTER PASSWORD',True,(0,0,0))
    win.blit(text3, (50,20))

def master_pass_screen():
    global master_pass, again_master_pass,m_list,m_string,a_list,m1_list
    setup()
    mouse = pygame.mouse.get_pos()
    #check for login button
    if 55 < mouse[0] < 55+ 230 and WIN_HEIGHT-50 < mouse[1] < WIN_HEIGHT-50+40:
        if master_pass == again_master_pass:
            for i in master_pass:
                m_list.append(i)
            for i in m_list:
                for x, y in enumerate(a_list):
                    if i == y:
                        i = char_list[x]
                        m1_list.append(i)
                if i not in a_list and i not in char_list:
                    m1_list.append(i)

            for j in m1_list:
                m_string+=j+'.'

            f = open('master_pass.txt', 'w')
            f.write(m_string)
            quit()
        else:
            master_pass = ''
            again_master_pass = ''
    #check for 1st password
    if 140 < mouse[0] < 140 + 180 and 50 < mouse[1] < 80:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    master_pass += event.unicode
                    if key[pygame.K_DELETE]:
                        master_pass = ''
    #check for 2nd password
    if 140 < mouse[0] < 140 + 180 and 115 < mouse[1] < 115 + 30:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    again_master_pass += event.unicode
                    if key[pygame.K_DELETE]:
                        again_master_pass = ''

def start():
    global user_input, saving,u_list,u_string,a_list,char_list,u1_list
    pygame.draw.rect(win,(230,230,230),(120,WIN_HEIGHT-50,100,40))
    pygame.draw.rect(win, (160,160,160), (120, WIN_HEIGHT-50,100,40),3)
    font = pygame.font.Font(None, 30)
    text = font.render('LOGIN', True, (0,0,0))
    win.blit(text,(135,WIN_HEIGHT-35))

    text1 = font.render('ENTER MASTER PASSWORD', True, (0,0,0))
    win.blit(text1, (40,50))

    pygame.draw.rect(win,(200,200,200), (90,100,180,30))
    pygame.draw.rect(win,(150,150,150), (90,100,180,30), 3)

    #check for user input and encode it
    mouse = pygame.mouse.get_pos()
    if 90 < mouse[0] < 90 + 180 and 100 < mouse[1] < 130:
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                user_input += event.unicode
            if key[pygame.K_DELETE]:
                user_input = ''

    font1 = pygame.font.Font(None, 35)
    user_str = font1.render('*' * len(user_input), True, (0,0,0))
    win.blit(user_str,(95,105))

    if 120 < mouse[0] < 220 and WIN_HEIGHT - 50 < mouse[1] < WIN_HEIGHT - 10:
        for i in user_input:
            u_list.append(i)
        for i in u_list:
            for x,y in enumerate(a_list):
                if i == y:
                    i = char_list[x]
                    u1_list.append(i)
            if i not in a_list and i not in char_list:
                u1_list.append(i)
        for j in u1_list:
            u_string+=j+'.'
            
        f1 = open('master_pass.txt','r')
        if u_string == f1.read():
            saving = True
        else:
            user_input = ''

def saving_page():
    global name,email,password,p1_list,p1,a_list,p_list
    font = pygame.font.Font(None,35)
    text = font.render('SAVE', True, (0,0,0))
    pygame.draw.rect(win,(230,230,230),(120,WIN_HEIGHT-50,100,40))
    pygame.draw.rect(win, (160,160,160), (120, WIN_HEIGHT-50,100,40),3)
    win.blit(text,(135,WIN_HEIGHT-40))

    pygame.draw.rect(win,(200,200,200), (115,25,220,30))
    pygame.draw.rect(win,(150,150,150), (115,25,220,30), 3)
    text1 = font.render('Name', True, (0,0,0))
    win.blit(text1, (25,30))

    pygame.draw.rect(win,(200,200,200), (115,73,220,30))
    pygame.draw.rect(win,(150,150,150), (115,73,220,30), 3)
    text1 = font.render('Email', True, (0,0,0))
    win.blit(text1, (25,78))

    pygame.draw.rect(win,(200,200,200), (115,120,220,30))
    pygame.draw.rect(win,(150,150,150), (115,120,220,30), 3)
    text1 = font.render('Password', True, (0,0,0))
    win.blit(text1, (1,125))

    #check for name input
    mouse = pygame.mouse.get_pos()
    if 115 < mouse[0] < 115 + 220 and 25 < mouse[1] < 25 + 30:
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                name += event.unicode
            if key[pygame.K_DELETE]:
                name = ''

    #check for email input
    if 115 < mouse[0] < 115 + 220 and 73 < mouse[1] < 73 + 30:
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                email += event.unicode
            if key[pygame.K_DELETE]:
                email = ''

    #check for password input
    if 115 < mouse[0] < 115 + 220 and 120 < mouse[1] < 120 + 30:
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                password += event.unicode
                
            if key[pygame.K_DELETE]:
                password = ''

    font1 = pygame.font.Font(None,30)
    name_str = font1.render(name,True,(0,0,0))
    win.blit(name_str, (120,30))

    font2 = pygame.font.Font(None,27)
    email_str = font2.render(email,True,(0,0,0))
    win.blit(email_str, (120,82))

    #encoding the password
    password_str = font1.render( '*' * len(password),True,(0,0,0))
    win.blit(password_str, (120,125))    

    key = pygame.key.get_pressed()
    if key[pygame.K_RETURN]:
        for i in password:
            p_list.append(i)

        for y, p in enumerate(p_list):    
            for x, a in enumerate(a_list):
                if a == p:
                    p = char_list[x]
                    p1_list.append(p)
            if p not in a_list and p not in char_list:
                p1_list.append(p)              

        for i in p1_list:
            p1 += i+'.'
        
        f = open('name.txt','a')
        f1 = open('email.txt','a')
        f2 = open('password.txt','a')
        f.write('\n'+name)
        f1.write('\n'+email)
        f2.write('\n'+p1)
        quit()

def open_page():
    global name_open, open_pass, show, opened,details,open_s,open_list,open1_list,a_list,char_list,m_string,m1_string

    font = pygame.font.Font(None, 30)
    pygame.draw.rect(win,(200,200,200), (115,25,220,30))
    pygame.draw.rect(win,(150,150,150), (115,25,220,30), 3)
    text = font.render('Name', True, (0,0,0))
    win.blit(text, (25,30))

    text1 = font.render('Enter Master Password', True, (0,0,0)) 
    win.blit(text1, (50,90))
    pygame.draw.rect(win,(200,200,200), (50,115,220,30))
    pygame.draw.rect(win,(150,150,150), (50,115,220,30), 3)

    name_str = font.render(name_open,True,(0,0,0))
    win.blit(name_str, (120,30))

    open_str= font.render('*'*len(open_pass),True,(0,0,0))
    win.blit(open_str, (55,120))

    pygame.draw.rect(win,(230,230,230),(100,WIN_HEIGHT-50,200,40))
    pygame.draw.rect(win, (160,160,160), (100, WIN_HEIGHT-50,200,40),3)
    text2 = font.render('SHOW DETAILS',True,(0,0,0))
    win.blit(text2, (130, WIN_HEIGHT-35))

    #checking for name input 
    mouse = pygame.mouse.get_pos()
    if 115<mouse[0] < 115 +220 and 25<mouse[1]<55:
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                name_open += event.unicode
            if key[pygame.K_DELETE]:
                name_open = ''

    #checking for master password input
    if 50<mouse[0] <50+ 220 and 115<mouse[1]<115+30:
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                open_pass += event.unicode 
            if key[pygame.K_DELETE]:
                open_pass = ''


    key = pygame.key.get_pressed()
    if key[pygame.K_RETURN]:

        #decrypting password
        master_p = open('master_pass.txt', 'r')
        m_p = master_p.readlines()
        l = len(m_p)
        for i in m_p:
            if len(m_string) < l:
                m_string+=i

        ms = m_string.split('.')

        for x in ms:
            for i,j in enumerate(char_list):
                if j == x:
                    x = a_list[i]
                    if len(m1_string) < len(ms) - 1:
                        m1_string+=x
            if x not in char_list and x not in a_list:
                if len(m1_string) < len(ms) - 1:
                    m1_string+= x

        show = True
        details = True

    if show:
        file1 = open('name.txt','r')
        f1 = file1.readlines()
        for x,name in enumerate(f1):
            if name != f1[-1]:
                if name_open+"\n" == name and open_pass == m1_string:
                    return x
            else:
                if name_open == name and open_pass == m1_string:
                    return x
        else:
            name_open = ''
            open_pass = ''
                 
def choose():
    global chosen, opened
    pygame.draw.rect(win,(230,230,230),(120,50,100,40))
    pygame.draw.rect(win, (160,160,160), (120,50,100,40),3)
    font = pygame.font.Font(None, 35)
    text = font.render('OPEN', True, (0,0,0))
    win.blit(text, (135,55))

    pygame.draw.rect(win,(230,230,230),(120,150,100,40))
    pygame.draw.rect(win, (160,160,160), (120,150,100,40),3)
    text1 = font.render('SAVE', True,(0,0,0))
    win.blit(text1, (135,155))

    mouse = pygame.mouse.get_pos()
    if 120 < mouse[0] < 220 and 50 < mouse[1] < 90:
        if pygame.mouse.get_pressed():
            opened = True

    if 120 < mouse[0] < 220 and 150 < mouse[1] < 190:
        if pygame.mouse.get_pressed():    
            chosen = True

while True: 
    clock.tick(100)
    f1 = open('master_pass.txt', 'r')
    win.fill((255,255,255))
    if f1.read() == '':
        master_pass_screen()
        pygame.display.set_caption('CREATE MASTER PASSWORD')

    elif saving == False:
        start()
        pygame.display.set_caption('LOGIN SCREEN')

    if saving == True and chosen == False and opened== False:
        choose()      
        pygame.display.set_caption('CHOOSE')

    if chosen:  
        saving_page()
        pygame.display.set_caption('SAVING PAGE')

    if opened and details == False and show == False:
        open_page()
        pygame.display.set_caption('OPENING PAGE')

    if details:
        x1 = open_page()
        pygame.display.set_caption('DETAILS')
        if x1 != None:
            win.fill((255,255,255))
            file2 = open('email.txt','r')
            f2 = file2.readlines()
            font = pygame.font.Font(None, 30)
            email_str = font.render(f'EMAIL: {f2[x1]}', True, (0,0,0))
            win.blit(email_str, (20,50))

            file3 = open('password.txt','r')
            f3 = file3.readlines() 
            p_split = f3[x1].split('.')
            p_string = ''

            for x,p in enumerate(p_split):
                for y,i in enumerate(char_list):
                    if p == i:
                        p = a_list[y]
                        p_string+=p
                if p not in char_list and p not in a_list:
                    p = p
                    p_string += p 

            pass_str = font.render(f'PASSWORD: {p_string}', True, (0,0,0))
            win.blit(pass_str, (20,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.update()
  