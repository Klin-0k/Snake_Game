import Global_definitions
import pyglet
from pyglet.window import key
import random
from MainMenuClass import MainMenu
from PlayMenuClass import PlayMenu
from GameOverMenuClass import GameOverMenu
from GameClass import Game


window = pyglet.window.Window(800, 800)
window.set_exclusive_keyboard(True)
main_menu = MainMenu(window)
play_menu = PlayMenu(window)
game_over_menu = GameOverMenu(window)
game = Game(window)
stage = 'open_main_menu'
settings_file = open("Resources/Settings.txt")
settings = []
for i in settings_file:
    settings.append(i)

game.snake_style = settings[0]


def on_draw():
    window.clear()


def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        return True


def on_close():
    settings_file.close()


window.push_handlers(on_draw, on_key_press, on_close)


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
    elif Global_definitions.stage == 'open_game_over_menu':
        game_over_menu.result_label.text = 'Your score is {}'.format(game.score)
        game_over_menu.enable = True
        Global_definitions.stage = ''
    elif Global_definitions.stage == 'play_again':
        game.reset()
        game.enable = True
        Global_definitions.stage = ''


pyglet.clock.schedule_interval(update, 1/1000000)

pyglet.app.run()
