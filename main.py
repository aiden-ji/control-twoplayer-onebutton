def on_a_pressed():
    global yellow_speed, blue_speed
    music.play(music.string_playable("C - - - C5 - - - ", 700),
        music.PlaybackMode.IN_BACKGROUND)
    if blue_speed == 0:
        yellow_speed = 0
        blue_speed = 100
        controller.move_sprite(blue, blue_speed, blue_speed)
        controller.move_sprite(yellow, yellow_speed, yellow_speed)
        yellow.set_image(assets.image("""
            myImage1
        """))
        blue.set_image(assets.image("""
            myImage0
        """))
        myAniY.set_position(yellow.x, yellow.y)
        animation.run_image_animation(myAniY, assets.animation("""
            myAnim
        """), 12, False)
    else:
        yellow_speed = 100
        blue_speed = 0
        controller.move_sprite(blue, blue_speed, blue_speed)
        controller.move_sprite(yellow, yellow_speed, yellow_speed)
        blue.set_image(assets.image("""
            myImage2
        """))
        yellow.set_image(assets.image("""
            myImage
        """))
        myAniY.set_position(blue.x, blue.y)
        animation.run_image_animation(myAniY, assets.animation("""
            myAnim0
        """), 12, False)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

blue_speed = 0
blue: Sprite = None
yellow: Sprite = None
yellow_speed = 0
myAniY: Sprite = None
myAniY = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
myAniB = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
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
textSprite = textsprite.create("Swap player with A button", 15, 1)
textSprite.set_position(80, 110)