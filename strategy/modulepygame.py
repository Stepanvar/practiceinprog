import pygame as pg
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
key_dict = {pg.K_k:BLACK, pg.K_r:RED, pg.K_g:GREEN, pg.K_b:BLUE,
pg.K_y:YELLOW, pg.K_c:CYAN, pg.K_m:MAGENTA, pg.K_l:WHITE}
pg.init()
running = True
sc = pg.display.set_mode((920, 600), pg.RESIZABLE)
gameIcon = pg.image.load("C:\\Users\\user\\vscode\\practiceinprog\\strategy\\images\\aliance.png")
background = GRAY
card = pg.image.load("C:\\Users\\user\\vscode\\practiceinprog\\strategy\\images\\orda.png")
while (running):
	for event in pg.event.get():
		if (event.type == pg.QUIT):
			running = False
		elif (event.type == pg.KEYDOWN):
			if (event.key in key_dict):
				background = key_dict[event.key]
				caption = "background color is " + str(background)
				pg.display.set_caption(caption)
		pg.display.set_icon(gameIcon)
		sc.fill(background)
		# pg.draw.rect(sc, WHITE, rect, 1)
		# sc.blit(rect, (50, 50))
		pg.time.delay(66)
		pg.draw.rect(sc, (0, 0, 0), (80, 80, 160, 160))
		pg.draw.circle(sc, (250, 0, 0), (400, 250), 75)
		pg.display.update()

