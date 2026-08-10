import json
from media import Media
from film import Film
from livre import Livre
from mediatheque import Mediatheque

if __name__ == "__main__":

    mediatheque = Mediatheque()

# Tentative d'ouverture de mediatheque.json ou création d'un nouveau tableau de médias
    try:
        with open("mediatheque.json", "r") as jsonfile:
            data_to_load = json.load(jsonfile)

            for data in data_to_load:
                if data["type"] == "Film":
                    media_to_load = Film(data["titre"], data["annee"], data["realisateur"], data["duree_minutes"])

                elif data["type"] == "Livre":
                    media_to_load = Livre(data["titre"], data["annee"], data["auteur"], data["nb_pages"])
                    
                mediatheque.ajouter_media(media_to_load)

    except (FileNotFoundError, json.JSONDecodeError):
            print("Aucune donnée trouvée. Création d'une nouvelle médiathèque.")
            data_to_load = []

# Début de la boucle du programme
    while True:

        print("")
        print("=== GESTIONNAIRE DE MEDIATHEQUE ===")
        print("1. Afficher tous les médias")
        print("2. Ajouter un livre")
        print("3. Ajouter un film")
        print("4. Rechercher un média")
        print("5. Supprimer un média")
        print("6. Quitter")

        user_choice: str = input("\nChoix : ").strip()
        print("")
        if user_choice.isdigit():
            user_choice = int(user_choice)

        else:
            print("La valeur entrée doit être un entier.")
            continue

        if user_choice > 6:
            print(f"Aucune option n'est associée au choix {user_choice}")

# Choix de l'utilisateur

        elif user_choice == 1:
            mediatheque.afficher_medias()

        elif user_choice == 2:
            print("--- AJOUT D'UN LIVRE ---")
            book_title: str = input("Titre : ")
            book_release_year: int = input("Année : ")
            book_author: str = input("Auteur : ")
            book_nbpages: int = input("Nombre de pages : ")

            user_added_book = Livre(book_title, book_release_year, book_author, book_nbpages)
            mediatheque.ajouter_media(user_added_book)

            print(f"\nLivre ajouté avec succès (ID: {user_added_book.id})")

        elif user_choice == 3:
            print("--- AJOUT D'UN FILM ---")
            movie_title: str = input("Titre : ")
            movie_release_year: int = input("Année : ")
            movie_real: str = input("Réalisateur : ")
            movie_duration: int = input("Durée du film (minutes) : ")

            user_added_movie = Film(movie_title, movie_release_year, movie_real, movie_duration)
            mediatheque.ajouter_media(user_added_movie)

            print(f"\nFilm ajouté avec succès (ID: {user_added_movie.id})")

        elif user_choice == 4:
            mediatheque.rechercher(input("Recherche : "))

        elif user_choice == 5:
            id_to_delete: str = input("ID du média à supprimer : ").strip()
            if id_to_delete.isdigit():
                id_to_delete = int(id_to_delete)
                mediatheque.supprimer_media(id_to_delete)

            else:
                print("La valeur entrée doit être un entier.")
                continue

# Sauvegarde des médias dans mediatheque.json à la fermeture du programme

        elif user_choice == 6:

            data_to_save = [media.to_dict() for media in mediatheque.liste_medias()]

            with open("mediatheque.json", "w", encoding="utf-8") as file:
                json.dump(data_to_save, file, indent=4, ensure_ascii=False)

            print("Fermeture du gestionnaire. A bientôt !\n")
            break

        print("")
        input("Appuyez sur ENTREE pour continuer.")