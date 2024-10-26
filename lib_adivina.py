import random

def giveMeNumber(min, max):
    return random.randint(min, max)

def welcome():
    print("""
╔══════════════╗
║ ¡Bienvenido! ║
╚══════════════╝
""")

def win():
    print(r"""
🎉 GANADOR 🎉
  __     ______  _    _  __          _______ _   _ 
  \ \   / / __ \| |  | | \ \        / /_   _| \ | |
   \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |
    \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |
     | | | |__| | |__| |    \  /\  /   _| |_| |\  |
     |_|  \____/ \____/      \/  \/   |_____|_| \_|
""")
    

def lose():
    print("""
╔═══╗ ♪
║███║ ♪
║ (╯︵╰) Has perdido! Fin del juego...
╚═══╝
""")
    

def Menu():
    print("""
╔═════════╗
║   MENU  ║
╚═════════╝
""")

def nivel():
    print("""
┏━━━━━━━━━━━━━┓
┃    NIVEL    ┃
┗━━━━━━━━━━━━━┛
""")
    
def estadistica():
    print("""
      ESTADÍSTICA
[▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒]  
[▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒]  
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓]  
""")