# Project-1


from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

#Get url and then set url of the video accordingly
def setURL():
    url = getURL.get()
    print(url)
    
#Object is created to hold and print URL
global yt
yt = YouTube(url)
print(yt.title)

#Get the stream qualities of the videos 
global videos
videos = yt.streams.filter(mime_type='video/mp4')

#Description is visible in listboxDes
title = yt.title
views = yt.views
length = yt.length
rating = yt.rating
listboxDes.insert(END,"Title: " +str(title))
listboxDes.insert(END,"Number of views: " +str(views))
listboxDes.insert(END,"Length of video: " +str(length))
listboxDes.insert(END,"Rating of video: " +str(rating))
    
#Get stream quality and display as list(one after the other) in the Listbox
count = 1
for v in videos:
    listboxQuality.insert(END, str(count)+". "+str(v)+"\n\n")
    count += 1

#get downloaded file and browse for a location and set the location 
def clickBrowse():
    location_of_download = filedialog.askdirectory()
    getLoc.set(location_of_download)
    
#get downloaded file and run it to make sure it works
def clickDownload():
    if(getURL.get() == ""):
        messagebox.showinfo("ERROR: Please try again", "Enter url! ")
        return
    elif (getLoc.get() == ""):
        messagebox.showinfo("ERROR: Please try again", "Enter location! ")
        return
    

select = listboxQuality.curselection()
quality = videos[select[0]]
location = getLoc.get()
quality.download(location)
messagebox.showinfo("The downloading has finished", yt.title+" has been downloaded successfully!")

#clear the fields for another url
def clickReset():
    getURL.set("")
    getLoc.set("")
    listboxDes.delete(0, END)
    listboxQuality.delete(0,END)

#Create root object for style attributes within the form itself
root = Tk()
root.title("YouTube Dowloader")
root.config(bg="Yellow")
root.geometry("855x600")
root.resizable(False, False)

#Set the correct labels for the form
headLabel       = Label(root,   text="YOUTUBE DOWNLOADER", font=("Times New Roman",25), relief=SOLID, bd=4, borderwidth=2).
grid(row=0, column=1, padx=10, pady=10)
urlLabel        = Label(root,   text="URL",                 font=("Times New Roman",17), relief=SOLID, bd=4, borderwidth=2).
grid(row=1, column=0, padx=10, pady=10)
descriptionLabel= Label(root,   text="Description",         font=("Times New Roman",17), relief=SOLID, bd=4, borderwidth=2).
grid(row=2, column=0, padx=10, pady=10)
qualityLabel    = Label(root,   text="SELECT QUALITY",      font=("Times New Roman",17), relief=SOLID, bd=4, borderwidth=2).
grid(row=3, column=0, padx=10, pady=10)
locLabel        = Label(root,   text="LOCATION",            font=("Times New Roman",17), relief=SOLID, bd=4, borderwidth=2).
grid(row=4, column=0, padx=10, pady=10)

#Get input of url and location from the form
getURL = StringVar()
getLoc = StringVar()

#Set entry from the form for location and url
locEntry    = Entry(root,   font=("Times New Roman",14), textvariable = getLoc, width = 30, relief=SOLID, bd=4, borderwidth=2).
grid(row=4,column=1, padx=10, pady=10)
urlEntry    = Entry(root,   font=("Times New Roman",14), textvariable = getURL, width = 30, relief=SOLID, bd=4, borderwidth=2).
grid(row=1,column=1, padx=10, pady=10)

#List box is created for video details
listboxDes     = Listbox(root, font=("Times New Roman",14), width = 56, height = 12, bd=3, relief=SOLID, borderwidth=2)
listboxDes.grid(row=2,column=1, padx=10, pady=10)

#List box is created for video qualities
listboxQuality     = Listbox(root, font=("Times New Roman",12), width = 56, height = 12, bd=3, relief=SOLID, borderwidth=2)
listboxQuality.grid(row=3,column=1, padx=10, pady=10)

#Set buttons on the form and align them properly with the correct attributes
reset     = Button(root, text = "Clear",      font=("Times New Roman",14), width=20, relief=SOLID, borderwidth=4, command=clickReset).
grid(row=5, column=2, padx=10, pady=10)
download  = Button(root, text = "Download",   font=("Times New Roman",14), width=20, relief=SOLID, borderwidth=4, command=clickDownload).
grid(row=5, column=0, padx=10, pady=10)
browse    = Button(root, text = "Browse",     font=("Times New Roman",14), width=20, relief=SOLID, borderwidth=4, command=clickBrowse).
grid(row=5, column=1, padx=10, pady=10)
url       = Button(root, text = "Set URL",    font=("Times New Roman",14), width=20, relief=SOLID, borderwidth=4, command=setURL).
grid(row=1, column=2, padx=10, pady=10)

#Loop is set so form is continous
root.mainloop()
