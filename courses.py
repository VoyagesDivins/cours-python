import random

legumes = ["Artichaut", "Aubergine", "Betterave", "Blette", "Brocoli", "Carotte", "Céleri", "Chou", "Chou de Bruxelles", "Chou-fleur", "Courgette", "Épinard", "Fenouil", "Frisée", "Haricot vert", "Laitue feuille de chêne", "Laitue pommée", "Maïs", "Oignon", "Panais", "Poireau", "Poivron", "Pomme de terre", "Potiron", "Radis", "Scarole", "Tomate"]
fruits = ["Coing", "Cornouiller du Canada", "Cynorrhodon", "Datte", "Épine-vinette", "Feijoa", "Figue", "Figue de barbarie", "Fraise", "Framboise", "Grenade", "Griotte", "Groseille", "Jujube", "Kaki", "Kiwaï", "Kiwi", "Lime", "Mandarine", "Marron", "Melon"]
epices = ["cumin", "curcuma", "curry", "poivre", "gingembre moulu", "paprika", "piment doux", "noix de muscade", "clou de girofle", "safran"]

random.seed()

def acheter(quantite, nourriture):
    mes_achats = []
    for i in range(quantite):
        mes_achats.append(nourriture[random.randint(0, len(nourriture) - 1)])
    return mes_achats

def acheter_epices(quantite):
    return acheter(quantite, epices)

def acheter_legumes(quantite):
    return acheter(quantite, legumes)

def acheter_fruits(quantite):
    return acheter(quantite, fruits)

def acheter_a_manger(qte_legumes, qte_fruits, qte_epices):
    return [*acheter_legumes(qte_legumes), *acheter_fruits(qte_fruits), *acheter_epices(qte_epices)]