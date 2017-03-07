#!/usr/bin/env python3
"""
Obtain the weather for PDX (Portland, Oregon, USA) from the NOAA web site.
Works from the Linux Omega command line.

This link https://github.com/RandomArray/wifiweather
shows you how to use PHP to obtain your weather. (and also posts the results as Wifi access points
so you can see it on youre phone)

From Mike's README.md
This was built to run on an Onion Omega running OpenWRT in the United States.
Lookup the XML feed for your area here: http://w1.weather.gov/xml/current_obs/
"""

import urllib
from urllib import request
import json
import xml.etree.ElementTree as ET

site="http://w1.weather.gov/xml/current_obs/KPDX.xml"

jfile=urllib.request.urlopen(site)

jsfile=jfile.read()
#print(type(jsfile))  # bytes
jsf = str(jsfile).strip('b\'')
jsf = jsf.replace('\\r','')
jsf = jsf.replace('\\t','    ')
jsf = jsf.replace('\\n','\n')

#print(jsf)

tags = ["observation_time", "location", "latitude", "longitude", "weather", \
        "wind_dir", "wind_mph", "wind_string", "pressure_in", "temperature_string",
        "relative_humidity", "windchill_string", "visibility"]
vals=[]
tag_names=[]

root = ET.fromstring(jsf)
for child in root:
    if child.tag in tags:
        vals.append(child.text)
        tag_names.append(child.tag)
        #print(child.tag, child.text)

lst = zip(tag_names, vals)
dct = dict(lst)

#j = 0
#for i in tag_names:
#    print(i, ": ",vals[j])
#    j += 1

print("Location    : {0}".format(dct["location"]))
print("Lat/Long    : ({0},{1})".format(dct["latitude"], dct["longitude"]))
print("Time        : {0}".format(dct["observation_time"]))
print("Weather     : {0}".format(dct["weather"]))
print("Rel Humidity: {0}%".format(dct["relative_humidity"]))
print("Temperature : {0}".format(dct["temperature_string"]))
print("Wind        : {0} {1} mph".format(dct["wind_dir"], dct["wind_mph"]))
print("            : {0}".format(dct["wind_string"]))
print("Wind chill  : {0}".format(dct["windchill_string"]))
print("Pressure    : {0} inches Hg".format(dct["pressure_in"]))
