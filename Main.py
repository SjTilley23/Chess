import pygame

pygame.init()
from Graphics import Graphics
from Detection import Detection

previous_click = False
Run = True
window= pygame.display.set_mode([810,810])
clock = pygame.time.Clock()

while Run:
    
    Click = pygame.mouse.get_pressed()

    # Quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False

    #Drawing and detecting
    Graphics.Draw_Board(window,5,5,800)
    Detection.square_mouse_detection(5,5,800)
    Detection.click_square(Detection, previous_click,Click[0],5,5,800)
    Graphics.draw_pieces(window,5,5,800)






    previous_click = Click[0]
    clock.tick(60)
    pygame.display.flip()
pygame.quit()