from __future__ import division, print_function, unicode_literals

# This code is so you can run the samples without installing the package
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

testinfo = "s, q"
tags = "tiles, Driver"

import pyglet
from pyglet.window import key

pyglet.resource.path.append(pyglet.resource.get_script_home())
pyglet.resource.reindex()

import cocos
from cocos import tiles, actions, layer
from cocos.director import director
from cocos.actions import AccelDeccel, MoveTo, MoveBy, Reverse, Repeat
from cocos.sprite import Sprite
speeed = 80

class DriveCar(actions.Driver):
    def step(self, dt):
        # handle input and move the car
        super(DriveCar, self).step(dt)
        scroller.set_focus(self.target.x, self.target.y)

def main():
    global keyboard, scroller
    from cocos.director import director
    director.init(width=800, height=600, autoscale=False, resizable=True)


    scroller = layer.ScrollingManager()
    test_layer = tiles.load('mapaKCK.tmx')['Warstwa Kafelków 1']
    obj = tiles.load('mapaKCK.tmx')['GameObjects']
    poi = tiles.load('mapaKCK.tmx')['Points']
    scroller.add(test_layer)
#0=start, 1=up, 2=bottom 3=bottom1,
#0=stacja, 1=mickiewicza, 2=kopernika, 3=orlicza, 4= pascala, 5=borsuka
    car_layer = layer.ScrollableLayer()
    car = cocos.sprite.Sprite('carKCK.png')
    car_layer.add(car)

    startX = poi.objects[0].x
    startY = poi.objects[0].y
    start = (startX, startY)

    upX = poi.objects[1].x
    upY = poi.objects[1].y
    up = (upX, upY)

    bottomX = poi.objects[2].x
    bottomY = poi.objects[2].y
    bottom = (bottomX, bottomY)

    bottom1X = poi.objects[3].x
    bottom1Y = poi.objects[3].y
    bottom1 = (bottom1X, bottom1Y)

    stacjaX = obj.objects[0].x
    stacjaY = obj.objects[0].y
    stacja = (stacjaX, stacjaY)

    micX = obj.objects[1].x
    micY = obj.objects[1].y
    mickiewicza = (micX, micY)

    kopX = obj.objects[2].x
    kopY = obj.objects[2].y
    kopernika = (kopX, kopY)
#najkrótsza ścieżka grafu
#wizualizacja samochodu z paczka

    orlX = obj.objects[3].x
    orlY = obj.objects[3].y
    orlicza = (orlX, orlY)

    pasX = obj.objects[4].x
    pasY = obj.objects[4].y
    pascala = (pasX, pasY)

    borX = obj.objects[5].x
    borY = obj.objects[5].y
    borsuka = (borX, borY)

    car.position = (start)
    car.rotation = 90
    if(car.position == start):
        car.do( MoveTo((mickiewicza),2))
    if(car.position == mickiewicza):
        car.do( MoveTo((borsuka),2))

    # yy = poi.objects(name ='mickiewicza').y
    # z =(xx,yy)

#    car.rotation = -180
    # yorl = obj.objects[2].y
    # xorl = obj.objects[2].x
    # orl =  (xorl,yorl)
    # car.do( MoveTo((orl),2))

    car.do(DriveCar())
    scroller.add(car_layer)

    main_scene = cocos.scene.Scene(scroller)


    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    def on_key_press(key, modifier):#obsluga klawiatury
        if key == pyglet.window.key.Z:
            if scroller.scale == 0.25:
                scroller.do(actions.ScaleTo(1, 0.5))
            else:
                scroller.do(actions.ScaleTo(.25, 0.5))
        elif key == pyglet.window.key.D:
            test_layer.set_debug(True)
        elif key == pyglet.window.key.RIGHT:
            car.rotation = 90
            car.speed = speeed
        elif key == pyglet.window.key.LEFT:
            car.rotation = -90
            car.speed = speeed
        elif key == pyglet.window.key.UP:
            car.rotation = 0
            car.speed = speeed
        elif key == pyglet.window.key.DOWN:
            car.rotation = 180
            car.speed = speeed
        elif key == pyglet.window.key.SPACE:
            car.speed = 0

    director.window.push_handlers(on_key_press)

    director.run(main_scene)

if __name__ == '__main__':
    main()

    # def on_key_press(key, modifier):
    #     if key == pyglet.window.key.Z:
    #         if scroller.scale == 1:
    #             scroller.do(actions.ScaleTo(0.3, 1))
    #         else:
    #             scroller.do(actions.ScaleTo(0.3, 1))
    #     elif key == pyglet.window.key.D:
    #        test_layer.set_debug(True)
    #director.window.push_handlers(on_key_press)

#    director.run(main_scene)

    #object_layer = test_layer['GameObjects']
    #move = MoveBy((20,300), duration=1)
    #car.do(move)
    #start = test_layer['GameObjects'][1]
    #car.positon = (kopernika.x,kopernika.y)
#    tmxdata = TiledMap('mapaTMX.tmx')


#PSEUDOKOD
# class Time(czas)
#    props = tmxdata.get_layer_by_name("mickiewicza").properties
#     czas = 2000s
#     if(czas == 0):
#         print('GameOver')
#         exit()
#
# paczkiDoDostarczenia = 2
# paczkiDoOdbioru = 2
# class Paczki(miejsce)
#     if(miejsce == 'mickiwicza' or miejsce == 'kopernika'):
#         if(miejsce == 'mickiewicza'):
#             MoveTo(miejsce)
#             MoveTo('magazyn')
#             paczkiDoDostaraczenia = paczkiDoDostarczenia -1;
#
#             if(paczkiDoDostarczenia ==0 and paczkiDoOdbioru == 0):
#                 print('YouWin')
#
#         if(miejsce == 'kopernika')
#             MoveTo(miejsce)
#             MoveTo('magazyn')
#             paczkiDoDostaraczenia = paczkiDoDostarczenia -1;
#
#             if(paczkiDoDostarczenia ==0 and paczkiDoOdbioru == 0):
#                 print('YouWin')
#     elif(miejsce == 'stacja'):
#         czas = 200s
#     else:
#         MoveTo(miejsce)
#         paczki= paczki -1
#         if(paczkiDoDostarczenia ==0 and paczkiDoOdbioru == 0):
#             print('YouWin')
