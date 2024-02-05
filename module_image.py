# Librairie
from PIL import Image
# Ouvre un fichier image
une_image = Image.open("diamant.png")
# Charge l'image en mémoire
une_image.load()
# Convertit l'image au format RGB
une_image = une_image.convert("RGB")
# Récupère et affiche la couleur du pixel en haut à gauche
print(une_image.getpixel((10, 40))) # (255, 255, 255)
print(f"dimensions : {une_image.width}x{une_image.height}")



class Img(self):
    def __init__(self):
        self.une_image = None
        self.nom_image = 
        self.lst_pixels = []

    def open_image(self):
        une_image = Image.open(f"{nom_image}")
    
    def get_width(self):
        return self.une_image.img.width

    def get_height(self):
        return une_image.img.height

    def get_pixel_color(self, i, j):
        pixel_couleur = self.image.getpixel((i, j))
        return pixel_couleur

    def get_pixel_greyscale(self, pixel_couleur):
        return (pixel_couleur[0] * 0.3) + (pixel_couleur[1] * 0.59) + (pixel_couleur[2] * 0.11)

    def get_all(self):
        for i in range(self.get_width()):
            for j in range(self.get_height()):
                pyxel_color = self.get_pixel_color(i,j)
            self.grayscale = self.get_pyxel_grayscale(pyxel_color)
        self.final_pyxels.append(((pyxel_color),grayscale,(i,j)))
