'''complex(a,b) = (a+bi)
f(z) = z^2 +c
'''
from PIL import Image
a = int(2*160)

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
    #print(int((k/len(cs))*1000)/10)
    for i in range(1,50):
        z = f(z,c)
        if (z.imag ** 2 + z.real ** 2) > 4:
            break

    if (z.imag ** 2 + z.real ** 2) ** 0.5 < 2:
        goodcs.append(c)

coords = []
for i in goodcs:
    coords.append([i.real,i.imag])


newcoords =[]
for i  in coords:

    t = [int(i[0]*a +im.size[0]/2),int(im.size[1]/2 - i[1]*a)]
    newcoords.append(t)
print(newcoords)


for i in range(im.size[0]): # for every pixel:
    for j in range(im.size[1]):
        if [i,j] in newcoords :
            pixels[i,j] = (225,225,225)



im.save("image.jpg")
