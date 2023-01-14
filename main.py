import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
         

        video.download()
        
        finishLable.configure(text="Download Complete")
    except:
        finishLable.configure(text="Invalid Youtube URL", text_color="red")
    
def progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = bytes_downloaded / total_size * 100
    per = str(int(percentage)) 
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    progressBar.set(float(percentage / 100))





customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# our app frame
title = customtkinter.CTkLabel(app, text="Insert Youtube Link")
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#final download 
finishLable = customtkinter.CTkLabel(app, text="") 
finishLable.pack()

# progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


# download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload ,width=350, height=40)

download.pack(padx=10, pady=10)

# run app
app.mainloop()