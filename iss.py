#!/usr/bin/env python

__author__ = 'Jasmyne with help from 101computer.net and JT'
import json
import turtle
import urllib.request
import time


url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print("There are currently " + str(result["number"]) + " astronauts in space:")
print("")

people = result["people"]

for p in people:
    print(p["name"] + " on board of " + p["craft"])


def indipassing():
    url = "http://api.open-notify.org/iss-pass.json?lat=39.7&lon=86.1&alt=20&n=5"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    passings = result["response"]
    for p in passings:
        date_time = time.ctime(p['risetime'])
        print("The ISS will be over Indianapolis on " + date_time)


def currentlocation():
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)

    obj = json.loads(response.read())

    print("The current time is " + str(time.ctime(obj['timestamp'])))
    print("The space station is currently at " + obj['iss_position']['latitude'] + "lat,", obj['iss_position']['longitude'] + "long")


def main():
    indipassing()
    currentlocation()
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic("map.gif")
    screen.register_shape("iss.gif")
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    turtle.done()
    # iss.setheading(45)
    # iss.penup()


if __name__ == '__main__':
    main()
