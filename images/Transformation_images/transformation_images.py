from PIL import Image
import matplotlib.pyplot as plt

def carre(img, x0:int,y0:int,c:int, niveaux_de_gris:bool)->int:
    """
        Renvoi le niveau de gris moyen de la zone de c * c pixels partant du point (x0,y0)
        niveaux_de_gris: False si rendu e nnoir&Blanc sinon en niveaux de gris
    """
    niveau = 0
    for y in range(c):
        for x in range(c):
            r,v,b = img.getpixel((x+x0,y+y0)) # r, v et b récupèrent les valeurs des 3 canaux (rouge, vert et bleu)
            g = (r+v+b)//3 # On calcul la moyenne des 3 canaux (arrondi à l'inférieur)
            niveau += g
    g_final = int(niveau / (c * c))
    if not niveaux_de_gris:
        if g_final > 110:
            g_final = 255
        else:
            g_final = 0
    #print(g_final)
    return g_final

def niveaux_gris(img):
    largeur, hauteur = img.size # Récupération des dimensions de l'image
    for y in range(hauteur): # On parcourt toute les lignes de l'image
        for x in range(largeur): # Pour chaque ligne, on parcourt chaque colonne
            r,v,b = img.getpixel((x,y)) # r, v et b récupèrent les valeurs des 3 canaux (rouge, vert et bleu)
            g = (r+v+b)//3 # On calcul la moyenne des 3 canaux (arrondi à l'inférieur)
            img.putpixel((x,y),(g,g,g)) # On impose ce même niveau aux 3 canaux

def pixelise(img_source, c:int, niveaux_de_gris = False):
    """
       Pixelise l'image source en carrés de c*c pixels et renvoie l'image produite
       niveaux_de_gris: False si rendu e nnoir&Blanc sinon en niveaux de gris
    """
    largeur, hauteur = img_source.size # Récupération des dimensions de l'image
    img_new = Image.new(mode="RGB", size=(largeur, hauteur))
    for y in range(0, hauteur, c):
        for x in range(0, largeur, c):
            g = carre(img_source, x, y, c, niveaux_de_gris)
            for y1 in range(c):
                for x1 in range(c):
                    img_new.putpixel((x+x1,y+y1),(g,g,g))
    return img_new

plt. axis('off')
image1 = "bird_source.jpg"
img1 = Image.open(image1)
plt.imshow(img1)
plt.savefig("bird_original_800_200_160.png", dpi=160)

img2 = pixelise(img1, 10, True)
plt.imshow(img2)
plt.savefig("bird_niveaux_gris_160.png", dpi=160)

img3 = pixelise(img1, 10, False)
plt.imshow(img3)
plt.savefig("bird_niveaux_sat_160.png", dpi=160)

plt.show()