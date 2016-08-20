##importing socket
import socket

##importing variables needed from Settings.py
from Settings import HOST, PORT, PASS, IDENT, CHANNEL

def openSocket():
	
	##creatr a socket
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send("PASS " + PASS + "\r\n") 
	s.send("ztmurphy21" + IDENT + "\r\n")
	s.send("JOIN #" + CHANNEL + "\r\n")
	return s
	
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send(messageTemp + "\r\n")
	print("Sent: " + messageTemp)