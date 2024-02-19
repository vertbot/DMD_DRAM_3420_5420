from adafruit_circuitplayground import cp
while True:
    if cp.button_a:
        cp.play_mp3("laugh.mp3")
    elif cp.button_b:
        cp.play_mp3("rimshot.mp3")
