import cv2
import numpy as np
from Crypto.Cipher import AES


class EncryptImage:
    def __init__(self,path):
        self.img=cv2.imread(path)

    def displayImage(self):
        if self.img is None:
            print('Unable to open image')
            return
        cv2.imshow("image", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def encrypt(self):
        pixels=[]
        pix_string = ""
        m=len(self.img)
        n=len(self.img[0])
        for i in range(m):
            for j in range(n):
                rgbvals= [bin(self.img[i][j][0])[2:], bin(self.img[i][j][1])[2:], bin(self.img[i][j][2])[2:]]
                pixels.append(rgbvals)
                ##
                pix_string += bin(self.img[i][j][0])[2:] + bin(self.img[i][j][1])[2:] + bin(self.img[i][j][2])[2:]
        if not len(pix_string)%16==0:
            pix_string+='0'*(16-(len(pix_string)%16))
        key=b'1000100011100101'
        cipher=AES.new(key,AES.MODE_ECB)
        ciphertext=cipher.encrypt(bytearray(pix_string,'utf-8'))
        print(ciphertext)
        '''print(pixels[0], '\n', pixels[2])

        ##
        print(pix_string)
        print(np.shape(self.img))

        # swapping
        for i in range(0, m * n // 2, 2):
            pixels[i], pixels[m * n - i - 1] = pixels[m * n - i - 1], pixels[i]
        # construct image
        t = 0
        for i in range(m):
            for j in range(n):
                self.img[i][j][0] = int(pixels[t][0], 2)
                self.img[i][j][1] = int(pixels[t][1], 2)
                self.img[i][j][2] = int(pixels[t][2], 2)
                t = t + 1
        '''
    def decrypt(self):
        # following things are somewhat unnecessary to decrypt given image,
        # only simple swap could have gotten the image back without going into the
        # pixels thing, but written for future encryption considerations
        pixels = []
        m = len(self.img)
        n = len(self.img[0])
        for i in range(m):
            for j in range(n):
                rgbvals = [bin(self.img[i][j][0])[2:], bin(self.img[i][j][1])[2:], bin(self.img[i][j][2])[2:]]
                pixels.append(rgbvals)
        print(pixels[0], '\n', pixels[2])
        # swapping
        for i in range(0, m * n // 2, 2):
            pixels[i], pixels[m * n - i - 1] = pixels[m * n - i - 1], pixels[i]
        # construct image
        t = 0
        for i in range(m):
            for j in range(n):
                self.img[i][j][0] = int(pixels[t][0], 2)
                self.img[i][j][1] = int(pixels[t][1], 2)
                self.img[i][j][2] = int(pixels[t][2], 2)
                t = t + 1


if __name__=='__main__':
    image=EncryptImage(r'C:/Users/USER19/PycharmProjects/python_assignments/NetworkSecurity/image4.bmp')
    #image.displayImage()
    image.encrypt()
    #image.displayImage()
    #image.decrypt()
    #image.displayImage()
