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

import collections
import math
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

class Graf:

  def __init__(self):
      self.wiechrzcholki = set()

      self.krawedzie = collections.defaultdict(list)
      self.wagi = {}

  def add_vertex(self, value):
    self.wiechrzcholki.add(value)

  def add_edge(self, od_wierzcholka, do_wierzcholka, dystans):
    if od_wierzcholka == do_wierzcholka: pass  # bez cykli
    self.krawedzie[od_wierzcholka].append(do_wierzcholka)
    self.wagi[(od_wierzcholka, do_wierzcholka)] = dystans


def dijkstra(graf, start):
  S = set()

  delta = dict.fromkeys(list(graf.wiechrzcholki), math.inf)
  poprzednik = dict.fromkeys(list(graf.wiechrzcholki), None)

  delta[start] = 0


  while S != graf.wiechrzcholki:
    v = min((set(delta.keys()) - S), key=delta.get)
    for sasiad in set(graf.krawedzie[v]) - S:
      nowa_sciezka = delta[v] + graf.wagi[v,sasiad]

      if nowa_sciezka < delta[sasiad]:
        delta[sasiad] = nowa_sciezka

        poprzednik[sasiad] = v
    S.add(v)

  return (delta, poprzednik)

def shortest_path(graf, start, end):

  delta, poprzednik = dijkstra(graf, start)

  sciezka = []
  wierzcholek = end

  while wierzcholek is not None and wierzcholek is not start:
    sciezka.append(wierzcholek)
    wierzcholek = poprzednik[wierzcholek]

  sciezka.reverse()
  return sciezka

if __name__ == "__main__":

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

    miejsca = {}
    startX = poi.objects[0].x
    startY = poi.objects[0].y
    miejsca['start'] = (startX, startY)

    upX = poi.objects[1].x
    upY = poi.objects[1].y
    miejsca['up'] = (upX, upY)

    bottomX = poi.objects[2].x
    bottomY = poi.objects[2].y
    miejsca['bottom'] = (bottomX, bottomY)

    bottom1X = poi.objects[3].x
    bottom1Y = poi.objects[3].y
    miejsca['bottom1'] = (bottom1X, bottom1Y)

    stacjaX = obj.objects[0].x
    stacjaY = obj.objects[0].y
    miejsca['stacja'] = (stacjaX, stacjaY)

    micX = obj.objects[1].x
    micY = obj.objects[1].y
    miejsca['mickiewicza'] = (micX, micY)

    kopX = obj.objects[2].x
    kopY = obj.objects[2].y
    miejsca['kopernika'] = (kopX, kopY)

    orlX = obj.objects[3].x
    orlY = obj.objects[3].y
    miejsca['orlicza'] = (orlX, orlY)

    pasX = obj.objects[4].x
    pasY = obj.objects[4].y
    miejsca['pascala'] = (pasX, pasY)

    borX = obj.objects[5].x
    borY = obj.objects[5].y
    miejsca['borsuka'] = (borX, borY)

    G = Graf()
    G.add_vertex('start')
    G.add_vertex('mickiewicza')
    G.add_vertex('up')
    G.add_vertex('borsuka')
    G.add_vertex('bottom1')
    G.add_vertex('stacja')
    G.add_vertex('pascala')
    G.add_vertex('orlicza')
    G.add_vertex('bottom')
    G.add_vertex('kopernika')

    G.add_edge('start', 'mickiewicza', 9)
    G.add_edge('mickiewicza', 'up', 2)
    G.add_edge('up', 'borsuka', 2)
    G.add_edge('borsuka', 'bottom1', 4)
    G.add_edge('bottom1', 'stacja', 1)
    G.add_edge('bottom1', 'pascala', 3)
    G.add_edge('pascala', 'orlicza', 5)
    G.add_edge('orlicza', 'bottom', 3)
    G.add_edge('bottom', 'kopernika', 3)
    G.add_edge('kopernika', 'start', 3)


    G.add_edge('mickiewicza', 'start', 9)
    G.add_edge('up', 'mickiewicza', 2)
    G.add_edge('borsuka', 'up', 2)
    G.add_edge('bottom1', 'borsuka', 4)
    G.add_edge('stacja', 'bottom1', 1)
    G.add_edge('pascala', 'bottom1', 3)
    G.add_edge('orlicza', 'pascala', 5)
    G.add_edge('bottom', 'orlicza', 3)
    G.add_edge('kopernika', 'bottom', 3)
    G.add_edge('start', 'kopernika', 3)

    #   car.rotation = 90
    #   if(car.position == start):
    #       car.do( MoveTo((mickiewicza),2))
    #   if(car.position == mickiewicza):
    #       car.do( MoveTo((borsuka),2))


#	print(dijkstra(G, 'c'))
    print(shortest_path(G, 'mickiewicza', 'pascala'))

    zupa = shortest_path(G, 'mickiewicza', 'pascala')

	#print(G)

    car.position = miejsca['start']
    # car.runAction(aaa)
    # time.sleep(10)
    # car.do(MoveTo(miejsca['borsuka']))
    # car.do(MoveTo(
        # for i in zupa:
            # MoveTo(miejsca[i], 5)
    # ))

    def www():
        print('aaa')

    action = CallFunc(www)


    for i in zupa:
        # car.do(MoveTo(miejsca['up'], 10) + MoveTo(miejsca['borsuka'], 5))
        car.do( MoveTo((miejsca[i]),2))
        action
        # car.do(Sequence(DelayTime(10), MoveTo((miejsca[i]),2)))
        # MoveTo((miejsca[i]),2)
        # print(miejsca[i])
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
