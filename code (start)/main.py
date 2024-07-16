from settings import *

class Game:
    def __init__(self):
        
        #init pygame and display
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("INSERT GAME NAME")

    #game rune function
    def run(self):
        while True:
            #event loop, able to close down game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit() 

            #game logic
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()