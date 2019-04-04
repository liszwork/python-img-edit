# -*- coding: utf-8 -*-
from PIL import Image
import os

imgName = 'img.png'
imgDir = os.getcwd() + '\\'

class ImgInfo:
    def __init__(self, name, sx, sy, ex, ey):
        self.name = name + '.png'
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
    def carving(self):
        # 画像を切り出して保存
        baseFile = imgDir + imgName
        img = Image.open(baseFile)
        imgCrop = img.crop((self.sx, self.sy, self.ex, self.ey))
        output = imgDir + self.name
        imgCrop.save(output)
    def show(self):
        # 情報表示
        print('[{}] {: >4}, {: >4}, {: >4}, {: >4}'.format(self.name, self.sx, self.sy, self.ex, self.ey))

def getOfsList(num, size):
    ofs = []
    for i in range(0, num):
        ofs.append(i * size)
    return ofs

if __name__ == '__main__':
    # イメージの始点
    startX = 5
    startY = 5
    # イメージの幅、高さ
    imgW = 120
    imgH = 120
    #
    xofs = getOfsList(4, imgW)
    yofs = getOfsList(4, imgH)
    # 画像情報
    imgs = []
    cnt = 0
    ycnt = 1
    for y in yofs:
        xcnt = 1
        for x in xofs:
            name = str(cnt).zfill(2)
            sx = x + startX
            sy = y + startY
            ex = (imgW * xcnt) + startX
            ey = (imgH * ycnt) + startY
            img = ImgInfo(name, sx, sy, ex, ey)
            imgs.append(img)
            cnt += 1
            xcnt += 1
        ycnt += 1
    # 確認
    for img in imgs:
        img.show()
    # 分割
    for img in imgs:
        img.carving()
