import time
import sys
import os


ORANGE = '\033[38;5;208m'
PURPLE = '\033[38;5;141m'
CYAN = '\033[38;5;51m'
WHITE = '\033[38;5;97m'
RED = '\033[38;5;196m'    
GREEN = '\033[38;5;46m'    
YELLOW = '\033[38;5;226m' 
BOLD = '\033[1m'
RESET = '\033[0m'
BLINK = '\033[5m'

def aesthetic_typing(text, color, speed=0.1):
    for char in text:
        sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(speed)


os.system('cls' if os.name == 'nt' else 'clear')


aesthetic_typing("Closing all other paths... 👨‍💻\n", CYAN, speed=0.05)
aesthetic_typing("Destination Reached: 'unke andaaz e karam ' 📍\n\n", PURPLE, speed=0.05)

aesthetic_typing("Na suna usne tawajjo se  🥺\n\n", ORANGE, speed=0.1)
aesthetic_typing("Fasaana dil ka   😣\n\n", CYAN, speed=0.1)

aesthetic_typing("Na suna usne tawajjo se  🥺\n\n", ORANGE, speed=0.1)
aesthetic_typing("Fasaana dil ka   😣\n\n", CYAN, speed=0.1)

aesthetic_typing("Umra guzri hai magar  🥰\n\n", WHITE, speed=0.1)
aesthetic_typing("Dard na jaana dil ka 😔\n\n",RED , speed=0.1)

aesthetic_typing("Umra guzri hai magar  🥰\n\n", WHITE, speed=0.1)
aesthetic_typing("Dard na jaana dil ka 😔\n\n", RED, speed=0.1)

aesthetic_typing("Unke andaaz e karam 👧 \n\n", YELLOW, speed=0.1)
aesthetic_typing("Unpe woh aana dil ka 🥰  \n\n", GREEN, speed=0.1)

aesthetic_typing("Unke andaaz e karam 👧 \n\n", YELLOW, speed=0.1)
aesthetic_typing("Unpe woh aana dil ka 🥰  \n\n", GREEN, speed=0.1)


aesthetic_typing("\n✨ This code Manage and  Developed by Mehul Kumar  ✨\n", RED + BLINK, speed=0.1)





