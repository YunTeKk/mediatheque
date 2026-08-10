class Media:

    _id_count = 0

    def __init__(self, titre : str, annee: int):
        Media._id_count += 1
        self.id = Media._id_count
        self.titre = titre
        self.annee = annee

    def to_dict(self) -> dict[str,int,int]:
        return {
            "type" : self.__class__.__name__,
            "id" : self.id,
            "titre" : self.titre,
            "annee" : self.annee
            }
    
    def __str__(self):
        return f"ID : {self.id}, {self.__class__.__name__} : {self.titre} sorti en {self.annee}"
