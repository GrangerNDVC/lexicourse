# Firebase : profil et collection de cartes

Le jeu fonctionne **sans** Firebase (sauvegarde dans le navigateur). Avec Firebase, la collection est sauvegardée en ligne et le professeur pourra la consulter.

## Mise en place (à faire une fois, dans la console Firebase de ton projet existant)
1. **Authentication** : activer le fournisseur *Anonyme*. Dans *Paramètres > Domaines autorisés*, ajouter le domaine où le jeu sera publié (GitHub Pages, Netlify…).
2. **Firestore** : ajouter le bloc de `firestore.rules` à tes règles existantes (**ne remplace pas** celles de tes autres jeux), puis publier.
3. **Configuration web** : copier `firebase.config.example.json` en `firebase.config.json` et y coller la configuration web de ton projet (Paramètres du projet > Tes applications > Configuration). Ce n'est pas un secret : la sécurité vient des règles.
4. Relancer `python src/tools/build.py` : le jeu demande alors un pseudo et un code de classe au premier lancement.

## Données enregistrées (collection `lexicourse_joueurs`, un document par joueur)
`pseudo`, `classe`, `cartes` (numéros des personnages obtenus), `ok` (bonnes réponses), `tot` (portiques passés), `maj` (date).
**Aucun nom réel, aucune adresse, aucune photo.**

## Limite connue
La connexion anonyme est liée au navigateur : si l'élève change d'appareil ou vide son navigateur, il retrouve une collection vide. Solution prévue : code de récupération (chantier 7).

## Ne jamais déposer ici
Clés privées, fichiers de compte de service (`serviceAccount*.json`) : ils sont dans `.gitignore`.
