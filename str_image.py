from PIL import Image

char_set = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''
im = Image.open('messi.jpg')   
# Image.open对于彩色图像返回后图像模式都为RGB
# Image.open对于灰度图像，打开后模式都为L
im = im.resize((268, 180), Image.ANTIALIAS)
im = im.convert('L')
# L模式为灰色图像
# 后续可以了解各种convert()以及图像模式
im.save('messi-L.jpg')

def get_char(gray):
    if gray >= 240:
        return ' '
    else:
        return char_set[int(gray/((256.0+1)/len(char_set)))]

text = ''
for i in range(im.height):
    for j in range(im.width):
        gray = im.getpixel((j, i))  # getpixel获取图片上像素点的灰度值，返回值
        if isinstance(gray, tuple):
            # ？后续可以了解灰度图像的像素点值
            gray = int(0.2126 * gray[0] + 0.7152 * gray[1] + 
            0.0722 * gray[2])
        text += get_char(gray)
    text += '\n'

with open('pic.txt', 'w') as f:
    f.write(text)