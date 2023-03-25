# Made with help from a YouTube video by "nevsky.programming" and a StackExchange question.
# Finds your IP address.

import socket # <--- Imports Socket
pchostname=socket.gethostname() # <--- Finds PC Hostname
ipaddress=socket.gethostbyname(pchostname) # <--- Finds IP Address
print("Your Computer Hostname is: "+pchostname) # <--- Says Hostname
print("Your IP Address is: "+ipaddress) # <--- Says IP 

