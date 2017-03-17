from PIL import Image, ImageFilter
class MyGaussianBlur(ImageFilter.Filter):
    name = "GaussianBlur"
    def __init__(self, radius=2, bounds=None):
        self.radius = radius
        self.bounds = bounds
    def filter(self, image):
        if self.bounds:
            clips = image.crop(self.bounds).gaussian_blur(self.radius)
            image.paste(clips, self.bounds)
            return image
        else:
            return image.gaussian_blur(self.radius)




simg = 'demo.jpg'

image = Image.open(simg)

for x in range(1,12):
    cc=x*10
    image = image.filter(MyGaussianBlur(radius=cc))
    image.save(str(x)+".jpg")




