##from __future__ import division, print_function, unicode_literals

# This code is so you can run the samples without installing the package
##import sys
##import os
##import time
##sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
##
##testinfo = "s, q"
##tags = "tiles, Driver"

##pyglet.resource.path.append(pyglet.resource.get_script_home())
##pyglet.resource.reindex()

import pyglet
from pyglet.window import key
import cocos
from cocos import tiles, actions, layer, collision_model as cm

##global
speeed = 666
collision_manager = cm.CollisionManagerBruteForce() #menager kolizji
orlenColl = cm.CollisionManagerBruteForce() #menager kolizji dla stacji paliw
x = 0
##/global

class DriveCar(actions.Driver):
    def step(self, dt):
        orlen = set(orlenColl.known_objs())
        global x 
                    
        collisions = set(collision_manager.objs_colliding(self.target))
        if collisions is not None:
            if orlen.intersection(collisions): #jesli z ktoras ze stacji wystepuje kolizja
                print("Witamy na stacji!" + str(x))
                x += 1
                        
        self.target.cshape.center = self.target.position #aktualizacja pozycji Cshape

        super(DriveCar, self).step(dt)
        scroller.set_focus(self.target.x, self.target.y)

def main():
    global keyboard, scroller
    from cocos.director import director
    director.init(width=800, height=600, autoscale=False, resizable=True)
    
    petrol = tiles.load('road-map.tmx')['petrol']
    for i in range(2): #ustawienie kolizji dla stacji paliw
        petrol.objects[i].x = petrol.objects[i].x+64
        petrol.objects[i].y = petrol.objects[i].y+64
        petrol.objects[i].cshape = cm.AARectShape(
            petrol.objects[i].position,
            petrol.objects[i].width//2,
            petrol.objects[i].height//2
        )
        orlenColl.add(petrol.objects[i])
        collision_manager.add(petrol.objects[i])

    car_layer = layer.ScrollableLayer()
    car = cocos.sprite.Sprite('car.png')
    car_layer.add(car)
    car.position = (3584, 1280)
    car.cshape = cm.AARectShape(
        car.position,
        car.width//2,
        car.height//2
    )
    collision_manager.add(car) #dodanie auta do managera kolizji

    scroller = layer.ScrollingManager()
    test_layer = tiles.load('road-map.tmx')['map0']
    scroller.add(test_layer)
    scroller.add(car_layer)
    scroller.do(actions.ScaleTo(.25, 0.5))
    
    car.do(DriveCar())##DRIVE    

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
