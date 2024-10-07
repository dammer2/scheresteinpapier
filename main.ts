input.onGesture(Gesture.Shake, function () {
    z = randint(0, 100)
    if (z < 34) {
        basic.showLeds(`
            . # . # .
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            `)
    } else if (z < 68) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # . .
            . . . . .
            `)
    } else {
        basic.showLeds(`
            . . . . .
            . . . # #
            . # # . .
            # . . . .
            . . . . .
            `)
    }
    basic.pause(1000)
    basic.clearScreen()
})
let z = 0
basic.showLeds(`
    . # . # .
    . . # . .
    . . # . .
    . . # . .
    . . . . .
    `)
basic.pause(1000)
basic.showLeds(`
    . . . . .
    . # # # .
    . # # # .
    . # # . .
    . . . . .
    `)
basic.pause(1000)
basic.showLeds(`
    . . . . .
    . . . # #
    . # # . .
    # . . . .
    . . . . .
    `)
basic.pause(1000)
basic.clearScreen()
basic.forever(function () {
	
})
