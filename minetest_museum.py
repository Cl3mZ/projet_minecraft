from module_image import *
from module_KNN import *
from module_reseau import *

class Afficher_image():
    def __init__(self):
        self.Mk = MinstestKNN('donnees_couleurs.csv', 5)
        self.Mk.train()
        self.Mc = Reseau()
        self.Mc.connect_to("127.0.0.1", 4711)
        self.Mi = Img("0d")

    def draw(self, position_x, position_y, position_z):
        """Dessine l'image donnée dans minetest"""
    # Parcourir tous les pixels de l'image
        for i in range(self.Mi.get_width()):
            for j in range(self.Mi.get_height()):
                # Obtenir la couleur du pixel
                couleur_pixel = self.Mi.get_pixel_color(i, j)
                # Utiliser le KNN pour trouver la couleur la plus proche dans les données
                couleur_plus_proche = self.Mk.find_closest_bricks_color(couleur_pixel[0], couleur_pixel[1], couleur_pixel[2])[0]
                # Placer un bloc dans Minetest à la position spécifiée
                # En tenant compte que y est la hauteur et z est la profondeur
                avance = self.Mi.get_pixel_greyscale(couleur_pixel) // 10
                self.Mc.world_set_block(couleur_plus_proche, position_x + i, position_y-j , position_z + avance )
        self.Mc.disconnect()


if __name__ == '__main__':
    test = Afficher_image()
    test.draw(100, 30, 50)
    