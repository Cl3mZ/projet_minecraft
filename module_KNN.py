import csv

class MinetestKNN:
    """Permet la classification """
    def __init__(self, chemin_fichier):
        self.donnees = []
        with open(chemin_fichier, 'r') as fichier:
            lecteur = csv.reader(fichier, delimiter=';')
            next(lecteur) 
            for ligne in lecteur:
                valeurs_rgb = list(map(int, ligne[1:4]))
                couleur_minetest = int(ligne[4])
                self.donnees.append((valeurs_rgb, couleur_minetest))

    def classifier_couleur(self, couleur_rgb):
        couleur_minetest = None
        distance_minimale = float('inf')
        for point_de_donnees in self.donnees:
            valeurs_rgb, couleur_point = point_de_donnees
            distance = sum((a - b) ** 2 for a, b in zip(couleur_rgb, valeurs_rgb)) ** 0.5
            if distance < distance_minimale:
                distance_minimale = distance
                couleur_minetest = couleur_point
        return couleur_minetest

minetest_knn = MinetestKNN('/home/clementdelage/Bureau/projet_minecraft/donnees_couleurs.csv')
couleur_rgb_a_classifier = [17, 137, 102]
couleur_minetest_resultat = minetest_knn.classifier_couleur(couleur_rgb_a_classifier)
print(f"Couleur Minetest pour RGB {couleur_rgb_a_classifier} : {couleur_minetest_resultat}")