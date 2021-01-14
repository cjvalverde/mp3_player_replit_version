from replit import audio
from tkinter import *
from tkinter import filedialog

print('\nmp3 player started')
current_title_id = 0
global_vol = 0.3


class MusicPlayer:
    def __init__(self, window):
        window.geometry('320x100');
        window.title('mp3 player');
        window.resizable(0, 0)
        Start = Button(window, text='Start', width=10, font=('Times', 10), command=self.start)
        PauseResume = Button(window, text='Pause/Resume', width=10, font=('Times', 10), command=self.pauseresume)
        Up = Button(window, text='Vol+', width=10, font=('Times', 10), command=self.up)
        Down = Button(window, text='Vol-', width=10, font=('Times', 10), command=self.down)
        Start.place(x=40, y=20)
        PauseResume.place(x=40, y=60)
        Up.place(x=170, y=20)
        Down.place(x=170, y=60)

    def start(self):
        global current_title_id
        global global_vol
        self.music_file = filedialog.askopenfilename()
        if len(self.music_file) != 0:
            playing = audio.get_playing()
            if len(playing) == 0:
                audio.play_file(self.music_file, global_vol, True, 0)
                print('Now playing %s' % self.music_file)
                temp = audio.get_playing()
                for t in temp:
                    current_title_id = t.id
            else:
                for p in playing:
                    p.toggle_playing()  # is something was being payed, then pause it first
                audio.play_file(self.music_file, global_vol, True, 0)
                print('Now playing %s' % self.music_file)
                temp = audio.get_playing()
                for t in temp:
                    current_title_id = t.id

    def pauseresume(self):
        playing = audio.get_playing()
        paused = audio.get_paused()
        if len(playing) != 0:
            for p in playing:
                if p.id == current_title_id:
                    p.toggle_playing()
                    print('Reproduction paused')
        if len(paused) != 0:
            for p in paused:
                if p.id == current_title_id:
                    p.toggle_playing()
                    print('Reproduction resumed')

    def up(self):
        global global_vol
        playing = audio.get_playing()
        if len(playing) != 0:
            for p in playing:
                p.volume += 0.1
                global_vol += 0.1
                print('Volume turned up to %d%%' % int(100 * global_vol))

    def down(self):
        global global_vol
        playing = audio.get_playing()
        if len(playing) != 0:
            for p in playing:
                p.volume -= 0.1
                global_vol -= 0.1
                print('Volume turned down to %d%%' % int(100 * global_vol))


root = Tk()
app = MusicPlayer(root)
root.mainloop()
