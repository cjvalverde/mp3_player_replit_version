# mp3_player in Python, replit_version

**Version 1.0.0**

Code and music files for MP3 Player on repl.it. The idea of this program is to further explore different python modules. In this case, I am exploring the BETA functionality of AUDIO in repl.it and implementing a user interface with TKINTER

---

##Description of how it works on repl.it
To use this program, open your repl account, upload main.py and the mp3  music files  you want to hear. Then, run the main file.

When the program is started (main.py), the user interface appears in the graphical console (on top of the standard text console). The console has 4 buttons:
- Start :     This button is used to select the music file that is going to be played
- Pause/Resume :  This button will pause and resume the currently played song
- Vol+ :  This button trunks the volume up
- Vol- :  This button trunks the volume down


On click on “Start”, a File Dialog opens to select a music file. Initially the folder shown is the same where main.py is located. In my case, I uploaded some mp3 files in the same folder, so no need to navigate. However, a folder structure could be used to organize the music and the user can navigate in the File Dialog to the desired mp3 file.

Double click or select it and click “Open” to start listening to a file.

“Pause/Resume” pauses or resumes the reproduction.
“Vol+” or “Vol-” turn 10% up or down the volume. The initial volume setting is 30%.

Golbal volume for all songs for each song, but I decided to make it global, because I felt more real like that.

Click on “Start” when a file is being reproduced opens the file manager but music will only stop if user opens a file. If user exits file dialog with "cancel", msic is not interrupted.

All actions are logged as text in the text console output.

---

## Contents

All files can be found in https://repl.it/@...
- main.py
- BROKENFACE.mp3
- CUERPO.mp3
- INVITADO.mp3
- JETSET.mp3
- readme.txt

---
## Sources

https://docs.python.org/3/library/dialog.html?highlight=tkinter%20basics
Tkinter Dialogs on  python.org:
For the file dialog to select a music file:

https://nerdparadise.com/programming/pygame/part3
PyGame Tutorial:
I used PyGame to program a first draft of the mp3 Player, but it didn’t work in repl.it, so I moved to use the beta Audio libraries offered in REPL after my professor's recommendation.

http://docs.repl.it/repls/audio
Audio on repl.it [BETA:
A wiki entry on repl.it to actually be able to play, pause, turn volume up and down, and manage the music files

---
## Contributors

- Carlos Valverde <carlos_valverdeb@hotmail.com.com>

---
## Licence and copyright

© Carlos Valverde
