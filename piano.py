#-*-coding:utf-8-*-
import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((650, 365))
pygame.display.set_caption('钢琴')
pygame.mouse.set_visible(True)
# 背景图
background = pygame.image.load('res/1.jpg')
# 绘制背景
screen.blit(background, (0, 0))
#初始化
pygame.display.update()

music = []
for i in range(1, 27):
    musicName = 'music (' + '%d' % (i*3) + ').wav'
    print(musicName)
    music.append(pygame.mixer.Sound(musicName))


musicHistory = []


def deleteMusic(musicNow):
    if len(musicHistory) < 5:
        musicHistory.append(musicNow)
    else:
        musicHistory.pop(0)
        musicHistory.append(musicNow)
    for i in music:
        if len(musicHistory) < 5:
            break
        else:
            if i == musicNow:
                continue
            elif i == musicHistory[0]:
                continue
            elif i == musicHistory[1]:
                continue
            elif i == musicHistory[2]:
                continue
            elif i == musicHistory[3]:
                continue
            else:
                i.stop()

key = [pygame.K_q, pygame.K_a, pygame.K_z, pygame.K_w, pygame.K_s, pygame.K_x, pygame.K_e, pygame.K_d, pygame.K_c, pygame.K_r, pygame.K_f, pygame.K_v, pygame.K_t, pygame.K_g, pygame.K_b, pygame.K_y, pygame.K_h, pygame.K_n, pygame.K_u, pygame.K_j, pygame.K_m, pygame.K_i, pygame.K_k, pygame.K_o, pygame.K_l, pygame.K_p]

def Play():
    while True:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                for k in key:
                    if k == event.key:
                        music[key.index(k)].play()
                        deleteMusic(music[key.index(k)])
                        break
    pygame.display.update()



if __name__ == '__main__':
    Play()
