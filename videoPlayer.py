import os
import vlc
import time
import keyboard
import tkinter as tk

#create tk frame
root = tk.Tk()
root.title("ComSeg")
root.videoFrame = tk.Frame(root)
root.canvas = tk.Canvas(root.videoFrame).pack(fill=tk.BOTH,expand=1)
root.videoFrame.pack(fill=tk.BOTH,expand=1)

#create vlc instance
instance = vlc.Instance()
player = instance.media_player_new()
player.set_hwnd(root.videoFrame.winfo_id()) #put in tkinter
media = instance.media_new("MY_VIDEO.mp4") #specify video
media.get_mrl()
player.set_media(media)
player.play()

#handles playing and pausing with space bar
playing = True
def playPauseButton():
	global playing
	if playing:
		player.pause()
		playing = False
		print("Pausing")
	else:
		player.play()
		playing = True
		print("Playing")	

# Handles fast forwarding and rewinding with . (FF) and , (RW)
def skipFive():
	global player
	player.set_time(player.get_time() + 5000)
	print(">>Fast Forwarding>>")

def rewFive():
	global player
	player.set_time(player.get_time() - 5000)
	print("<<Rewinding<<")

def quit():
	os._exit(1)

# configure hotkeys
keyboard.on_press_key(" ", lambda _:playPauseButton())
keyboard.on_press_key(".", lambda _:skipFive())
keyboard.on_press_key(",", lambda _:rewFive())
keyboard.on_press_key("x", lambda _:quit())

# detect hotkeys while running
while True:
	tk.mainloop()


