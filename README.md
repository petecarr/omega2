# omega2
Tools for Onion Omega2 Linux based microcomputer with wifi.

webserver1
Allows you to display a Web page on your browser and to control the RGB LED on the Omega expansion board.

Written in Python2 because onionGpio is only available in Python2 but the Omega Python2 allows 
version 3 style print() calls.

To use, run the program on your omega 
python ./webserver1.py
Then go to your browser and access
http://omega-xxxx.local:8888/hello
where xxxx is your Omega's unique id.

The browser refresh button is helpful.

I got the basic Web Server code from the following Web Page
https://ruslanspivak.com/lsbaws-part1/    (check out parts 2 and 3 too)
A very educational website.

The LED control part is taken from a Texas Instrument CC3200 Energia Example 
by 
created 25 Nov 2012 by Tom Igoe
modified 6 July 2014 by Noah Luskey

Thank you guys.

There are some behind the scene problems with this code. The blocking recv() calls
appear to get 3 responses for each recv and the first one tends to be a Q (quit)
response from the last time you ran the program. You can see these if you add a print(request) call
in the main loop. 
I think the use of sockets here is too simple-minded for use in anything but a toy Web page.
