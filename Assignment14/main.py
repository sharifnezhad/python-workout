import random
import arcade
import time
RIGHT_FACING = 0
LEFT_FACING = 1
UPDATES_PER_FRAME = 2
def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]

class Game (arcade.View):
    def __init__(self):
        super().__init__()
        self.player=Player()
        self.gravity=0.4
        self.ground_list=arcade.SpriteList()
        self.enemy_list=arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.time_start=time.time()
        for i in range(0,1000,80):
            ground=Ground(i,20)
            self.ground_list.append(ground)
        for i in range(300,700,80):
            ground=Ground(i,250)
            self.ground_list.append(ground)
        for i in range(80,300,80):
            ground=Ground(i,450)
            self.ground_list.append(ground)
        self.physics_engine=arcade.PhysicsEnginePlatformer(self.player,self.ground_list,gravity_constant=self.gravity)
        self.enemy_physics_engine_list=[]
        self.key=arcade.Sprite(':resources:images/items/keyYellow.png')
        self.key.center_x=random.randint(320,600)
        self.key.center_y=320
        self.key.width=48
        self.key.height=48
        self.lock=arcade.Sprite(':resources:images/tiles/lockYellow.png')
        self.lock.center_x=random.randint(80,260)
        self.lock.center_y=520
        self.lock.width = 48
        self.lock.height = 48
        self.found=False
        self.you_win=You_win(800,600,self)
        self.setup()
    def on_draw(self):
        arcade.start_render()
        background_image = arcade.load_texture('image/Birds-Star-Wars-Background.png')
        arcade.draw_lrwh_rectangle_textured(0, 0, 800, 600, background_image)
        self.player.draw()
        self.enemy_list.draw()
        for ground in self.ground_list:
            ground.draw()
        self.lock.draw()
        self.key.draw()
        for i in range(len(self.player.heart_list)):
            arcade.Sprite('heart.png',center_x=650+50*i,center_y=30,image_width=48,image_height=48).draw()

    def setup(self):
        self.player_list.append(self.player)
    def on_update(self, delta_time: float):

        self.physics_engine.update()
        self.player_list.update_animation()
        self.enemy_list.update_animation()
        for item in self.enemy_physics_engine_list:
            item.update()
        time_end=time.time()
        if time_end-self.time_start>3:
            new_enemy=Enemy()
            self.enemy_list.append(new_enemy)
            self.enemy_physics_engine_list.append(arcade.PhysicsEnginePlatformer(new_enemy,self.ground_list,gravity_constant=self.gravity))
            self.time_start=time.time()
        for enemy in self.enemy_list:
            # collision=
            if arcade.check_for_collision(self.player,enemy):
                if len(self.player.heart_list)==0:
                    self.window.show_view(Gameover(800,600,self))
                else:
                    del self.player.heart_list[0]
                    enemy.remove_from_sprite_lists()

        if arcade.check_for_collision(self.player,self.key) and self.found==False:
            self.found=True
            self.key.remove_from_sprite_lists()
        if arcade.check_for_collision(self.player,self.lock) and self.found==True:
            self.window.show_view(self.you_win)

    def on_key_press(self, key, modifiers: int):
        if key==arcade.key.LEFT:
            self.player.change_x=-1*self.player.speed
        elif key==arcade.key.RIGHT:
            self.player.change_x=1*self.player.speed
        elif key==arcade.key.UP and self.physics_engine.can_jump():
                self.player.change_y=15
                self.player.change_x=0
    def on_key_release(self, key, _modifiers: int):
        self.player.change_x = 0
        # self.player.change_y = 0

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture=arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png')
        self.center_x=100
        self.center_y=200
        self.speed=4
        # self.change_x=0
        self.cur_texture = 0
        self.character_face_direction = RIGHT_FACING
        self.walk_textures = []
        for i in range(7):
            texture = load_texture_pair(f":resources:images/animated_characters/male_adventurer/maleAdventurer_walk{i}.png")
            self.walk_textures.append(texture)
        self.heart_list=[1,2,3]
    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Idle animation
        if self.change_x == 0 :
            self.texture=arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png')
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7 :
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = self.walk_textures[frame][direction]
class Ground(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__(':resources:images/tiles/grassMid.png')
        self.center_x=x
        self.center_y=y
        self.width=80
        self.height=80
class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture=arcade.load_texture(':resources:images/animated_characters/zombie/zombie_idle.png')
        self.center_x=random.randint(0,800)
        self.center_y=500
        self.speed=2
        self.change_x=random.choice([-1,1])*self.speed
        self.cur_texture = 0
        self.character_face_direction = RIGHT_FACING
        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f":resources:images/animated_characters/zombie/zombie_walk{i}.png")
            self.walk_textures.append(texture)
    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Idle animation
        if self.change_x == 0 :
            self.texture = arcade.load_texture(':resources:images/animated_characters/zombie/zombie_idle.png')
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7 :
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = self.walk_textures[frame][direction]
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
window=arcade.Window(800,600,'selver spacecraft')
game=Game()
window.show_view(game)
arcade.run()

list=['maleAdventurer_walk0.png','maleAdventurer_walk1.png','maleAdventurer_walk2.png','maleAdventurer_walk3.png','maleAdventurer_walk4.png','maleAdventurer_walk5.png','maleAdventurer_walk6.png']