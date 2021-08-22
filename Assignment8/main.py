import os
import imageio
from tkinter import Tk
from tkinter.filedialog import askdirectory
Tk().withdraw()
filename = askdirectory()
myfile =os.listdir(filename)
images=[]
for i in range(len(myfile)):
    images.append(imageio.imread(filename+'/'+myfile[i]))
imageio.mimsave('mypic2.gif',images)