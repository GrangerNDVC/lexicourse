# Journal des versions

## v0.9
- **Écran d'accueil** illustré (voitures rouge et jaune, titre animé) : emplacement du code à 4 chiffres (connexion bientôt disponible) et bouton « Jouer en invité ».
- **Cartes** recomposées : voiture de 3/4 avant DEVANT, robot de face DERRIÈRE. Tant que le robot n'est pas découvert, les cartes et le menu montrent la voiture seule.
- **Surprise du robot** : écran de découverte avec animation de transformation (déclenchement provisoire après 4 portiques ; prévu : en battant l'autre voiture du tutoriel).

## v0.8
- Cartes composées automatiquement (fond du type + voiture et robot de face) ; nom en bas, étoiles en haut à gauche, ajoutés par le jeu.
- Écran Collection avec vue détaillée ; étoiles et types dans `src/personnages.json`.
- 11 personnages : berline noire, citadine bleue simple (base des cartes communes), moto verte (carte).
- Détection des images de planches en 1, 2 ou 3 rangées.

## v0.7
- Le pilote se choisit **avant** la course seulement ; menu avec pages et regroupement des couleurs d'un même modèle.
- Cartes gagnées **après** la course : ≥ 70 % de bonnes réponses = 1 carte, sans-faute = 2 cartes dont une chance d'extra-rare ; carte garantie après 3 courses sans carte (règles provisoires).
- Rareté de chaque carte choisie dans `src/personnages.json` ; sauvegarde par identifiant de carte.
- Générateur de prompts v2 : image à joindre, nom du fichier, cartes de face, variantes de couleur, écrans.

## v0.6
- 8 personnages jouables (citadine blanche, formule 1 cyan, monster truck violet, camping-car rose en plus).
- Collection de cartes : départ avec le rouge et le jaune, une carte tirée au hasard toutes les 5 bonnes réponses.
- Profil du joueur : sauvegarde dans le navigateur, synchronisation Firebase facultative (pseudo + code de classe).

## v0.5
- Réponse verrouillée avant le portique ; le bloc de la bonne voie s'efface seulement si on y est.
- Camion et robot bleu plus imposants ; tailles réglables par personnage.
- Dépôt organisé : questions en JSON, script de fabrication.

## v0.4
- Progression : route lente au début, robot débloqué après 4 portiques.
- Jauge de boost (remplie par les bonnes réponses) et sprint final sans questions.
- Consigne en grand, mots en pastilles ; camion de dos.

## v0.3
- Voies, transformation voiture/robot, saut et enjambement, portiques avec mots, 4 personnages.

## v0.2
- Moteur de piste pseudo-3D (virages, collines, décors, ciel).

## v0.1 (archives/prototype-v0)
- Prototype initial : 4 voies fixes, questions en bandeau.
