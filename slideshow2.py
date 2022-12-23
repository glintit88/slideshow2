#!/usr/bin/env python3
"""Display a slideshow from a list of filenames"""

import os
import tkinter
import glob
from itertools import cycle
from PIL import Image, ImageTk
import time

class Slideshow(tkinter.Tk):
    """Display a slideshow from a list of filenames"""
    def __init__(self, images, slide_interval):
        """Initialize

        images = a list of filename 
        slide_interval = milliseconds to display image
        """
        tkinter.Tk.__init__(self)
        self.geometry("+0+0")
        self.slide_interval = slide_interval
        self.images = None
        self.set_images(images)
        self.slide = tkinter.Label(self)
        self.slide.pack()

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
        self.geometry("+%d+%d" % (100, 100))

    def set_image(self):
        """Setup image to be displayed"""
        #self.image_name = next(self.images)
        print(next(self.images))
        list_of_files = glob.glob(folder_path+ file_type)
        latest_file = max(list_of_files, key=os.path.getctime)
        print("latest_file--> "+latest_file)
        #self.image_name =  'image/test.png'
        self.image_name =  latest_file
        filename, ext = os.path.splitext(self.image_name)
        image=Image.open(self.image_name)
        reimage = image.resize((320,200), Image.ANTIALIAS)
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


if __name__ == "__main__":
    slide_interval = 1000

    folder_path = os.path.join(os.path.dirname(__file__), "image")
    print("folder path:: ->>> "+ folder_path)
    file_type = r'\*.jpg'
    list_of_files = glob.glob(folder_path+ file_type)

    

    images = glob.glob("image\\*.jpg")

    # start the slideshow
    slideshow = Slideshow(images, slide_interval)
    slideshow.start()
