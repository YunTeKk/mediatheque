from media import Media

class Mediatheque:

    def __init__(self):
        self.medias: list[Media] = []

    def ajouter_media(self, media: Media) -> None:
        self.medias.append(media)
        print(f"{media.titre} a bien été ajouté à la médiathèque.")

    def supprimer_media(self, media_id: int) -> bool:
        for media in self.medias:
            if media_id == media.id:
                self.medias.remove(media)
                print(f"{media.titre} a correctement été supprimé.")
                return True
           
        print(f"Aucun média n'existe avec l'id {media_id}")
        return False

    def rechercher(self, titre: str) -> list[Media]:
        titre = titre.lower()
        titre = titre.strip()
        search_results: list[Media] = []

        for media in self.medias:
            if titre in media.titre.lower():
                search_results.append(media)
                print(f"{media.__class__}: {media.titre}")

        if len(search_results) == 0:
            print(f"Aucun média contenant \"{titre}\" n'a été trouvé.")

        return search_results

    def afficher_medias(self) -> None:

        if not self.medias:
            print("La médiathèque est actuellement vide.")
            return

        print(f"=== CONTENU DE LA MEDIATHEQUE ({len(self.medias)} média(s)) ===")
        for media in self.medias:
            print(media)

    def liste_medias(self) -> list[Media]:
        return self.medias