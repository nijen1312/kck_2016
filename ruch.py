#from __future__ import division, print_function, unicode_literals

# sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# testinfo = "s, q"
# tags = "tiles, Driver"

import collections
import math
import cocos
import random
import sys
from cocos import tiles, layer, actions
from cocos.director import director
from cocos.actions import MoveTo

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

global inAction, startAction, doTask, G, miejsca, paczki

class DriveCar(actions.Driver):
    def step(self, dt):
        global inAction, startAction, doTask, cAdres, isPack, cel, ruch

        if(not inAction):
            plik = open('NLP.out')
            try:
                tekst = plik.read()
            finally:
                plik.close()
            pl = eval(tekst)
            
            zadanie = pl[0]
            if(len(pl) == 2):
              zadanie2 = pl[1]
            rozkaz = zadanie[0]
            if(rozkaz == 'ODBIERZ' or rozkaz == 'ZAWIEĹą'):
              adres = zadanie[2]
            if(rozkaz == 'JEDĹą'):
              adres = zadanie[1]
##            if(rozkaz2 == 'ODBIERZ' or rozkaz2 == 'ZAWIEĹą'):
##              adres2 = zadanie2[2]
##            if(rozkaz2 == 'JEDĹą'):
##              adres2 = zadanie2[1]
            inAction=True
            startAction=True
            
        if(not isPack):
          packAdres = random.choice(list(paczki))
          paczki[packAdres].opacity = 255
          cel = packAdres
          while(cel == packAdres or cel == cAdres):
            cel = random.choice(list(paczki))
          print("musze odebrac paczke z " + packAdres + " i dostarczyc paczke na " + cel)
          isPack = True
        
        if(startAction):
            startAction = False
            if(rozkaz == 'ODBIERZ' or rozkaz == 'JEDĹą'):
                ruch = MoveTo(self.target.position,0)
                for i in shortest_path(G, cAdres, adres.lower()):
                  ruch += MoveTo(miejsca[i], 2)
                self.target.do(ruch)
            if(rozkaz == 'ZATANKUJ'):
                ruch = MoveTo(self.target.position,0)
                for i in shortest_path(G, cAdres, 'stacja'):
                  ruch += MoveTo(miejsca[i], 2)
                self.target.do(ruch)
            if(rozkaz == 'ZAWIEĹą'):
                ruch = MoveTo(self.target.position,0)
                for i in shortest_path(G, cAdres, adres.lower()):
                  ruch += MoveTo(miejsca[i], 2)
                self.target.do(ruch)
            if(rozkaz == 'ODPOCZNIJ'):
                print('Odpoczywam')               

        if(inAction):
            if(self.target.position == miejsca['mickiewicza']):
                paczki['mickiewicza'].opacity = 0
                inAction = False
                cAdres = 'mickiewicza'
                if(cel == 'mickiewicza'):
                  isPack = False
            if(self.target.position == miejsca['orlicza']):
                paczki['orlicza'].opacity = 0
                inAction = False
                cAdres = 'orlicza'
                if(cel == 'orlicza'):
                  isPack = False
            if(self.target.position == miejsca['pascala']):
                paczki['pascala'].opacity = 0
                inAction = False
                cAdres = 'pascala'
                if(cel == 'pascala'):
                  isPack = False
            if(self.target.position == miejsca['kopernika']):
                paczki['kopernika'].opacity = 0
                inAction = False
                cAdres = 'kopernika'
                if(cel == 'kopernika'):
                  isPack = False
            if(self.target.position == miejsca['borsuka']):
                paczki['borsuka'].opacity = 0
                inAction = False
                cAdres = 'borsuka'
            if(self.target.position == miejsca['stacja']):
                inAction = False
                cAdres = 'stacja'
                if(cel == 'borsuka'):
                  isPack = False
            
            # handle input and move the car

        super(DriveCar, self).step(dt)
        scroller.set_focus(self.target.x, self.target.y)


def main():
    global inAction, startAction, doTask, isPack, cel, ruch
    isPack = False
    inAction = False
    doTask = True
    startAction = False
    global scroller
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

    global miejsca
    global paczki
    miejsca = {}
    paczki = {}
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

    paczki['mickiewicza'] = cocos.sprite.Sprite('paczka.png')
    paczki['orlicza'] = cocos.sprite.Sprite('paczka.png')
    paczki['pascala'] = cocos.sprite.Sprite('paczka.png')
    paczki['kopernika'] = cocos.sprite.Sprite('paczka.png')
    paczki['borsuka'] = cocos.sprite.Sprite('paczka.png')
    paczki['mickiewicza'].position = miejsca['mickiewicza']
    paczki['orlicza'].position = miejsca['orlicza']
    paczki['pascala'].position = miejsca['pascala']
    paczki['kopernika'].position = miejsca['kopernika']
    paczki['borsuka'].position = miejsca['borsuka']
    car_layer.add(paczki['mickiewicza'])
    car_layer.add(paczki['orlicza'])
    car_layer.add(paczki['pascala'])
    car_layer.add(paczki['kopernika'])
    car_layer.add(paczki['borsuka'])
    paczki['mickiewicza'].opacity = 0
    paczki['orlicza'].opacity = 0
    paczki['pascala'].opacity = 0
    paczki['kopernika'].opacity = 0
    paczki['borsuka'].opacity = 0
    
    global G
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

    print(shortest_path(G, 'mickiewicza', 'pascala'))
    print( paczki[random.choice(list(paczki))].position )

    short = shortest_path(G, 'mickiewicza', 'pascala')

    car.position = miejsca['start']
    car.rotation = 90
    
    global cAdres
    cAdres = 'start'
    car.do(DriveCar())
    scroller.add(car_layer)
    main_scene = cocos.scene.Scene(scroller)
    director.run(main_scene)

if __name__ == "__main__":
  main()
    
    
    # keyboard = key.KeyStateHandler()
    # director.window.push_handlers(keyboard)

    # def on_key_press(key, modifier):#obsluga klawiatury
    #     if key == pyglet.window.key.Z:
    #         if scroller.scale == 0.25:
    #             scroller.do(actions.ScaleTo(1, 0.5))
    #         else:
    #             scroller.do(actions.ScaleTo(.25, 0.5))
    #     elif key == pyglet.window.key.D:
    #         test_layer.set_debug(True)
    #     elif key == pyglet.window.key.RIGHT:
    #         car.rotation = 90
    #         car.speed = speeed
    #     elif key == pyglet.window.key.LEFT:
    #         car.rotation = -90
    #         car.speed = speeed
    #     elif key == pyglet.window.key.UP:
    #         car.rotation = 0
    #         car.speed = speeed
    #     elif key == pyglet.window.key.DOWN:
    #         car.rotation = 180
    #         car.speed = speeed
    #     elif key == pyglet.window.key.SPACE:
    #         car.speed = 0

    #director.window.push_handlers(on_key_press)


    # def on_key_press(key, modifier):
    #     if key == pyglet.window.key.Z:
    #         if scroller.scale == 1:
    #             scroller.do(actions.ScaleTo(0.3, 1))
    #         else:
    #             scroller.do(actions.ScaleTo(0.3, 1))
    #     elif key == pyglet.window.key.D:
    #        test_layer.set_debug(True)
    #director.window.push_handlers(on_key_press)
