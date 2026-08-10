# 📚 Gestionnaire de Médiathèque en Python

Un projet d'application console en Python orientée objet permettant de gérer une médiathèque interactive (livres, films), d'effectuer des recherches, de supprimer des éléments et de persister les données au format JSON.

---

## 🚀 Fonctionnalités

- **Affichage des médias** : Liste l'ensemble des livres et films enregistrés.
- **Ajout de médias** :
  - **Livre** (titre, année, auteur, nombre de pages)
  - **Film** (titre, année, réalisateur, durée en minutes)
- **Recherche** : Recherche par mots-clés parmi les médias enregistrés.
- **Suppression** : Suppression d'un média à partir de son identifiant unique.
- **Persistance des données** : Sauvegarde et chargement automatique des médias depuis un fichier `mediatheque.json`.

---

## 📂 Structure du Projet

```text
.
├── main.py            # Point d'entrée principal et menu interactif
├── mediatheque.py     # Classe Mediatheque (gestion de la collection)
├── media.py           # Classe parent / de base Media
├── livre.py           # Classe Livre (hérite de Media)
├── film.py            # Classe Film (hérite de Media)
├── mediatheque.json   # Fichier de persistance des données (généré automatiquement)
└── README.md          # Documentation du projet
