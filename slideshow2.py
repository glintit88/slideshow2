#!/usr/bin/env python3
"""Display a slideshow from a list of filenames"""

import os
import tkinter
import glob
from itertools import cycle
from PIL import Image, ImageTk
import time
from tkinter.messagebox import askyesno

global onoff
global tmp

class Slideshow(tkinter.Tk):
    """Display a slideshow from a list of filenames"""
    def __init__(self, images, slide_interval):
        """Initialize

        images = a list of filename 
        slide_interval = milliseconds to display image
        """
        tkinter.Tk.__init__(self)
        self.geometry("+0+0")
      #  self.iconbitmap('icon.ico')
        self.slide_interval = slide_interval
        self.images = None
        self.set_images(images)
        self.slide = tkinter.Label(self)
        self.slide.pack()
        self.button1 = tkinter.Button(text="1", command=loop1)
        self.button1.pack()
    def set_images(self, images):
         self.images = cycle(images)

    def center(self):
        """Center the slide window on the screen"""
        self.update_idletasks()
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        size = tuple(int(_) for _ in self.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        if answer:
            self.geometry("+%d+%d" % (10, 510))
        else:    
            self.geometry("+%d+%d" % (1920, 10))

    def set_image(self):
        global tmp
        """Setup image to be displayed"""
        #self.image_name = next(self.images)
        #print(next(self.images))
        list_of_files = glob.glob(folder_path+ file_type)
        latest_file = max(list_of_files, key=os.path.getctime)
        if tmp != latest_file:
            
            print("latest_file--> "+latest_file)
            print(pos)
            tmp = latest_file
        #self.image_name =  'image/test.png'
            self.image_name =  latest_file
            filename, ext = os.path.splitext(self.image_name)
            image=Image.open(self.image_name)
            if answer:
                 reimage = image.resize((820,450), Image.ANTIALIAS)
            else: 
                reimage = image.resize((1624,938), Image.ANTIALIAS)
           # self.image = ImageTk.PhotoImage(Image.open(self.image_name).resize(300,200), Image.ANTIALIAS)
            #img = image.resize(320, 300)
            self.image = ImageTk.PhotoImage(reimage)
            
    def main(self):
        """Display the images"""
        self.set_image()
        self.slide.config(image=self.image)
        self.title(self.image_name)
        self.center()
        self.after(self.slide_interval, self.start)

    def start(self):
        """Start method"""
        self.main()
        self.mainloop()

def loop1():
    answer = askyesno(title = 'Continue', message = "yes/no")
    
    if slide_interval == 1000:
        slide_interval = 10000
    else:
        slide_interval = 1000
        
    print("slide_interval:" + str(slide_interval))

if __name__ == "__main__":
    slide_interval = 1000
    answer = askyesno(title = 'Window 1?', message = "yes/no")
    print(answer)
    pos = 1
    folder_path = os.path.join(os.path.dirname(__file__), "pic")
    print("folder path:: ->>> "+ folder_path)
    file_type = r'\*.jpg'
    list_of_files = glob.glob(folder_path+ file_type)
    tmp = "ss"
    

    images = glob.glob("pic\\*.jpg")

    # start the slideshow
    slideshow = Slideshow(images, slide_interval)
    slideshow.start()

