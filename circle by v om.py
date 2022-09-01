from PIL import Image ,ImageDraw

radius = input("please enter the radius of the circle :: ")
color =  input ("color of the circle :: ")

stx =[]
sty =[]

cx = 500
cy = 500

img = Image.new('RGB', (900,900))
draw = ImageDraw.Draw(img)
pixelloader = img.load()

d = (4/5) - float(radius)
x = 0
y = float(radius)

def _draw_scan_lines(x,y):
    if (color == "red"):
        clr = (225, 0, 0)
    elif (color == "blue"):
        clr = (0,0,255)
    elif (color == "black"):
        clr = (255,255,255)
    else :
        clr = (255 , 255 , 0)
    draw.line((cx - x , cy + y , cx + x , cy +y) , fill = clr)
    draw.line((cx - x , cy - y , cx + x ,cy - y), fill = clr)    
    draw.line((cx - y , cy + x , cx + y ,cy + x), fill = clr)    
    draw.line((cx - y , cy - x , cx + y ,cy - x), fill = clr)    

_draw_scan_lines(x,y) 

while (x < y ):
    if (d<0):
        d += 2*x+3
        x += 1
    else :
        d += (2*(x-y)+5)
        x += 1
        y -= 1
    _draw_scan_lines(x,y)

img.show()