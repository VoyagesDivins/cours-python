# Variables

Une variable sert à stocker de la donnée en mémoire.

````
# Je mets la valeur 10 dans la variable x
>>> x = 10
>>> x
10
````

# Types

Les variables ont des types.

````
# La  variable x est de type int (entier)
>>> x = 10
>>> type(x)
<class 'int'>

# La  variable nom est de type string (chaine de caractères)
>>> nom = "Etaine"
>>> type(nom)
<class 'str'>

# La  variable fait_t_il_froid est de type bool (booléen : vrai ou faux)
>>> fait_t_il_froid = True
>>> type(fait_t_il_froid)
<class 'bool'>

````

# Fonctions

Une fonction est une structure qui permet de placer du code que l'on souhaite appeler plusieurs fois.

````
# La fonction addition prend en fonction deux paramètres et renvoie leur somme.
# Le code indenté est le code executé lors de l'appel de la fonction.
>>> def addition(x: int, y: int):
...     return x + y
...
>>> addition(10, 8)
18
````

Python fournit un grand nombre de fonctions prêtes à l'emploi.

````
# Fonction print pour afficher un texte.
>>> print("Bonjour, mille-pattes !")
Bonjour, mille-pattes !

# Fonction input pour récupérer ce que l'utilisateur a tapé au clavier.
>>> saisie = input("Quel est votre âge ?\n")
Quel est votre âge ?
54
>>> saisie
'54'

# Fonction type pour connaître le type d'une variable.
>>> quel_est_mon_type = 56.98
>>> type(quel_est_mon_type)
<class 'float'>
>>> et_le_mien = "Tralalère"
>>> type(et_le_mien)
<class 'str'>
````

# Execution

On peut executer du python de trois manières:

## Shell

Le shell permet d'executer du code directement, ligne par ligne. Pratique pour faire des tests. On le lance dans une invite de commande et on quitte avec la fonction **exit**.
````
(base) PS C:\Users\proym> python
Python 3.11.4 | packaged by Anaconda, Inc. | (main, Jul  5 2023, 13:47:18) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Bonjour le shell")
Bonjour le shell
>>> print("Au revoir le shell")
Au revoir le shell
>>> exit()
````

## Fichiers

Les fichiers permettent d'écrire de long programmes, executable à souhait.

Un fichier python est un fichier texte dont l'extension est *.py.

Dans le fichier mon_premier_programme.py
> print("Hello, World!)
>
> input("Tapez sur une touche pour terminer le programme.)

Ensuite executer avec la commande python

````
(base) PS C:\Users\proym\temp> python .\mon_premier_programme.py
Hello, World!
Tapez sur une touche pour terminer le programme.
(base) PS C:\Users\proym\temp>
````

## Jupyter notebook

Un mélange de texte et de bout de programmes, très adapté pour faire un cours. On ne l'a pas encore vu.

# Idées d'exercices

## Manipulation
### Shell
- Lancer le shell
- Faire une addition de deux variables
- Fermer le shell
### Fichier
- Créer un fichier avec la bonne extension
- Ecrire une ligne de code dans le fichier qui affichera "Mon premier fichier"
- Exécuter le fichier
- Vérifier l'affichage du texte
## Fonction
- Créer un fichier avec la bonne extension
- Ecrire une fonction nommée **fois_dix** qui prend en paramètre un nombre et le renvoie multiplié par 10.
- Ecrire une fonction nommée **carré** qui prend en paramètre un nombre et renvoie son carré.
- Ecrire une fonction nommé **carré_fois_dix** qui prend en paramètre un nombre et le renvoie au carré puis multiplié par 10. La fonction doit faire appel aux deux précédents.
- Ecrire un code qui fait appel à la fonction **carré_fois_dix** et affiche le résultat








