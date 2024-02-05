# Librairie
from PIL import Image
# Ouvre un fichier image
une_image = Image.open("diamant.png")
# Charge l'image en mémoire
une_image.load()
# Convertit l'image au format RGB
une_image = une_image.convert("RGB")
# Récupère et affiche la couleur du pixel en haut à gauche

pixel_color = []
final = []
for i in range(64):
    for j in range(64):
        vartemp = une_image.getpixel((i,j))
        grayscale = (vartemp[0] * 0.3) + (vartemp[1] * 0.59) + (vartemp[2] * 0.11)
        final.append(((vartemp),grayscale,(i,j)))

class image():
    def __init__(self, img_name):
        self.img = None
        self.img_name = img_name
        self.final_pyxels = []

def open(self):
    self.img = Image.open(f"{self.img_name}")

def get_width(self):
    return self.img.width

def get_height(self):
    return self.img.height

def get_pixel_color(self, i, j):
    return self.img.getpixel((i,j))

def get_pyxel_grayscale(self, pyxel_color):
    return (pyxel_color[0] * 0.3) + (pyxel_color[1] * 0.59) + (pyxel_color[2] * 0.11)

def get_all(self):

    for i in range(self.get_width()):
        for j in range(self.get_height()):
            pyxel_color = self.get_pixel_color(i,j)
        self.grayscale = self.get_pyxel_grayscale(pyxel_color)
    self.final_pyxels.append(((pyxel_color),grayscale,(i,j)))
    return self.final_pyxels


if __name__ == '__main__':
    img = image('diamant.png')
    img.open()
    print(img.get_all())