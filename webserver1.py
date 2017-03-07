import socket
import sys
if sys.version_info[0] >= 3:
    print("Must be using Python 2, onionGpio not available in Python 3")
    quit()
import onionGpio

"""
This is for the Omega expansion board with a RGB LED.
Can be adapted as necessary to drive other GPIOs.

Go to desktop browser and access the web address
http://omega-xxxx.local:8888/hello
xxxx is your own omega id

Credits:
The basic Web server code.
https://ruslanspivak.com/lsbaws-part1/    (check out parts 2 and 3 too)
The buttons and led interface.
From a TI cc3200 Launchpad demo on the Energia IDE
created 25 Nov 2012 by Tom Igoe
modified 6 July 2014 by Noah Luskey
"""

#----------------------------------------------------------------------------
# Was moved into a separate file (webserver1.html)
# Keep this here as a demo of differences between Python string and actual html.
# Pay attention to \" everywhere.

mypage1 = """\
HTTP/1.1 200 OK
Content-type:text/html

<head>
<title> Hello Omega</title>
</head>
<body>
<p>Hello Omega. I'm a Web Server!</p>
<h1 align=center><font color=\"red\">Welcome</font></h1>
<font color=\"red\">RED LED  </font>
    <button onclick=\"location.href='/RH'\">HIGH</button>
    <button onclick=\"location.href='/RL'\">LOW</button><br>
<font color=\"green\">GREEN LED</font>
    <button onclick=\"location.href='/GH'\">HIGH</button>
    <button onclick=\"location.href='/GL'\">LOW</button><br>
<font color=\"blue\">BLUE LED </font>
    <button onclick=\"location.href='/BH'\">HIGH</button>
    <button onclick=\"location.href='/BL'\">LOW</button><br>
Press to Quit <button onclick=\"location.href='/Q'\">QUIT</button>
<br>

</body>
"""
#----------------------------------------------------------------------------

RED_LED   = 17
GREEN_LED = 16
BLUE_LED  = 15
HIGH = 0
LOW = 1

gpioObjRed   = onionGpio.OnionGpio(RED_LED)
status       = gpioObjRed.setOutputDirection(0)
status       = gpioObjRed.setValue(LOW)
gpioObjGreen = onionGpio.OnionGpio(GREEN_LED)
status       = gpioObjGreen.setOutputDirection(0)
status       = gpioObjGreen.setValue(LOW)
gpioObjBlue  = onionGpio.OnionGpio(BLUE_LED)
status       = gpioObjBlue.setOutputDirection(0)
status       = gpioObjBlue.setValue(LOW)

def clear_leds():
    status       = gpioObjRed.setValue(LOW)
    status       = gpioObjGreen.setValue(LOW)
    status       = gpioObjBlue.setValue(LOW)

def digitalWrite(led, value):
    if led == RED_LED:
        status  = gpioObjRed.setValue(value)
    elif led == GREEN_LED:
        status  = gpioObjGreen.setValue(value)
    elif led == BLUE_LED:
        status  = gpioObjBlue.setValue(value)
    #print(led, value)

#-----------------------------------------------------------------

html_file = "webserver1.html"
try:
    myhtml = open(html_file, 'r')
except IOError:
    print("Can't find  html file {0}".format(html_file))
    quit()

mypage = myhtml.read()
myhtml.close()

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print("Serving HTTP on port {0} ...".format(PORT))
cnt = 0
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    #print(request[0:7])

    if request[4:7] =="/RH":
        digitalWrite(RED_LED, HIGH)               # GET /RH turns the LED on

    if request[4:7] =="/RL":
        digitalWrite(RED_LED, LOW)                # GET /RL turns the LED off

    if request[4:7] =="/GH":
        digitalWrite(GREEN_LED, HIGH)               # GET /GH turns the LED on

    if request[4:7] =="/GL":
        digitalWrite(GREEN_LED, LOW)                # GET /GL turns the LED off

    if request[4:7] =="/BH":
        digitalWrite(BLUE_LED, HIGH)               # GET /BH turns the LED on

    if request[4:7] =="/BL":
        digitalWrite(BLUE_LED, LOW)                # GET /BL turns the LED off

    if (cnt > 0) and request[4:6] =="/Q":
        # note we are running python2 (use input in python3)
        # but it appears the print statements are OK
        ans = raw_input("close client (y/n)")
        #ans = input("close client (y/n)")
        if ans[0] == 'y':
            # close the connection:
            client_connection.shutdown(socket.SHUT_RDWR)
            client_connection.close()
            print("client disconnected")
            clear_leds()
            break
    cnt += 1

# Mysteriously getting 3 responses including often the past one from the previous run. 

    http_response = mypage

    client_connection.sendall(http_response)
    #client_connection.sendall(http_response.encode('utf-8')) for Python 3
    client_connection.close()
webserver1.py" 150L, 4691C
