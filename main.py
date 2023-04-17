import Global_definitions
import pyglet
from pyglet.window import key
import random
from MainMenuClass import MainMenu
from PlayMenuClass import PlayMenu
from GameOverMenuClass import GameOverMenu
from GameClass import Game
from InGameMenuClass import InGameMenu
from SettingsClass import Settings

window = pyglet.window.Window(800, 800)
window.set_exclusive_keyboard(True)
settings = Settings(window)
main_menu = MainMenu(window)
play_menu = PlayMenu(window)
game_over_menu = GameOverMenu(window)
in_game_menu = InGameMenu(window)
game = Game(window)
stage = 'open_main_menu'


def on_draw():
    window.clear()


window.push_handlers(on_draw)


def update(dt):
    if Global_definitions.stage == 'open_main_menu':
        main_menu.enable = True
        Global_definitions.stage = ''
    elif Global_definitions.stage == 'open_play_menu':
        play_menu.enable = True
        Global_definitions.stage = ''
    elif Global_definitions.stage == 'open_classic_snake':
        game.reset()
        game.game_mode = 'classic'
        game.enable = True
        Global_definitions.stage = ''
    elif Global_definitions.stage == 'open_upgraded_classic_snake':
        game.reset()
        game.game_mode = 'upgraded_classic'
        game.enable = True
        Global_definitions.stage = ''
    elif Global_definitions.stage == 'open_game_over_menu':
        game_over_menu.result_label.text = 'Your score is {}'.format(game.score)
        game_over_menu.enable = True
        Global_definitions.stage = ''
    elif Global_definitions.stage == 'play_again':
        game.reset()
        game.enable = True
        Global_definitions.stage = ''
    elif Global_definitions.stage == 'open_in_game_menu':
        in_game_menu.enable = True
    elif Global_definitions.stage == 'close_in_game_menu':
        in_game_menu.visible = False
        if not game_over_menu.visible:
            game.enable = True
    elif Global_definitions.stage == 'open_settings':
        settings.enable = True


pyglet.clock.schedule_interval(update, 1/1000000)

pyglet.app.run()
