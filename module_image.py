# Librairie
from PIL import Image
# Ouvre un fichier image
une_image = Image.open("diamant.png")
# Charge l'image en mémoire
une_image.load()
# Convertit l'image au format RGB
une_image = une_image.convert("RGB")
# Récupère et affiche la couleur du pixel en haut à gauche
print(une_image.getpixel((40, 50))) # (255, 255, 255)
print(f"dimensions : {une_image.width}x{une_image.height}")



class Img():
    def __init__(self, nom_image ):
        self.une_image = None
        self.nom_image = nom_image
        self.lst_pixels = []
        self.une_image = Image.open(f"{nom_image}")
    
    def get_width(self):
        return self.une_image.width

    def get_height(self):
        return self.une_image.height

    def get_pixel_color(self, i, j):
        pixel_couleur = self.une_image.getpixel((i, j))
        return pixel_couleur

    def get_pixel_greyscale(self, pixel_couleur):
        return (pixel_couleur[0] * 0.3) + (pixel_couleur[1] * 0.59) + (pixel_couleur[2] * 0.11)

    def get_all(self):
        """Obtenir la """
        for i in range(self.get_width()):
            for j in range(self.get_height()):
                couleur_pyxel = self.get_pixel_color(i,j)
                niveau_gris = self.get_pixel_greyscale(couleur_pyxel)
                self.lst_pixels.append((couleur_pyxel, niveau_gris, (i,j)))
        return self.lst_pixels


if __name__== '__main__':
    image = Img("diamant.png")
    image.open_image("diamant.png")