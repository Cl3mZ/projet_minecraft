from module_image import *
from module_KNN import *
from module_reseau import *

class Afficher_image():
    def __init__(self):
        self.Mk = MinstestKNN('donnees_couleurs.csv', 5)
        self.Mk.train()
        self.Mc = Reseau()
        self.Mc.connect_to("127.0.0.1", 4711)
        self.Mi = Img("diamant.png")

    def draw3D(self, position_x, position_y, position_z):
        """Dessine l'image donnée dans minetest"""
    # Parcourir tous les pixels de l'image
        for i in range(self.Mi.get_width()):
            for j in range(self.Mi.get_height()):
                # Obtenir la couleur du pixel
                pixel_color = self.Mi.get_pixel_color(i, j)
                # Utiliser le KNN pour trouver la couleur la plus proche dans les données
                closest_color = self.Mk.find_closest_bricks_color(pixel_color[0], pixel_color[1], pixel_color[2])[0]
                # Placer un bloc dans Minetest à la position spécifiée
                # En tenant compte que y est la hauteur et z est la profondeur
                avance = self.Mi.get_pixel_greyscale(pixel_color) // 100
                self.Mc.world_set_block(closest_color, position_x + i, position_y-j , position_z + avance )
        self.Mc.disconnect()

    def draw2D(self, position_x, position_y, position_z):
        """Dessine l'image donnée dans minetest"""
    # Parcourir tous les pixels de l'image
        for i in range(self.Mi.get_width()):
            for j in range(self.Mi.get_height()):
                # Obtenir la couleur du pixel
                pixel_color = self.Mi.get_pixel_color(i, j)
                # Utiliser le KNN pour trouver la couleur la plus proche dans les données
                closest_color = self.Mk.find_closest_bricks_color(pixel_color[0], pixel_color[1], pixel_color[2])[0]
                # Placer un bloc dans Minetest à la position spécifiée
                # En tenant compte que y est la hauteur et z est la profondeur
                self.Mc.world_set_block(closest_color, position_x + i, position_y - j , position_z)
        self.Mc.disconnect()

if __name__ == '__main__':
    test = Afficher_image()
    test.draw3D(0, 20, 0)
    