from RTetris import Tetris

config = {
    'scale':    1,
    'cols':     10,
    'rows':     16,
}

p1 = Tetris(config["rows"], config["cols"],config["scale"])

print(p1.drawMatrix()) 
print("Next")
p1.newShape()
p1.play("DOWN")
print(p1.drawMatrix())
print("Next")
p1.play("DOWN")
print(p1.drawMatrix())











