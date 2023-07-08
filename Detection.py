import pygame

class Detection():
    def __init__(self) -> None:
        pass

    def square_mouse_detection(x_coord,y_coord,side_length):
        position = pygame.mouse.get_pos()
        
        x_coord_temp = x_coord
        y_coord_temp = y_coord
        column_numbers = [1,2,3,4,5,6,7,8]

        #Gives which column
        current_rounded_x = int(position[0]/(side_length/8))
        
        #Gives which row
        current_rounded_y = int(position[1]/(side_length/8))

        current_row = current_rounded_y + 1
        current_column = current_rounded_x + 1

        current_square = (current_column, current_row)
        return current_square
        
    def click_square(self, previous_click, current_click,y_coord,x_coord,side_length):
        current_square = self.square_mouse_detection(x_coord,y_coord,side_length)

        if previous_click == False and current_click:
            print(current_square)
    
