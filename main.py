def on_a_pressed():
    global yellow_speed, blue_speed
    if blue_speed == 0:
        yellow_speed = 0
        blue_speed = 100
        controller.move_sprite(blue, blue_speed, blue_speed)
        controller.move_sprite(yellow, yellow_speed, yellow_speed)
    else:
        yellow_speed = 100
        blue_speed = 0
        controller.move_sprite(blue, blue_speed, blue_speed)
        controller.move_sprite(yellow, yellow_speed, yellow_speed)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

blue_speed = 0
blue: Sprite = None
yellow: Sprite = None
yellow_speed = 0
yellow_speed = 100
yellow = sprites.create(assets.image("""
    myImage
"""), SpriteKind.player)
yellow.set_position(120, 30)
blue = sprites.create(assets.image("""
    myImage0
"""), SpriteKind.player)
blue.set_position(120, 80)
controller.move_sprite(yellow, yellow_speed, yellow_speed)
yellow.set_stay_in_screen(True)
blue.set_stay_in_screen(True)