##imports openSocket function from Socket.py file
from Socket import openSocket
from Initialize import joinRoom

s = openSocket()
joinRoom(s)

while True:
	##makes infinite loop
	persist = True