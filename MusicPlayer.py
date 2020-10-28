from pygame import mixer
from tkinter import *
from tkinter import filedialog

# mixer.init() initializes the pygame's mixer 
# mixer.music.load('filename.mp3') load a music file
# mixer.music.play() # Play



class MusicPlayer:
    def __init__(self, window): 
        window.geometry("320x100")
        window.title("El C##-productor")
        window.resizable(0,0)

        
        # Creating the buttons
        Load = Button(window, text = "Cargar", width = 10, font = ('Times', 10), command = self.load)   # This generates a Button to initialice a f(x)
        Play = Button(window, text = "Play", width = 10, font = ('Times', 10), command = self.play)
        Pause = Button(window, text = "Pausa", width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window, text = "Detener", width = 10, font = ('Times', 10), command = self.stop)     
        
        Load.place(x=30,y=20)    # This defines the position of the button
        Play.place(x=120,y=20)   # This defines the position of the button
        Pause.place(x=210,y=20)  # This defines the position of the button
        Stop.place(x=120,y=60)   # This defines the position of the button

        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()     #filedialog.askopenfilename open a window to select a file

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
    
    def stop(self):
        mixer.music.stop()

# Tkinter functions
root = Tk()
app = MusicPlayer(root)
root.mainloop()
