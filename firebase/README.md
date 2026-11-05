# Firebase pour Lexicourse (Realtime Database)

Le jeu utilise le projet Firebase **lexica** (celui de tes autres jeux) : même base **Realtime Database**, même schéma que `plume` ou `visualfadette` : un nœud par code à 4 chiffres, avec `v`, `maj`, `donnees`.

## À faire une seule fois dans la console Firebase
1. **Realtime Database > Règles** : recopier le fichier `database.rules.json` (tes règles actuelles + le nœud `jeux/lexicourse`) puis **Publier**. Si tu préfères, ajoute seulement le bloc `lexicourse` dans `jeux`.
2. **Authentication > Méthode de connexion** : vérifier que **Anonyme** (élèves) et **E-mail/Mot de passe** (toi) sont activés. Ton compte `julie.granger.rennes@gmail.com` doit exister en e-mail/mot de passe (tu l'utilises sans doute déjà pour tes autres jeux).
3. **Domaine du jeu : Authentication > Paramètres > Domaines autorisés > Ajouter un domaine** : ajoute le domaine Netlify du jeu (par exemple `ton-site.netlify.app`) et ton éventuel nom de domaine personnalisé, sans `https://`. `localhost` est déjà autorisé. Sans cela, la connexion échoue avec l'erreur `auth/unauthorized-domain` (le jeu affiche « Domaine non autorisé »).
4. La configuration web est dans `firebase.config.json` (déjà remplie avec ton application « lexica »). Ce n'est pas un secret : la sécurité est dans les règles. Tu peux restreindre la clé aux sites autorisés dans Google Cloud > API et services > Identifiants.

## Comment ça marche
- **Élèves** : sur l'écran d'accueil, un code à 4 chiffres (on clique sur les cases) puis « SE CONNECTER ». Nouveau code : l'élève choisit un pseudo (sans nom réel) et sa classe ; code déjà utilisé : le jeu affiche le pseudo trouvé et demande « C'est bien toi ? ». « Jouer en invité » reste possible, sans sauvegarde en ligne. « SE DÉCONNECTER » efface la sauvegarde locale du poste (la progression reste dans le compte), pratique sur les ordinateurs partagés.
- **Données** (`jeux/lexicourse/<code>`) : pseudo, classe, cartes, bonnes réponses et portiques, tutoriel, robot, nombre de courses, 30 dernières courses, réussites et erreurs par question.
- **Toi** : un très petit mortier gris, discret, en bas à gauche de l'écran d'accueil (le badge Netlify est en bas à droite), ouvre l'écran prof. Connexion avec ton e-mail et mot de passe Firebase. En local (`localhost` ou fichier ouvert directement), l'écran prof s'ouvre sans Firebase pour déboguer.
  - **Outils de test** : toutes les cartes, retour au départ, tutoriel / robot, réponses toujours justes, boost infini, course avec n'importe quel pilote, fins de course simulées, tirage, adversaire-carte battu, surprise du robot, statistiques de tirage, restauration de ta sauvegarde. Rien n'est envoyé aux comptes élèves en mode test.
  - **Élèves** : liste par classe (pseudo, code, cartes, % de réussite, courses, dernière activité) et fiche par élève (cartes, 8 dernières courses, questions les plus ratées).
- Limite connue : le code est le seul identifiant (comme tes autres jeux) ; deux élèves qui choisissent le même code partagent le même profil, d'où la question « C'est bien toi ? ».
