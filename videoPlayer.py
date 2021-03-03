import vlc
import time
import keyboard

#create vlc instance
instance = vlc.Instance()
player = instance.media_player_new()
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

def rewFive():
	global player
	player.set_time(player.get_time() - 5000)

# configure hotkeys
keyboard.on_press_key(" ", lambda _:playPauseButton())
keyboard.on_press_key(".", lambda _:skipFive())
keyboard.on_press_key(",", lambda _:rewFive())

# detect hotkeys while running
while True:
	if keyboard.is_pressed('x'):                                # exit keybind to x
		exit()
	else:
		time.sleep(.1)
