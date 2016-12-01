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

class DriveCar(actions.Driver):
    def step(self, dt):
        # handle input and move the car

        if keyboard[key.RIGHT]:
            self.target.rotation = 90
            self.target.speed = 100
        if keyboard[key.LEFT]:
            self.target.rotation = -90
            self.target.speed = 100
        if keyboard[key.UP]:
            self.target.rotation = 0
            self.target.speed = 100
        if keyboard[key.DOWN]:
            self.target.rotation = 180
            self.target.speed = 100
        if keyboard[key.SPACE]: self.target.speed = 0
        
        super(DriveCar, self).step(dt)
        scroller.set_focus(self.target.x, self.target.y)

def main():
    global keyboard, scroller
    from cocos.director import director
    director.init(width=800, height=600, autoscale=False, resizable=True)

    car_layer = layer.ScrollableLayer()
    car = cocos.sprite.Sprite('car.png')
    car_layer.add(car)
    car.position = (200, 100)
    car.do(DriveCar())

    scroller = layer.ScrollingManager()
    test_layer = tiles.load('road-map.tmx')['map0']
    scroller.add(test_layer)
    scroller.add(car_layer)

    main_scene = cocos.scene.Scene(scroller)

    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    def on_key_press(key, modifier):
        if key == pyglet.window.key.Z:
            if scroller.scale == 0.75:
                scroller.do(actions.ScaleTo(1, 2))
            else:
                scroller.do(actions.ScaleTo(.75, 2))
        elif key == pyglet.window.key.D:
            test_layer.set_debug(True)
    director.window.push_handlers(on_key_press)

    director.run(main_scene)

if __name__ == '__main__':
    main()
