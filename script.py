from gtts import gTTS 
import vlc
import socket 
import tkinter as tk
import time
import datetime

def is_connected(): 
    try:
        socket.create_connection(("www.google.com", 80)) 
        return True 
    except OSError: 
        pass 
        return False

if __name__ == "__main__":
    print("Hi, this script plays music and opens a new window if internet is available, it will keep running to check if internet is back. \n")
    play = input("Do you want me to play audio when internet is available? Make sure you have installed vlc if yes (yes/no): ")
    if play.lower() == "yes" or play.lower() == "y":
        mytext = input("\n What do you want me to say once internet is available? ")
    language = 'en'
    while True:

        if is_connected():
            print("\nInternet is available as of ", datetime.datetime.now())
            if play.lower() == "yes" or play.lower() == "y":
                myobj = gTTS(text=mytext, lang=language, slow=False) 
                myobj.save("speak.mp3") 
                audio = vlc.MediaPlayer("speak.mp3")
                audio.play()
            screen = tk.Tk() 
            screen.title('Internet is back!') 
            button = tk.Button(screen, text='close', width=25, command=screen.destroy) 
            button.pack() 
            screen.mainloop()
            exit()

        else:
            print("Internet is down. Sleeping.", datetime.datetime.now())
            time.sleep(30)
