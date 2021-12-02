import pygame
import self as self

from dino_runner.components.Dinosaurio import Dinosaur
from .obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.text_utils import get_score_element, get_centered_message
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self. points = 0
        self. running = True
        self.death_count = 0


    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def execute(self):
        while self.running:
            if not self.playing:
               self.show_menu()
        pygame.quit()



    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self) :
        self.score()
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def score (self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed +=1
        score, score_rect = get_score_element(self.points)
        self.screen.blit(score, score_rect)

    def show_menu(self):
        self.running = True
        white_color = (255, 255, 255)
        self.screen.fill(white_color)

        self. print_menu_elements(self.death_count )


        # THE VIEW OF THE GAME IS UPDATE

        pygame.display.update()

        self.handle_key_events_on_menu()


    def print_menu_elements(self, death_count = 0):
        #THEY ARE OPTIONALS

        half_screen_height =  SCREEN_HEIGHT// 2
        half_screen_width = SCREEN_WIDTH// 2

        text, text_rect = get_centered_message("Press any key to start the game")

        self.screen.blit(text, text_rect)



    def handle_key_events_on_menu(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
