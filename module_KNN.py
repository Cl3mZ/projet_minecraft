import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
class MinstestKNN():
    """Classe contenant un algorithme KNN convertissant un tuple RGB en couleur minetest"""
    def __init__(self, nom_fichier, k):
        self.k = k
        fichier = pd.read_csv(nom_fichier, delimiter=';').dropna()
        self.red = fichier.loc[:,"red"]
        self.green = fichier.loc[:,"green"]
        self.blue = fichier.loc[:,"blue"]
        self.choix = fichier.loc[:,"choice"]

    def train(self):
        """Entraine l'algorithme KNN permettant d'économiser un grand nombre de cycles"""
        d = list(zip(self.red, self.green, self.blue))
        self.model = KNeighborsClassifier(n_neighbors=self.k)
        self.model.fit(d, self.choix)
    
    def find_closest_bricks_color(self, r,g,b):
        """Permet de trouver la couleur la plus proche dans minetest"""
        return self.model.predict([[r,g,b]])

if __name__ == '__main__':
    x = MinstestKNN("donnees_couleurs.csv", 5)
    x.train()
    print(x.find_closest_bricks_color(255, 255, 255))
    print(x.find_closest_bricks_color(0, 0, 255))

    