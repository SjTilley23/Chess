import pygame

class Detection():
    def __init__(self) -> None:
        pass
    
    def board_state( x_coord, y_coord,side_length):
        board_state = []
        row_counter = 0
        
        for i in range(0,64):

            #Generates horizontal detection zone in pixels
            i_temp = int((i/8))
            lower_x_bound = (x_coord + ((i-((i_temp)*8))*(side_length/8)))
            
            upper_x_bound = lower_x_bound+(side_length/8)

            board_state.append(lower_x_bound)
            board_state.append(upper_x_bound)
            
            #generates vertical detection zone in pixels
            if i % 8 == 0:
                row_counter += 1

            lower_y_bound = (y_coord + ((row_counter-1)*(side_length/8)))
            upper_y_bound = lower_y_bound + (side_length/8)
            
            board_state.append(lower_y_bound)
            board_state.append(upper_y_bound)

            #is a piece on the board
            board_state.append(False)

            #What piece is in that spot
            board_state.append("None")

        return board_state
    
    def mouse_detection(self,x_coord,y_coord,side_length):
        board_state = self.board_state(x_coord, y_coord,side_length)
        
        for i in range(0,(64*6)):
            if i % 6 == 0:
                if (pygame.mouse.get_pos()[0] > board_state[i] and pygame.mouse.get_pos()[0] < board_state[i+1]
                    and pygame.mouse.get_pos()[1] > board_state[i+2] and pygame.mouse.get_pos()[1] < board_state[i+3]):
                        return int(i/6)
                
        
