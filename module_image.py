# Librairie
from PIL import Image


class Img():
    def __init__(self, nom_image ):
        self.une_image = None
        self.nom_image = nom_image
        self.lst_pixels = []
        self.une_image = Image.open(f"{nom_image}")
    
    def get_width(self):
        """Obtient la largeur d'une image"""
        return self.une_image.width

    def get_height(self):
        """Obtient la hauteur d'une image"""
        return self.une_image.height

    def get_pixel_color(self, i, j):
        """Obtient la couleur du pixel choisi"""
        pixel_couleur = self.une_image.getpixel((i, j))
        print(pixel_couleur)
        return pixel_couleur

    def get_pixel_greyscale(self, pixel_couleur):
        """Calcul le niveau de gris d'un pixel"""
        return (pixel_couleur[0] * 0.3) + (pixel_couleur[1] * 0.59) + (pixel_couleur[2] * 0.11)

    def get_all(self):
        """Obtenir la liste de tout les pixels de l'image avec leurs coordonnées"""
        for i in range(self.get_width()):
            for j in range(self.get_height()):
                couleur_pyxel = self.get_pixel_color(i,j)
                niveau_gris = self.get_pixel_greyscale(couleur_pyxel)
                self.lst_pixels.append(((couleur_pyxel), niveau_gris, (i,j)))
        return self.lst_pixels


if __name__== '__main__':
    image = Img("pessi.jpg")
    image.get_all()