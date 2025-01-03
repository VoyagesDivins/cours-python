class Soupe():
    def __init__(self, nom):
        # nom, legumes, mixee, cuite, sel, eau sont des attributs de la classe
        self.nom = nom
        self.legumes = []
        self.mixee = False
        self.cuite = False
        self.sel = False
        self.eau = 0

    # ajout_eau, ajout_sel, ajout_legume, mixer, cuire, est_ce_que_la_soupe_est_prete sont des méthodes de la classe, elles agissent sur les attributs
    def ajout_eau(self, nb_litres):
        print("J'ajoute {} litre{} d'eau à la soupe".format(nb_litres, "s" if nb_litres > 1 else ""))
        self.eau = nb_litres

    def ajout_sel(self):
        print("Un peu de sel...")
        self.sel = True

    def ajout_legume(self, legume):
        print("Miam ! J'ajoute des {} à la soupe.".format(legume))
        self.legumes.append(legume)

    def mixer(self):
        if len(self.legumes) == 0:
            print("Il n'y a pas assez de légume !")
        elif not self.cuite:
            print("Il faut d'abord cuire la soupe !")
        elif self.mixee:
            print("La soupe est déjà mixée !")
        else:
            print("VRZRZRZBZRZRNZNRNZRN")
            self.mixee = True

    def prete_a_cuire(self):
        if self.eau > 0 and self.sel and len(self.legumes) > 0:
            print("C'est cuit !")
            return True
        else:
            return False

    def cuire(self):
        if self.prete_a_cuire():
            self.cuite = True
        else:
            print("Il manque quelque chose à cette soupe")

    def est_ce_que_la_soupe_est_prete(self):
        if self.mixee:
            print("La soupe de {} est prête !".format(self.nom))
        elif self.cuite:
            print("Il ne vous reste plus qu'à mixer la soupe, et elle sera prête")
        elif self.prete_a_cuire():
            print("Il faut encore cuire la soupe et la mixer.")
        else:
            print("Non, au boulot !")