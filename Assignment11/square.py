import arcade
arcade.Window(500,500,'Square')
arcade.set_background_color(arcade.color.WHITE)
red_color=arcade.color.RED
blue_color=arcade.color.BLUE
center_x=160
center_y=160
arcade.start_render()
count=0
for i in range(10):
    for j in range(10):
        if i%2==0:
            if j%2==0:
                arcade.draw_circle_filled(center_x+count,center_y,8,red_color)
            else:
                arcade.draw_circle_filled(center_x+count, center_y, 8,blue_color)
        else:
            if j%2==0:
                arcade.draw_circle_filled(center_x+count,center_y,8,blue_color)
            else:
                arcade.draw_circle_filled(center_x+count, center_y, 8,red_color)
        count+=20
    count=0
    center_y+=20


arcade.finish_render()
arcade.run()

