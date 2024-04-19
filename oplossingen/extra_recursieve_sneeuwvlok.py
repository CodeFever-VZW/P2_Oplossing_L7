import turtle

from sneeuwvlok import Sneeuwvlok

def teken(startx, starty, orde, grootte, aantal_vlokken):
    if aantal_vlokken >= 0:
        sneeuwvlok = Sneeuwvlok(startx, starty)
        sneeuwvlok.teken(orde, grootte)
        startx = startx + 10
        starty = starty - 5.7
        grootte = grootte - 20
        teken(startx, starty, orde, grootte, aantal_vlokken - 1)

teken(0, 0, 2, 300, 15)
turtle.done()