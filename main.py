'''
complex(a,b) = (a+bi)
f(z) = z^2 +c
'''
from PIL import Image
a = int(2*1024)
im = Image.new("RGB", (4*a, 2*a), "black")
pixels = im.load()
size = im.size
z = 0
xlst = list(range(-3*a,a))
ylst = list(range(-a, a))
cs = []
goodcs =[]
def f(z,c) :
    return z**2 +c


for x in xlst:
    x = x/a
    for y in ylst:
        y = y/a
        n = complex(x, y)
        cs.append(n)
for k, c in enumerate(cs):
    z = 0
    for i in range(1,100):
        z = f(z,c)
        if (z.imag ** 2 + z.real ** 2) > 4:
            break

    if (z.imag ** 2 + z.real ** 2) ** 0.5 < 2:
        goodcs.append(c)
coordinates = []
for i in goodcs:
    coordinates.append([i.real, i.imag])

newcoordinates =[]
for i  in coordinates:
    t = [int(i[0]*a +im.size[0]/2),int(im.size[1]/2 - i[1]*a)]
    newcoordinates.append(t)


for i in newcoordinates:
    try:
        pixels[i[0],i[1] ] = (125, 125, 125)
    except IndexError:
        print(f"--->IndexError: {i}")
        pass



im.save("image2.png")




