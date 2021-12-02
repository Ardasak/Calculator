import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
process = False
Font = pygame.font.Font(None,50)
Font1 = pygame.font.Font(None,30)
text = ''
Rect = pygame.Rect(200,200,140,32)
pygame.display.set_caption("Hesap Makinesi")
color_active = (170,130,190)
color_passive = (60,60,60)
active = False
color = color_passive
number1 =Font.render("1",1,(0,0,0))
number2 = Font.render("2",1,(0,0,0))
number3 = Font.render("3",1,(0,0,0))
number4 = Font.render("4",1,(0,0,0))
number5 = Font.render("5",1,(0,0,0))
number6 = Font.render("6",1,(0,0,0))
number7 = Font.render("7",1,(0,0,0))
number8 = Font.render("8",1,(0,0,0))
number9 = Font.render("9",1,(0,0,0))
number10 = Font.render("0",1,(0,0,0))
sign1 = Font.render("+",1,(0,0,0))
sign2 = Font.render("-",1,(0,0,0))
sign3 = Font.render("*",1,(0,0,0))
sign4 = Font.render("/",1,(0,0,0))
text1 = Font1.render("Sil",1,(0,0,0))
text2=Font1.render("Yap",1,(0,0,0))

Rect1 = pygame.Rect(200,233,50,50)
Rect2 = pygame.Rect(251,233,50,50)
Rect3 = pygame.Rect(302,233,50,50)
Rect4 = pygame.Rect(353,233,50,50)
Rect5 = pygame.Rect(200,284,50,50)
Rect6 = pygame.Rect(251,284,50,50)
Rect7 = pygame.Rect(302,284,50,50)
Rect8 = pygame.Rect(353,284,50,50)
Rect9 = pygame.Rect(200,335,50,50)
Rect10 = pygame.Rect(251,335,50,50)
Rect11=pygame.Rect(302,335,50,50)
Rect12=pygame.Rect(353,335,50,50)
Rect13=pygame.Rect(200,386,50,50)
Rect14=pygame.Rect(251,386,50,50)
Rect15=pygame.Rect(302,386,50,50)
Rect16=pygame.Rect(353,386,50,50)
text3=Font1.render("",1,(255,255,255))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            try:
                if Rect1.collidepoint(event.pos):
                    text+='+'
                    process = False
                    text3 = Font1.render("", 1, (255, 255, 255))
                elif Rect2.collidepoint(event.pos):
                    text+='-'
                    process = False
                    text3 = Font1.render("", 1, (255, 255, 255))
                elif Rect3.collidepoint(event.pos):
                    text+='*'
                    process = False
                    text3 = Font1.render("", 1, (255, 255, 255))
                elif Rect4.collidepoint(event.pos):
                    text+='/'
                    process = False
                    text3 = Font1.render("", 1, (255, 255, 255))
                elif Rect5.collidepoint(event.pos):
                    text+='1'
                    process = False
                    text3 = Font1.render("", 1, (255, 255, 255))
                elif Rect6.collidepoint(event.pos):
                    text+='2'
                    process = False
                    text3 = Font1.render("", 1, (255, 255, 255))
                elif Rect7.collidepoint(event.pos):
                    text+='3'
                    process = False
                    text3 = Font1.render("", 1, (255, 255, 255))
                elif Rect8.collidepoint(event.pos):
                    text+='4'
                    process = False
                    text3 = Font1.render("", 1, (255, 255, 255))
                if Rect9.collidepoint(event.pos):
                    text+='5'
                    process = False
                    text3 = Font1.render("", 1, (255, 255, 255))
                if Rect10.collidepoint(event.pos):
                    text+='6'
                    process = False
                    text3 = Font1.render("", 1, (255, 255, 255))
                if Rect11.collidepoint(event.pos):
                    text+='7'
                    process = False
                    text3 = Font1.render("", 1, (255, 255, 255))
                if Rect12.collidepoint(event.pos):
                    text+='8'
                    process = False
                    text3 = Font1.render("", 1, (255, 255, 255))
                if Rect13.collidepoint(event.pos):
                    text+='9'
                    process = False
                    text3 = Font1.render("", 1, (255, 255, 255))
                if Rect14.collidepoint(event.pos):
                    text+='0'
                    process = False
                    text3 = Font1.render("", 1, (255, 255, 255))
                if Rect15.collidepoint(event.pos):
                    text = text[:-1]
                    process = False
                    text3 = Font1.render("", 1, (255, 255, 255))
                if Rect16.collidepoint(event.pos):
                    process = True

                    a = eval(text)
                    a = str(a)
                    text=''
                    text3 = Font1.render(a,1,(0,0,0))
            except:
                if len(text) == 0:
                    pass
                else:
                    process = True
                    text=''
                    text3 = Font1.render("Hata", 1, (0, 0, 0))


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
                process = False
                text3 = Font1.render("",1,(255,255,255))
            elif event.key == pygame.K_RETURN:
                process = True

                a = eval(text)
                a = str(a)
                text = ''
                text3 = Font1.render(a, 1, (0, 0, 0))

    screen.fill((255,255,255))
    pygame.draw.rect(screen,color,Rect,2)
    pygame.draw.rect(screen,color_active,Rect1,2)
    pygame.draw.rect(screen, color_active, Rect4, 2)
    pygame.draw.rect(screen, color_active, Rect3, 2)
    pygame.draw.rect(screen, color_active, Rect2, 2)
    pygame.draw.rect(screen, color_active, Rect5, 2)
    pygame.draw.rect(screen, color_active, Rect6, 2)
    pygame.draw.rect(screen, color_active, Rect7, 2)
    pygame.draw.rect(screen, color_active, Rect8, 2)
    pygame.draw.rect(screen, color_active, Rect9, 2)
    pygame.draw.rect(screen, color_active, Rect10, 2)
    pygame.draw.rect(screen, color_active, Rect11, 2)
    pygame.draw.rect(screen, color_active, Rect12, 2)
    pygame.draw.rect(screen, color_active, Rect13, 2)
    pygame.draw.rect(screen, color_active, Rect14, 2)
    pygame.draw.rect(screen, color_active, Rect15, 2)
    pygame.draw.rect(screen, color_active, Rect16, 2)
    screen.blit(sign1,(Rect1.x + 15,Rect1.y+5))
    screen.blit(sign2,(Rect2.x + 15,Rect2.y+5))
    screen.blit(sign3,(Rect3.x + 15,Rect3.y+10))
    screen.blit(sign4,(Rect4.x + 15,Rect4.y+5))
    screen.blit(number1, (Rect5.x + 15, Rect5.y + 5))
    screen.blit(number2, (Rect6.x + 15, Rect6.y + 5))
    screen.blit(number3, (Rect7.x + 15, Rect7.y + 5))
    screen.blit(number4, (Rect8.x + 15, Rect8.y + 5))
    screen.blit(number5, (Rect9.x + 15, Rect9.y + 5))
    screen.blit(number6, (Rect10.x + 15, Rect10.y + 5))
    screen.blit(number7, (Rect11.x + 15, Rect11.y + 5))
    screen.blit(number8, (Rect12.x + 15, Rect12.y + 5))
    screen.blit(number9, (Rect13.x + 15, Rect13.y + 5))
    screen.blit(number10, (Rect14.x + 15, Rect14.y + 5))
    screen.blit(text1, (Rect15.x + 10, Rect15.y + 15))
    screen.blit(text2, (Rect16.x + 10, Rect16.y + 15))
    if process:
        screen.blit(text3,(205,205))
    text_surface = Font1.render(text,1,(0,0,0))
    screen.blit(text_surface,(205,205))
    Rect.w = max(203, text_surface.get_width()+10,text3.get_width()+10)
    pygame.display.flip()
