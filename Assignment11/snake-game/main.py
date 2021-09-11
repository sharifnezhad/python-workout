import random
import time
import arcade
import os

class Game(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.EERIE_BLACK)
        self.snake=Snake(760,540)
        self.apple=Apple(760,540)
        self.pear=Pear(760,540)
        self.poop = Poop(760, 540)
        self.gameover=Gameover(800,600,self)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(400,300,750,500,arcade.color.WHEAT)
        arcade.draw_text('Score: %s'% self.snake.score,10,20,self.snake.color)
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.poop.draw()

    def on_update(self, delta_time: float):
        count=0
        self.snake.move()

        if arcade.check_for_collision(self.snake,self.apple):
            self.snake.eat(0)
            self.apple=Apple(760,540)
            self.snake.len += 3
            self.snake.draw()

        elif self.snake.center_x<=28 or self.snake.center_x>=770 or self.snake.center_y>=548 or self.snake.center_y<=48:
            self.window.show_view(self.gameover)
        elif arcade.check_for_collision(self.snake,self.pear):
            self.snake.eat(1)
            self.pear=Pear(760,540)
            self.snake.len += 3
            self.snake.draw()
        elif arcade.check_for_collision(self.snake,self.poop):
            self.snake.eat(2)
            self.snake.len -= 3
            if self.snake.score<0:
                self.window.show_view(self.gameover)
            self.poop=Poop(760,540)

            self.snake.draw()


    def on_key_press(self, key, modifiers):
        if key==arcade.key.UP:
            self.snake.change_x=0
            self.snake.change_y=1
        elif key==arcade.key.DOWN:
            self.snake.change_x=0
            self.snake.change_y=-1
        elif key== arcade.key.RIGHT:
            self.snake.change_x=1
            self.snake.change_y=0
        elif key==arcade.key.LEFT:
            self.snake.change_x=-1
            self.snake.change_y=0
        else:
            self.snake.change_x=0
            self.snake.change_y=0

class Snake(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__()
        self.width=16
        self.height=16
        self.r=8
        self.center_x=w//2
        self.center_y=h//2
        self.change_x=0
        self.change_y=0
        self.color=arcade.color.WHITE
        self.speed=4
        self.score=0
        self.body=[]
        self.len=0
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,8,self.color)
        self.body.append([self.center_x,self.center_y])
        for i in self.body:
            arcade.draw_circle_filled(i[0], i[1], 8, self.color)
        if len(self.body)>self.len:
            self.body.pop(0)
    def move(self):
        self.center_x+=self.speed*self.change_x
        self.center_y+=self.speed*self.change_y
    def eat(self,x):
        if x==0:
            self.score+=1
        elif x==1:
            self.score += 2
        elif x==2:
            self.score-=1
class Apple(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__()
        self.color=arcade.color.RED
        self.width=16
        self.height=16
        self.r=8
        self.apple_img=arcade.Sprite('images/apple.png')
        self.apple_img.center_x=self.center_x=random.randint(30,w)
        self.apple_img.center_y=self.center_y=random.randint(50,h)
    def draw(self):
        self.apple_img.draw()
class Pear (arcade.Sprite):
    def __init__(self,w,h):
        super().__init__()
        self.color=arcade.color.RED
        self.width=16
        self.height=16
        self.r=8
        self.pear_img = arcade.Sprite('images/pear.png')
        self.pear_img.center_x=self.center_x=random.randint(30,w)
        self.pear_img.center_y=self.center_y=random.randint(50,h)


    def draw(self):
        self.pear_img.draw()
class Poop (arcade.Sprite):
    def __init__(self,w,h):
        super().__init__()
        self.color=arcade.color.RED
        self.width=16
        self.height=16
        self.r=8
        self.poop_img = arcade.Sprite('images/poop.png')
        self.poop_img.center_x=self.center_x=random.randint(30,w)
        self.poop_img.center_y=self.center_y=random.randint(50,h)


    def draw(self):
        self.poop_img.draw()
class Gameover (arcade.View):
    def __init__(self,w,h,gameview):
        super().__init__()
        self.center_x=w//2
        self.center_y=h//2
        self.color=arcade.color.BLACK
        self.game_view=gameview
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE)

    def on_draw(self):
        arcade.start_render()


        arcade.draw_text('GAME OVER',self.center_x-100,self.center_y,self.color,30,15,bold=True)
        arcade.draw_text('Press the T button to play again',self.center_x-150,self.center_y-50,self.color,20,15)
    def on_key_press(self, key, modifiers: int):
        if key==arcade.key.T:
            self.window.show_view(Game())

window = arcade.Window(800,600,'Snake Game')
game=Game()
window.show_view(game)
arcade.run()
