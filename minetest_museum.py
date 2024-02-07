from module_image import *
from module_KNN import *
from module_reseau import *

class Afficher_image():
    def __init__(self, chemin_fichier):
        self.Mk = MinetestKNN('/home/clementdelage/Bureau/projet_minecraft/donnees_couleurs.csv')
        self.Mc = Reseau()
        self.Mi = Img()

    def draw(self):



if __name__ == '__main__':
    test = Afficher_image()
    
    