import random
import arcade
import math
import time
PARTICLE_GRAVITY = 0.05
PARTICLE_FADE_RATE = 8
PARTICLE_MIN_SPEED = 2.5
PARTICLE_SPEED_RANGE = 2.5
PARTICLE_COUNT = 20
PARTICLE_RADIUS = 3
PARTICLE_COLORS = [arcade.color.ALIZARIN_CRIMSON,
                   arcade.color.COQUELICOT,
                   arcade.color.LAVA,
                   arcade.color.KU_CRIMSON,
                   arcade.color.DARK_TANGERINE]

PARTICLE_SPARKLE_CHANCE = 0.02
SMOKE_START_SCALE = 0.25
SMOKE_EXPANSION_RATE = 0.03
SMOKE_FADE_RATE = 7
SMOKE_RISE_RATE = 0.5
SMOKE_CHANCE = 0.25

class Game (arcade.View):
    def __init__(self):
        super().__init__()
        self.rocket_me=SpaceCraft(800)
        self.enemy_list=[]
        self.start_time=time.time()
        self.speed = 4
        self.enemy=Enemy(800,600,self.speed)
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.enemy_shot_list=[]
        self.gameover=Gameover(800,600,self)
        self.you_win=You_win(800,600,self)
        self.sound_explode = arcade.load_sound(':resources:sounds/explosion2.wav')
        self.giant_enemy=Giant_enemy(800,600)
        self.giant_list=arcade.SpriteList()
        self.smoke = Smoke(50)
        self.explosions_list=arcade.SpriteList()

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK)
        background_image = arcade.load_texture(':resources:images/backgrounds/stars.png')
        arcade.draw_lrwh_rectangle_textured(0, 0, 800, 600, background_image)
        self.rocket_me.draw()
        for i in range(len(self.rocket_me.bullet_list)):
            self.rocket_me.bullet_list[i].draw()
        if self.rocket_me.score>=10:
            self.giant_enemy.draw()
            arcade.draw_xywh_rectangle_filled(10,570,self.giant_enemy.heart_giant,20,arcade.color.GREEN)
            for i in range(len(self.giant_enemy.giant_bullet_list)):
                self.giant_enemy.giant_bullet_list[i].draw()
        else:
            for i in range(len(self.enemy_list)):
                self.enemy_list[i].draw()
        arcade.draw_text('Score: %s' % self.rocket_me.score, 10, 20, self.rocket_me.color)
        for i in range(len(self.rocket_me.heart)):
            arcade.Sprite('heart.png',center_x=650+50*i,center_y=30,image_width=48,image_height=48).draw()
        self.explosions_list.draw()
    def on_update(self, delta_time: float):
        self.explosions_list.update()
        self.rocket_me.rotate()
        self.rocket_me.move()
        for i in range(len(self.rocket_me.bullet_list)):
            self.rocket_me.bullet_list[i].move()
        for bullet in self.rocket_me.bullet_list:
            if bullet.center_x>800 or bullet.center_y>600 or bullet.center_x<0:
                bullet.remove_from_sprite_lists()
        self.end_time = time.time()
        if self.rocket_me.score<10:
            t=random.randint(2,8)
            if self.end_time-self.start_time>t:
                self.enemy_list.append(Enemy(800, 600,self.speed))
                self.start_time=time.time()

            for i in range(len(self.enemy_list)):
                self.enemy_list[i].move()
                if self.enemy_list[i-1].center_y<=0:
                    self.enemy_list[i-1].remove_from_sprite_lists()
                    if self.rocket_me.heart==[]:
                        self.window.show_view(self.gameover)
                    else:
                        del (self.rocket_me.heart[0])

            for bullet in self.rocket_me.bullet_list:
                self.enemy_shot_list=arcade.check_for_collision_with_list(bullet, self.enemy_list)
                for enamy in self.enemy_shot_list:
                    bullet.remove_from_sprite_lists()
                    arcade.play_sound(self.sound_explode)
                    self.rocket_me.score += 1
                    if self.speed==8:
                        self.speed=2
                    else:
                        self.speed+=1
                    for i in range(PARTICLE_COUNT):
                        particle = Particle(self.explosions_list)
                        particle.position = enamy.position
                        self.explosions_list.append(particle)

                    smoke = Smoke(50)
                    smoke.position = enamy.position
                    self.explosions_list.append(smoke)
                    enamy.remove_from_sprite_lists()



        else:
            self.giant_list = self.giant_enemy
            self.giant_enemy.move(800)
            t = random.randint(2, 8)
            if self.end_time-self.start_time>t:
                self.giant_enemy.fire()
                self.start_time=time.time()

            for i in range(len(self.giant_enemy.giant_bullet_list)):
                self.giant_enemy.giant_bullet_list[i].move()
            for i in range(len(self.rocket_me.bullet_list)):
                try:
                    if arcade.check_for_collision(self.rocket_me.bullet_list[i], self.giant_enemy):
                        self.rocket_me.bullet_list.pop(i)
                        if self.giant_enemy.heart_giant<0:
                            self.window.show_view(self.you_win)
                        else:
                            self.giant_enemy.heart_giant-=50
                except:
                    pass
            for i in range(len(self.giant_enemy.giant_bullet_list)):
                if arcade.check_for_collision(self.giant_enemy.giant_bullet_list[i],self.rocket_me):
                    del self.giant_enemy.giant_bullet_list[i]
                    if self.rocket_me.heart==[]:
                        self.window.show_view(self.gameover)
                    else:
                        del (self.rocket_me.heart[0])




    def on_key_press(self, key, _modifiers: int):
        if key==arcade.key.RIGHT:
            self.rocket_me.change_angle=-1
        elif key== arcade.key.LEFT:
            self.rocket_me.change_angle=1
        elif key==arcade.key.SPACE:
            self.rocket_me.fire()

        elif key==arcade.key.D:
            self.rocket_me.change_x=1

        elif key==arcade.key.A:
            self.rocket_me.change_x=-1



    def on_key_release(self, key, _modifiers: int):
        self.rocket_me.change_angle=0
        self.rocket_me.change_x = 0
class Enemy (arcade.Sprite):
    def __init__(self,w,h,speed):
        super().__init__(':resources:images/space_shooter/playerShip3_orange.png')
        self.center_x=random.randint(0,w)
        self.center_y=h
        self.angle=180
        self.width=48
        self.height=48
        self.speed=speed

    def move(self):
        self.center_y-=self.speed
class SpaceCraft (arcade.Sprite):
    def __init__(self,w):
        super().__init__(':resources:images/space_shooter/playerShip1_green.png')
        self.width = 48
        self.height = 48
        self.center_x = w // 2
        self.center_y = 48
        self.angle=0
        self.change_angle=0
        self.bullet_list=[]
        self.speed=4
        self.score=0
        self.heart=[1,2,3]
        self.sound_fire=arcade.load_sound(':resources:sounds/fall2.wav')
        self.change_x=0
        # self.change_y=0

    def rotate(self):
        self.angle+=self.change_angle*self.speed
    def move(self):
        self.center_x+=self.speed*self.change_x
        # self.center_y+=self.speed*self.change_y
    def fire(self):
        self.bullet_list.append(Bullet(self))
        arcade.play_sound(self.sound_fire)
class Bullet (arcade.Sprite):
    def __init__(self,rocket):
        super().__init__(':resources:images/space_shooter/laserRed01.png')
        self.speed=10
        self.angle=rocket.angle
        self.center_x=rocket.center_x
        self.center_y=rocket.center_y
        self.game=Game()
    def move(self):
        angle_rad=math.radians(self.angle)
        self.center_x-=int(self.speed* math.sin(angle_rad))
        self.center_y+=int(self.speed* math.cos(angle_rad))
class Giant_enemy(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__(':resources:images/space_shooter/playerShip3_orange.png')
        self.angle=180
        self.angle_bullet=90
        self.center_x=w//2
        self.center_y=h
        self.speed=4
        self.width=150
        self.height=150
        self.center_bullet_x=w//2
        self.center_bullet_y=h//2
        self.giant_bullet_list=[]
        self.heart_giant=780
    def move(self,heith):
        if self.center_y>= heith//2:
            self.center_y-=self.speed
    def fire(self):
        self.angle_bullet = random.randint(90,270)
        self.giant_bullet_list.append(Giant_bullet(self))
class Giant_bullet (arcade.Sprite):
    def __init__(self,rocket):
        super().__init__(':resources:images/space_shooter/laserRed01.png')
        self.speed=10
        self.angle=rocket.angle_bullet
        self.center_x=rocket.center_x
        self.center_y=rocket.center_y
        self.game=Game()
    def move(self):
        angle_rad=math.radians(self.angle)
        self.center_x-=int(self.speed* math.sin(angle_rad))
        self.center_y+=int(self.speed* math.cos(angle_rad))
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
class You_win(arcade.View):
    def __init__(self,w,h,gameview):
        super().__init__()
        self.center_x=w//2
        self.center_y=h//2
        self.color=arcade.color.BLACK
        self.game_view=gameview
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('YOU WIN',self.center_x-100,self.center_y,self.color,30,15,bold=True)
        arcade.draw_text('Press the T button to play again',self.center_x-150,self.center_y-50,self.color,20,15)
    def on_key_press(self, key, modifiers: int):
        if key==arcade.key.T:
            self.window.show_view(Game())
class Smoke(arcade.SpriteCircle):
    """ This represents a puff of smoke """
    def __init__(self, size):
        super().__init__(size, arcade.color.LIGHT_GRAY, soft=True)
        self.change_y = SMOKE_RISE_RATE
        self.scale = SMOKE_START_SCALE

    def update(self):
        """ Update this particle """
        if self.alpha <= PARTICLE_FADE_RATE:
            # Remove faded out particles
            self.remove_from_sprite_lists()
        else:
            # Update values
            self.alpha -= SMOKE_FADE_RATE
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.scale += SMOKE_EXPANSION_RATE
class Particle(arcade.SpriteCircle):
    """ Explosion particle """
    def __init__(self, my_list):
        # Choose a random color
        color = random.choice(PARTICLE_COLORS)

        # Make the particle
        super().__init__(PARTICLE_RADIUS, color)

        # Track normal particle texture, so we can 'flip' when we sparkle.
        self.normal_texture = self.texture

        # Keep track of the list we are in, so we can add a smoke trail
        self.my_list = my_list

        # Set direction/speed
        speed = random.random() * PARTICLE_SPEED_RANGE + PARTICLE_MIN_SPEED
        direction = random.randrange(360)
        self.change_x = math.sin(math.radians(direction)) * speed
        self.change_y = math.cos(math.radians(direction)) * speed

        # Track original alpha. Used as part of 'sparkle' where we temp set the
        # alpha back to 255
        self.my_alpha = 255

        # What list do we add smoke particles to?
        self.my_list = my_list

    def update(self):
        """ Update the particle """
        if self.my_alpha <= PARTICLE_FADE_RATE:
            # Faded out, remove
            self.remove_from_sprite_lists()
        else:
            # Update
            self.my_alpha -= PARTICLE_FADE_RATE
            self.alpha = self.my_alpha
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.change_y -= PARTICLE_GRAVITY

            # Should we sparkle this?
            if random.random() <= PARTICLE_SPARKLE_CHANCE:
                self.alpha = 255
                self.texture = arcade.make_circle_texture(int(self.width),
                                                          arcade.color.WHITE)
            else:
                self.texture = self.normal_texture

            # Leave a smoke particle?
            if random.random() <= SMOKE_CHANCE:
                smoke = Smoke(5)
                smoke.position = self.position
                self.my_list.append(smoke)


window=arcade.Window(800,600,'selver spacecraft')
game=Game()
window.show_view(game)
arcade.run()