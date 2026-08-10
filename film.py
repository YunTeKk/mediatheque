from media import Media

class Film(Media):

    def __init__(self, titre: str, annee: int, realisateur: str, duree_minutes: int):
        super().__init__(titre, annee)
        self.realisateur = realisateur
        self.duree_minutes = duree_minutes


    def to_dict(self):
        film_dict = super().to_dict()
        film_dict["realisateur"] = self.realisateur
        film_dict["duree_minutes"] = self.duree_minutes

        return film_dict

    def __str__(self):
        return f"ID : {self.id}, Film : {self.titre} de {self.realisateur} sorti en {self.annee} (durée : {self.duree_minutes} minutes)" 

    