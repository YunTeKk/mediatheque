from media import Media

class Livre(Media):

    def __init__(self, titre: str, annee: int, auteur: str, nb_pages: int):
        super().__init__(titre, annee)
        self.auteur = auteur
        self.nb_pages = nb_pages

    def to_dict(self):
        livre_dict = super().to_dict()
        livre_dict["auteur"] = self.auteur
        livre_dict["nb_pages"] = self.nb_pages

        return livre_dict

    def __str__(self):
        return f"ID : {self.id}, Livre : {self.titre} de {self.auteur} sorti en {self.annee} ({self.nb_pages} pages)"