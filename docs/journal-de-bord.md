# Journal de bord

## Décisions
- 29/10 — Piste en données (liste de segments) ; boucle à pas fixe 60 Hz ; interface dessinée dans le canvas.
- 29/10 — Commandes : flèches + clic sur une voie + bouton de transformation ; tactile prévu (chantier 16).
- 29/10 — Obstacles uniquement dans des portiques de question ; réponse verrouillée avant le portique.
- 29/10 — Jauge de boost plutôt qu'accélération automatique ; sprint final sans question.
- 29/10 — Robot verrouillé au début, débloqué quand la route accélère ; courses thématiques ensuite.
- 29/10 — Tuto : tous les personnages testables ; en course, un choisi, les autres sont des bots ; nouveaux personnages débloqués au fil des réussites.
- 29/10 — Audio : SFX embarqués dans le jeu, musique chargée depuis `assets/sources/audio/musique` ; musique en 3 couches selon la vitesse ; manifest événement → fichier ; moteur audio au chantier 6b.
- 29/10 — Collection : départ rouge + jaune, 6 autres personnages gagnés au hasard (une carte toutes les 5 bonnes réponses) ; Firebase facultatif avec connexion anonyme.
- 29/10 — Raretés proposées (à valider) : communes = citadine, camping-car ; rares = camion, moto ; épiques = formule 1, monster truck.
- 29/10 — Le pilote se choisit avant la course seulement (sinon les courses contre adversaires perdent leur intérêt).
- 29/10 — Cartes gagnées après une course, pas pendant ; la rareté de chaque carte est décidée par Julie ; extra-rares uniquement par sans-faute ; plusieurs cartes communes seront des variantes de couleur d'un même modèle (famille) ; l'élève choisira aussi ses adversaires parmi ses cartes.
- 29/10 — Cartes illustrées de face ; cadre et texte ajoutés par le jeu.
- 29/10 — Chaque personnage doit avoir une particularité (proposition dans `src/personnages.json`, pas encore implémentée).
- 30/10 — Cartes : les générateurs d'images ne tiennent pas un gabarit commun ; le jeu compose donc les cartes lui-même à partir de fonds de types (feu, électrique, énergie, eau, force, glace, amour, nature, ténèbre) et des vues de face de la planche 8 vues.
- 30/10 — Étoiles = rareté (2 à 4 pour les communes ; 5 = extra-rare, sans-faute seulement ; départ = rouge et jaune, 3★).
- 30/10 — Cartes communes : recoloration par code de la citadine bleue simple (test concluant sur 10 couleurs) ; type de carte déduit de la couleur.
- 30/10 — Robot bleu simple : l'image de dos utilisée est la dernière image de la transformation ; l'enjambement a été refait pour rester cohérent.
- 30/10 — Cartes dans le jeu : voiture de 3/4 avant devant, robot de face derrière ; version « voiture seule » tant que le robot n'est pas découvert (la surprise du tutoriel). Les cartes faites à la main restent possibles avec "carte":"main".
- 30/10 — Écran d'accueil installé ; connexion par code à 4 chiffres reportée (invité seulement pour l'instant).
- 30/10 — Découverte du robot : provisoire après 4 portiques ; cible = battre l'autre voiture du tutoriel (conditions proposées dans `regles-de-jeu.md`).
- 30/10 — Tirage : propositions à valider — 2★ 60 %, 3★ 30 %, 4★ 10 % ; 5★ par sans-faute seulement ; chances en hausse avec les séries de bonnes réponses et la régularité.

## Bugs et limites connus
- Transformations rouge et jaune : l'angle de caméra change en cours de séquence (retouches 1 à 3 de la feuille de route).
- Obstacles des portiques provisoires (modules fermé/ouvert à générer).
- Ciel : panneau répété en miroir (vrai panorama à générer, optionnel).
- Banque de questions : 9 questions sur 12 ajoutées par l'assistant, à relire.
- Connexion anonyme liée au navigateur : changement d'appareil = collection vide (code de récupération à prévoir).
- Collection complète : plus de récompense (à prévoir : monnaie, couleurs, doublons).
- Moto verte : carte seule, utilise les sprites de la moto noire en attendant ses propres images.
- Étoiles et types des nouveaux personnages : provisoires.
- Tactile non testé ; pas de son ; pas d'adversaires.

## Idées reportées
- Plus-value du robot : batterie (recharge la jauge), analyse de la consigne (mot-clé surligné), passage de force, raccourcis.
- Rampes qui s'ouvrent seulement en boost, tapis de boost, classement du sprint.
- Noms de pilotes tirés des verbes de consigne (Relever, Citer, Justifier, Résumer).
- Championnat, saisons, mode révision (questions ratées), fantômes entre élèves.
