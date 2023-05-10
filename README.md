# Python_2023_Project_1
## About: 
This is the snake game that has two modes in current time: classic mode and upgrade classic mode.
Classic mode is classic snake game in which you should eat food to grow up and get score. Aim of the game is to get as much score as possible.
Upgraded Classic mode has the same aim of the game, but there are bonuses that can help or interfere you to play it: 
1) syringe - bonus that makes snake two times faster than it was and gives you two score points
2) tablet - bonus that makes snake two times slower than it was
3) knife - bonus that takes out half of your scores and make snake two times shorter than it was.

All games results are recording and saving in Resources/Records.txt file, but in current time you can't watch them from the game 

Also the game has settings in which you can change snake style, field style and field size

Navigation in game menus is done using the mouse. The snake is controlled using the wasd or arrows
## How to run:
Clone this repository, make sure you have the pyglet library installed and run main.py

You can also compile the code into an executable file (for this you need to first install pyinstaller, you can do this with the command: `pip install pyinstaller`):

   Run the command: `pyinstaller .\Python_2023_Project_1.spec`

   In this case, two folders **build** and **dist** will be created, the executable file will be placed in the **dist** folder, however, it will no longer be linked to any files in the folder and you can move it to any convenient place and run it from anywhere. In theory, this method should work for all operating systems, however, in practice, when I tried to run the file generated for unix systems on wsl, I got an error, when running the executable file generated under windows, no errors should occur