# String_image
原图效果

![messi](https://user-images.githubusercontent.com/111946478/219236864-c5b73d94-d655-49e7-b2ec-3507832d5fe2.jpg)

字符画效果

![messi_str](https://user-images.githubusercontent.com/111946478/219237125-a17b6b80-1f9a-41d9-80f4-08f9c0c48666.jpeg)

## 实现原理
首先准备一个字符集

```python
char_set = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''
```

然后调用PIL库，将图片转化为灰度图

````python
im = Image.open('messi.jpg')   
# Image.open对于彩色图像返回后图像模式都为RGB
# Image.open对于灰度图像，打开后模式都为L
im = im.resize((268, 180), Image.ANTIALIAS)
im = im.convert('L')
# L模式为灰色图像
# 后续可以了解各种convert()以及图像模式
im.save('messi-L.jpg')
```

灰度图效果

![messi-L](https://user-images.githubusercontent.com/111946478/219238150-195db50f-8447-446d-ac70-7d23ff97788d.jpg)

原图属性显示图片一共有268x180个像素，所以我们需要将268x180个像素的灰度值转化为相对应的字符,将灰度值大于240的都转化为空字符，其他的，按比例映射到字符集上

```python
def get_char(gray):
    if gray >= 240:
        return ' '
    else:
        return char_set[int(gray/((256.0+1)/len(char_set)))]
```

最终效果图

![messi_str](https://user-images.githubusercontent.com/111946478/219239588-2d69c2a5-161b-41b7-be51-9add229674cb.jpeg)

> 建议使用浏览器打开字符画文本，记事本打开显示效果不理想
