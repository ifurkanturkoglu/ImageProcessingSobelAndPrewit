##from main import frame_image ???
from PIL import ImageTk, Image
import numpy as np


class edge_detection:
    global image
    global threshold
    global algorihtm

    global gx_image
    global gy_image
    global gsiddet_image

    bg=Image.open("backg.jpg").resize((170, 170))
    bg1=Image.open("backg1.jpg").resize((170, 170))
    bg2 = Image.open("backg2.jpg").resize((170, 170))



    def __init__(self, Selected_image, threshold, algorihtm):

        self.image = Selected_image.convert('L')
        self.threshold = threshold
        self.algorihtm = algorihtm

    def sobel(self):

        Maskx = [[-1, 0, 1],
                 [-2, 0, 2],
                 [-1, 0, 1]]

        Masky = [[1, 2, 1],
                 [0, 0, 0],
                 [-1, -2, -1]]

        self.sobel_gx(Maskx)
        self.sobel_gy(Masky)
        self.sobel_gtoplam(self.gx_image,self.gy_image)

    def sobel_gx(self,Maskx):
        Array = []

        max = 0
        min = 256
        sum = 0
        for y in range(1, self.image.height - 1):
            for x in range(1, self.image.width - 1):
                pixel = self.image.getpixel((x, y))

                for i in range(3):
                    for j in range(3):
                        sum = sum + self.image.getpixel((x - 1 + i, y - 1 + j)) * Maskx[0 + i][0 + j]

                sum = int(sum / 9)
                Array.append(sum)
                if (sum > max):
                    max = sum
                if (min > sum):
                    min = sum
        print(max)
        print(min)
        ekle = ((max) * self.threshold) / 100

        for t in range(len(Array)):

            if (Array[t] > ekle):
                Array[t] = 255

            else:
                Array[t] = 0

        d = 0
        for y in range(1, self.bg.height - 1):
            for x in range(1, self.bg.width - 1):
                self.bg.putpixel((x, y), (Array[d], Array[d], Array[d]))
                d = d + 1
        self.gx_image = self.bg

    def sobel_gy(self,Masky):
        Array = []

        max = 0
        min = 256
        sum = 0
        for y in range(1, self.image.height - 1):
            for x in range(1, self.image.width - 1):
                pixel = self.image.getpixel((x, y))

                for i in range(3):
                    for j in range(3):
                        sum = sum + self.image.getpixel((x - 1 + i, y - 1 + j)) * Masky[0 + i][0 + j]

                sum = int(sum / 9)
                Array.append(sum)
                if (sum > max):
                    max = sum
                if (min > sum):
                    min = sum

        print(max)
        print(min)
        ekle = ((max) * self.threshold) / 100

        for t in range(len(Array)):

            if (Array[t] > ekle):
                Array[t] = 255
            else:
                Array[t] = 0

        d = 0
        for y in range(1, self.bg1.height - 1):
            for x in range(1, self.bg1.width - 1):
                self.bg1.putpixel((x, y), (Array[d], Array[d], Array[d]))
                d = d + 1

        self.gy_image = self.bg1

    def sobel_gtoplam(self,gx_image,gy_image):
        for y in range(gx_image.height ):
            for x in range(gx_image.width ):
                pixel_gx = gx_image.getpixel((x,y))
                pixel_gy = gy_image.getpixel((x,y))
            #    print(pixel_gx[1],pixel_gy)

                if(pixel_gx[1]==255 or pixel_gy[1]==255 or pixel_gx[1]==253 or pixel_gy[1]==253):
                    self.bg2.putpixel((x, y),(255,255,255))
                else:
                    self.bg2.putpixel((x, y), (0, 0, 0))

        self.gsiddet_image = self.bg2


    def prewitt(self):
        Maskx = [[-1, 0, 1],
                 [-1, 0, 1],
                 [-1, 0, 1]]

        Masky = [[1, 1, 1],
                 [0, 0, 0],
                 [-1, -1, -1]]

        self.prewitt_gx(Maskx)
        self.prewitt_gy(Masky)
        self.prewitt_gtoplam(self.gx_image, self.gy_image)

    def prewitt_gx(self, Maskx):
        Array = []

        max = 0
        min = 256
        sum = 0
        for y in range(1, self.image.height - 1):
            for x in range(1, self.image.width - 1):
                pixel = self.image.getpixel((x, y))

                for i in range(3):
                    for j in range(3):
                        sum = sum + self.image.getpixel((x - 1 + i, y - 1 + j)) * Maskx[0 + i][0 + j]

                sum = int(sum / 9)
                Array.append(sum)
                if (sum > max):
                    max = sum
                if (min > sum):
                    min = sum
        print(max)
        print(min)
        ekle = ((max) * self.threshold) / 100

        for t in range(len(Array)):

            if (Array[t] > ekle):
                Array[t] = 255

            else:
                Array[t] = 0

        d = 0
        for y in range(1, self.bg.height - 1):
            for x in range(1, self.bg.width - 1):
                self.bg.putpixel((x, y), (Array[d], Array[d], Array[d]))
                d = d + 1
        self.gx_image = self.bg

    def prewitt_gy(self, Masky):
        Array = []

        max = 0
        min = 256
        sum = 0
        for y in range(1, self.image.height - 1):
            for x in range(1, self.image.width - 1):
                pixel = self.image.getpixel((x, y))

                for i in range(3):
                    for j in range(3):
                        sum = sum + self.image.getpixel((x - 1 + i, y - 1 + j)) * Masky[0 + i][0 + j]

                sum = int(sum / 9)
                Array.append(sum)
                if (sum > max):
                    max = sum
                if (min > sum):
                    min = sum

        print(max)
        print(min)
        ekle = ((max) * self.threshold) / 100

        for t in range(len(Array)):

            if (Array[t] > ekle):
                Array[t] = 255
            else:
                Array[t] = 0

        d = 0
        for y in range(1, self.bg1.height - 1):
            for x in range(1, self.bg1.width - 1):
                self.bg1.putpixel((x, y), (Array[d], Array[d], Array[d]))
                d = d + 1

        self.gy_image = self.bg1

    def prewitt_gtoplam(self, gx_image, gy_image):
        for y in range(gx_image.height ):
            for x in range(gx_image.width ):

                pixel_gx = gx_image.getpixel((x,y))
                pixel_gy = gy_image.getpixel((x,y))


                if(pixel_gx[1]==255 or pixel_gy[1]==255 or pixel_gx[1]==253 or pixel_gy[1]==253):
                    self.bg2.putpixel((x, y),(255,255,255))
                else:
                    self.bg2.putpixel((x, y), (0, 0, 0))

        self.gsiddet_image = self.bg2

