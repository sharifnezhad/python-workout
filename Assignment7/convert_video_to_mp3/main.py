from moviepy import editor
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()
filename = askopenfilename()
video=editor.VideoFileClip(filename)
name_file=filename.split('.')
video.audio.write_audiofile(name_file[0]+'.mp3')