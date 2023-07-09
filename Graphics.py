import pygame
from Detection import Detection
class Graphics():
    def __init__(self) -> None:
        pass

    def Draw_Board(window,x_coord,y_coord,side_length):

        x_coord_temp = x_coord
        y_coord_temp = y_coord
        rect_counter = 0
        flip = True

        window.fill((0,0,0))
        for number in range(1,33):
        
            pygame.draw.rect(window, (255,255,255), (x_coord_temp,y_coord,side_length/8,side_length/8))

            rect_counter += 1
            x_coord_temp += side_length/4
            
            if rect_counter == 4:

                y_coord += side_length/8

                if flip:
                    x_coord_temp = x_coord + (side_length/8)
                    flip = False
                else:
                    flip = True
                    x_coord_temp = x_coord
                rect_counter = 0