controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    game.reset()
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    music.play(music.stringPlayable("C - - - C5 - - - ", 700), music.PlaybackMode.InBackground)
    if (blue_speed == 0) {
        yellow_speed = 0
        blue_speed = 100
        controller.moveSprite(blue, blue_speed, blue_speed)
        controller.moveSprite(yellow, yellow_speed, yellow_speed)
        yellow.setImage(assets.image`
            myImage1
        `)
        blue.setImage(assets.image`
            myImage0
        `)
        myAniY.setPosition(yellow.x, yellow.y)
        animation.runImageAnimation(myAniY, assets.animation`
            myAnim
        `, 12, false)
    } else {
        yellow_speed = 100
        blue_speed = 0
        controller.moveSprite(blue, blue_speed, blue_speed)
        controller.moveSprite(yellow, yellow_speed, yellow_speed)
        blue.setImage(assets.image`
            myImage2
        `)
        yellow.setImage(assets.image`
            myImage
        `)
        myAniY.setPosition(blue.x, blue.y)
        animation.runImageAnimation(myAniY, assets.animation`
            myAnim0
        `, 12, false)
    }
    
})
let blue_speed = 0
let yellow : Sprite = null
let blue : Sprite = null
let yellow_speed = 0
let myAniY : Sprite = null
myAniY = sprites.create(img`
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
    `, SpriteKind.Player)
let myAniB = sprites.create(img`
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
    `, SpriteKind.Player)
yellow_speed = 100
blue = sprites.create(assets.image`
    myImage3
`, SpriteKind.Player)
blue.setPosition(120, 80)
yellow = sprites.create(assets.image`
    myImage
`, SpriteKind.Player)
yellow.setPosition(120, 30)
controller.moveSprite(yellow, yellow_speed, yellow_speed)
yellow.setStayInScreen(true)
blue.setStayInScreen(true)
let textSprite = textsprite.create("Swap player with A button", 15, 1)
textSprite.setPosition(80, 110)
