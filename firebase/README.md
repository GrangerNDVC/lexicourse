# Firebase : profil et collection de cartes

Le jeu fonctionne **sans** Firebase (sauvegarde dans le navigateur). Avec Firebase, la collection est sauvegardée en ligne et le professeur pourra la consulter.

## Mise en place (à faire une fois, dans la console Firebase de ton projet existant)
1. **Authentication** : activer le fournisseur *Anonyme*. Dans *Paramètres > Domaines autorisés*, ajouter le domaine où le jeu sera publié (GitHub Pages, Netlify…).
2. **Firestore** : ajouter le bloc de `firestore.rules` à tes règles existantes (**ne remplace pas** celles de tes autres jeux), puis publier.
3. **Configuration web** : copier `firebase.config.example.json` en `firebase.config.json` et y coller la configuration web de ton projet (Paramètres du projet > Tes applications > Configuration). Ce n'est pas un secret : la sécurité vient des règles.
4. Relancer `python src/tools/build.py` : le jeu demande alors un pseudo et un code de classe au premier lancement.

## Écran prof (connexion e-mail / mot de passe)
Un très petit mortier gris, discret, en bas à gauche de l'écran d'accueil, ouvre l'écran prof. À faire une fois :
1. **Authentication > Méthode de connexion** : activer *E-mail/Mot de passe* (en plus d'*Anonyme*).
2. **Authentication > Utilisateurs > Ajouter un utilisateur** : ton e-mail et ton mot de passe.
3. **Authentication > Paramètres > Actions de l'utilisateur** : **décocher « Activer la création (inscription) »**, pour que personne d'autre ne puisse créer de compte.
4. **Firestore** : remplacer le bloc `lexicourse_joueurs` par celui de `firestore.rules` (mis à jour) et **remplacer `TON_EMAIL_PROF@exemple.fr` par ton adresse**, puis publier.
5. Ajouter le domaine du jeu dans *Authentication > Paramètres > Domaines autorisés* (déjà fait si l'étape 1 de la mise en place l'est).

Dans l'écran prof :
- **Outils de test** : débloquer toutes les cartes, revenir au départ, tutoriel terminé / robot découvert, réponses toujours justes, boost infini, course test avec n'importe quel pilote, fins de course simulées (sans-faute, belle, ratée) pour vérifier les récompenses, tirage de carte, adversaire-carte battu, surprise du robot, statistiques de tirage, restauration de ta sauvegarde. Rien n'est envoyé aux comptes élèves en mode test ; « Se déconnecter » restaure ta sauvegarde (et si le navigateur est fermé avant, elle est restaurée au lancement suivant).
- **Élèves** : liste par classe (pseudo, cartes, % de réussite, courses, dernière activité) puis fiche de chaque élève : cartes, dernières courses, questions les plus ratées.
- En local (`localhost` ou fichier ouvert directement), l'écran prof s'ouvre **sans** Firebase pour déboguer ; en ligne, il exige la connexion.

## Données enregistrées (collection `lexicourse_joueurs`, un document par joueur)
`pseudo`, `classe`, `cartes` (identifiants des personnages obtenus), `ok` (bonnes réponses), `tot` (portiques passés), `tuto`, `robot`, `races` (nombre de courses), `hist` (30 dernières courses : date, %, cartes), `q` (réussites et erreurs par question), `maj` (date).
**Aucun nom réel, aucune adresse, aucune photo.**

## Limite connue
La connexion anonyme est liée au navigateur : si l'élève change d'appareil ou vide son navigateur, il retrouve une collection vide. Solution prévue : code de récupération (chantier 7).

## Ne jamais déposer ici
Clés privées, fichiers de compte de service (`serviceAccount*.json`) : ils sont dans `.gitignore`.
