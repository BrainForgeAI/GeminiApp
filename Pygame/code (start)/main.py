import pygame
import asyncio
from settings import *
from game_data import *
from pytmx.util_pygame import load_pygame
from os.path import join

from sprites import Sprite
from entities import Player, Character
from groups import AllSprites
from support import *
from dialog import DialogTree

# Global variables
COUNT_DOWN = 3000000000

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("INSERT GAME NAME")
        self.clock = pygame.time.Clock()
        self.all_sprites = AllSprites()
        self.character_sprites = pygame.sprite.Group()
        self.import_assets()
        self.setup(self.tmx_maps['world'], 'home')
        self.dialog_tree = None

    def import_assets(self):
        self.tmx_maps = {'world': load_pygame(join('data', 'maps', 'basemap.tmx'))}
        self.overworld_frames = {
            'characters': all_character_import('graphics', 'characters')
        }
        self.fonts = {
            'dialog': pygame.font.Font(join('graphics', 'fonts', 'PixeloidSans.ttf'))
        }
    
    def setup(self, tmx_map, player_start_pos):
        for x, y, surf in tmx_map.get_layer_by_name("Terrain").tiles():
            Sprite((x*TILE_SIZE, y*TILE_SIZE), surf, self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                if obj.properties['pos'] == player_start_pos:
                    self.player = Player(
                        pos = (obj.x, obj.y), 
                        frames = self.overworld_frames['characters']['young_guy'],
                        groups = self.all_sprites,
                        facing_direction = obj.properties['direction'])
            else:
                Character(
                    pos = (obj.x, obj.y), 
                    frames = self.overworld_frames['characters'][obj.properties['graphic']],
                    groups = (self.all_sprites, self.character_sprites),
                    facing_direction = obj.properties['direction'],
                    character_data = TRAINER_DATA[obj.properties['character_id']]
                )

    def input(self):
        if not self.dialog_tree:
            keys = pygame.key.get_just_pressed()
            if keys[pygame.K_SPACE]:
                for character in self.character_sprites:
                    if check_connections(100, self.player, character):
                        self.player.block()
                        character.change_facing_direction(self.player.rect.center)
                        self.create_dialog(character)

    def create_dialog(self, character):
        if not self.dialog_tree:
            self.dialog_tree = DialogTree(character, self.player, self.all_sprites, self.fonts['dialog'], self.end_dialog)

    def end_dialog(self, character):
        self.dialog_tree = None
        self.player.unblock()

    async def run(self):
        global COUNT_DOWN
        while True:
            dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.input()
            self.all_sprites.update(dt)
            self.display_surface.fill('black')
            self.all_sprites.draw(self.player.rect.center)
            if self.dialog_tree: 
                self.dialog_tree.update()

            print(f"\n\nHello[{COUNT_DOWN}] from Python\n")
            pygame.display.update()

            await asyncio.sleep(0)

            if not COUNT_DOWN:
                return

            COUNT_DOWN -= 1

async def main():
    game = Game()
    await game.run()

# Program entry point
asyncio.run(main())