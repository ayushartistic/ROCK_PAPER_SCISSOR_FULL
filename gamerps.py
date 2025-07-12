import time
import os
import sys
import random
import pygame
pygame.mixer.init()

if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
else:
    app_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(app_path)

def filemaker(tcontent):
    with open("Score_Card.txt", "w") as f:
        f.write(tcontent)

def typeeffect(txt):
    for ch in txt:
        print(ch, end='', flush=True)
        time.sleep(0.1)

def play_effect(path, volume=1.0):
    try:
        effect = pygame.mixer.Sound(path)
        effect.set_volume(volume)
        effect.play()
    except Exception as e:
        print(f"Error playing sound effect: {e}")

def play_music(path, volume, loop=-1):

    
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(volume)  # 0.0 to 1.0
    pygame.mixer.music.play(loop)  # -1 means loop forever

def rps(rounds,score,c,name):
    if rounds <= 0:
        rounds = 1
    
    playerscore = 0
    drawscore = 0
    ayushscore = 0
    l = ["r", "p", "s"]
    win = [("r","s"),("p","r"),("s","p")]
    loss =[("s","r"),("r","p"),("p","s")]
    draw = [("r","r"),("p","p"),("s","s")]
    while c < rounds:
        print(f"\nRound {c + 1} of {rounds}")  
        
        r = input("Enter your choice (r/p/s): ")
        play_effect(resource_path("gunshot.wav"))
        ai = random.choice(l)
        r=r.lower().strip()
            
        if((r in l)):
            print(f"Your choice: {r}")
            print("Ayush is throwing...")
            for i in [3,2,1]:
                    print(i)
                    time.sleep(1)
            play_effect(resource_path("gunshot.wav"))
            print(f"Ayush choice: {ai}")
            
            if((r,ai) in win):
                    print("You win!")
                    play_effect(resource_path("win.wav"))
                    playerscore += 1
                    c += 1
                
            elif((r,ai) in loss):
                    print("You lost, try again!")
                    play_effect(resource_path("loss.wav"))
                    ayushscore += 1
                    c += 1

            else:
                    print("Draw match, try again!")
                    play_effect(resource_path("loss.wav"))
                    drawscore += 1
                    c += 1
        else:
            print("Wrong input, try again!")
    
    content = f"Game of {rounds} rounds is Over!\n{name} score: {playerscore}/{rounds}\nAyush score: {ayushscore}/{rounds}\nDraws: {drawscore}/{rounds}"

    print("\nGame Over! Generating Final Scores:")
    for i in [3,2,1]:
        print(i)
        time.sleep(1)
    play_effect(resource_path("victory.wav"))
    filemaker(content)
    print()
    print("Score Card saved as Score_Card.txt")
    print(content) 

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        # PyInstaller packs files into a temp folder _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


play_effect(resource_path("drumroll.wav"))
typeeffect("Welcome to Rock-Paper-Scissors Game!\n")
typeeffect("Instructions:\n")
typeeffect("1. Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors.\n")
typeeffect("2. Ayush will randomly choose one of the three options.\n")
print()
typeeffect("Enter your name to start:\n")
name = input(">> ")
name = name.strip() if name else "Player"
typeeffect("Enter the number of rounds you want to play.\n")
rounds = int(input("Enter number of rounds (default is 1): "))

rps(rounds, 0, 0, name)
      
print("Thank you for playing!")
input("Press Enter to exit...")