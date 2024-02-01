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

x_3d = x_2d
y_3d = y_2d
z_3d = convert_to_grayscale(x_2d, y_2d)
grayscale = (reg x 0.3) + (green x 0.59) + (blue x 0.11)


class MinetestImage(self):
    def __init__(self):
        
    def open_image(self, nom_image):

        une_image = Image.open(nom_image)
        une_image.load()
        une_image = une_image.convert("RGB")

    def get_width():

    def get_height():

    def get_pixel_color():
        pixel_couleur = self.image.getpixel((i, j))
        return pixel_couleur
    def get_pixel_greyscale()