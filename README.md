# triangle_pascal
Programme qui permet de construire le triangle de Pascal à l'aide de python en utilisant le module turtle.
Le module turtle permet de dessiner dans une fenêtre.

## Explication du programme en détail
Il y a deux fonctions : 
- <code>carre(n)</code> prend un paramètre <code>n</code> qui est égal à soit 0 ou 1, ensuite si <code>n</code> = 0 alors il va définir la couleur sur rouge et dessiner un carré et le remplir avec la couleur rouge, sinon si <code>n</code> = 1 alors il va définir la couleur sur bleu et dessiner aussi un carré et le remplir avec la couleur bleue. Pour résumer, si <code>n</code> = 0 alors carré rouge sinon si <code>n</code> = 1 alors carré bleu
- <code>dessine(nombre_ligne)</code> prend un paramètre <code>nombre_ligne</code> qui correspond au nombre de ligne qu'on veut afficher du triangle de Pascal, ensuite on va parcourir le nombre de fois <code>nombre_ligne</code> et pour chaque ligne ajouter 1 à la fin de la prochaine ligne, et après pour construire cette prochaine ligne on va parcourir la longueur de la ligne actuelle - 1, on va pouvoir donc constuire la prochaine ligne avec <code>ligne[x] + ligne[x + 1]</code>. Pour construire graphiquement le triangle de Pascal, il faut remplacer les nombres pairs par 0 et les impairs par 1, on va vérifier le résultat. Pour finir, on va parcourir la ligne actuelle, et la construire gaphiquement.
