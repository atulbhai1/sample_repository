import os
from helpful_stuff.functions import get_entry
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
video_link = get_entry('Enter the video link(example: https://youtu.be/ycJe_fhkOuw):', 'Youtube Video Downloader', 'Next')
os.chdir(askdirectory(initialdir=os.getcwd(), title='Youtube Video Downloader'))
showinfo('Youtube Video Downloader', 'This might take a while')
os.system(f'youtube-dl --no-check-certificate {video_link}')
showinfo('Youtube Video Downloader', 'Done!')