def on_gesture_shake():
    global z
    z = randint(0, 100)
    if z < 34:
        basic.show_leds("""
            . # . # .
                        . . # . .
                        . . # . .
                        . . # . .
                        . . . . .
        """)
    else:
        if z < 68:
            basic.show_leds("""
                . . . . .
                                . # # # .
                                . # # # .
                                . # # . .
                                . . . . .
            """)
        else:
            basic.show_leds("""
                . . . . .
                                . . . # #
                                . # # . .
                                # . . . .
                                . . . . .
            """)
    basic.pause(1000)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

z = 0
basic.show_leds("""
    . # . # .
        . . # . .
        . . # . .
        . . # . .
        . . . . .
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        . # # # .
        . # # # .
        . # # . .
        . . . . .
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        . . . # #
        . # # . .
        # . . . .
        . . . . .
""")
basic.pause(1000)
basic.clear_screen()

def on_forever():
    pass
basic.forever(on_forever)
