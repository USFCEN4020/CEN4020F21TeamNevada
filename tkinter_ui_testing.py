from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

root = Tk()
root.title = "Welcome to InCollege"

mainframe = ttk.Frame(root, padding=(0, 0, 0, 0))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

incollege_Image = PhotoImage(file="resources/InCollegePhotoEdited.png")

# the incollege image
incollege_image_label = ttk.Label(mainframe)
incollege_image_label['image'] = incollege_Image
incollege_image_label.grid(column=0, row=0, columnspan=12, rowspan=3)

# the welcome to incollege text
incollege_welcome_label = ttk.Label(mainframe, text="Welcome to InCollege", font="Helvetica 48")
incollege_welcome_label.grid(column=1, row=4, columnspan=8, rowspan=1)

# image with success story
success_story_image = Image.open("resources/PersonAtLaptopStock.jpg")
success_story_image.thumbnail((1248, 900))

# cut the image in half vertically so that we can overlay the text over the left half
success_story_image_left = success_story_image.crop((0, 0, success_story_image.width/2, success_story_image.height))
success_story_image_right = success_story_image.crop((success_story_image.width/2, 0, success_story_image.width, success_story_image.height))

# convert resized image to tk photoimage
success_story_image_left_tk = ImageTk.PhotoImage(success_story_image_left)
success_story_image_left_label = ttk.Label(mainframe, text="Daniela, USF 21':\n \"InCollege has made my stressful job "
                                                     "search a\n thousands times easier by connecting with other\n "
                                                     "students and applying to jobs in one go!\"",
                                            font="Helvetica 16",
                                            compound="center",
                                            image=success_story_image_left_tk,
                                            padding=(0, 0, 0, 0))
# success_story_image_left_label['image'] = success_story_image_left_tk
success_story_image_left_label.grid(column=0, row=5, columnspan=6, rowspan=10)

success_story_image_right_tk = ImageTk.PhotoImage(success_story_image_right)
success_story_image_left_label = ttk.Label(mainframe, image=success_story_image_right_tk, padding=(0, 0, 0, 0))
success_story_image_left_label.grid(column=6, row=5, columnspan=6, rowspan=10)


# success_story_text_label = ttk.Label(mainframe, text="Daniela, USF 21':\n \"InCollege has made my stressful job "
#                                                      "search a\n thousands times easier by connecting with other\n "
#                                                      "students and applying to jobs in one go!\"",
#                                      font="Helvetica 16",
#                                      background=None)
# success_story_text_label.grid(column=1, row=7, columnspan=5, rowspan=2)

root.mainloop()
