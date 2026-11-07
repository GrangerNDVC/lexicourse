# Journal des versions

## v0.18 (duel contre un adversaire)
- **Tutoriel 2 jouable** : course contre l'autre voiture de départ, visible sur la piste, avec une **jauge de course** verticale à droite (Toi / adversaire). **Victoire = arriver devant.** Elle se trompe 4 fois sur 10.
- **Garantie à 100 %** : tant que l'élève ne s'est pas trompé, l'adversaire reste derrière lui. Défaite : revanche plus facile (+5 points d'erreurs, 3 fois au maximum).
- **Première victoire** : une carte **rare** garantie ; victoires suivantes : plus de chances de belle carte ; la surprise du robot se déclenche si le robot n'est pas encore découvert.
- **Niveaux pour les futures courses** : erreurs de l'adversaire selon la rareté de sa carte (40 / 30 / 20 %), **−3 points à chaque victoire** jusqu'à 25 / 15 / 8 % ; chances d'affronter des cartes plus rares qui augmentent avec les victoires (`pickRival`).
- Écran prof : outils « Duel test », « Fin de duel : victoire / défaite » ; la fiche élève affiche les duels gagnés. Détails : `docs/regles-de-jeu.md`.
## v0.17 (comptes par code, Realtime Database)
- **Firebase configuré avec ton projet « lexica »** : le jeu utilise la **Realtime Database** (comme `plume`, `visualfadette`…) et non Firestore. Nouveau nœud `jeux/lexicourse/<code à 4 chiffres>` avec `v`, `maj`, `donnees` ; `firebase/database.rules.json` contient tes règles complètes avec ce nœud ajouté.
- **Connexion par code à 4 chiffres** branchée sur l'écran d'accueil (clic sur les cases, bouton SE CONNECTER / SE DÉCONNECTER) : nouveau code = création du profil (pseudo + classe), code existant = « C'est bien toi ? » puis chargement. Sauvegarde en ligne automatique (après chaque réponse, regroupée toutes les 1,5 s). Invité = local seulement.
- **Écran prof** : liste des élèves lue dans `jeux/lexicourse` (colonne Code ajoutée) ; messages d'erreur de connexion explicites (domaine non autorisé, e-mail/mot de passe, réseau).
- `firebase/README.md` réécrit : règles à publier, comptes à vérifier, **domaine autorisé à ajouter** (Authentication > Paramètres > Domaines autorisés). `firebase/firestore.rules` supprimé.
## v0.16 (écran prof)
- **Écran prof** : un très petit mortier discret en bas à gauche de l'écran d'accueil (loin du badge Netlify en bas à droite) ouvre une connexion **e-mail / mot de passe Firebase**.
- **Outils de test** : toutes les cartes, retour au départ, tutoriel / robot, réponses toujours justes, boost infini, course avec n'importe quel pilote, fins de course simulées (sans-faute, belle, ratée), tirage, adversaire-carte battu, surprise du robot, statistiques de tirage. Mode test : rien n'est envoyé aux comptes élèves ; la déconnexion restaure ta sauvegarde (restauration aussi au lancement suivant si le navigateur a été fermé avant).
- **Suivi des élèves** : liste par classe (pseudo, cartes, % de réussite, courses, dernière activité) et fiche par élève (cartes, 8 dernières courses, questions les plus ratées).
- Le jeu enregistre maintenant pour chaque élève : tutoriel, robot, nombre de courses, 30 dernières courses, réussites et erreurs par question (`firebase/firestore.rules` et `firebase/README.md` mis à jour : **les règles Firestore sont à republier**, avec ton e-mail).
- En local (`localhost`, fichier ouvert directement), l'écran prof s'ouvre sans Firebase.
## v0.15 (trois modèles recolorables)
- Les modèles recolorables sont maintenant **la citadine bleue (Aqua), le scooter (Formica) et la hatchback rétro (Vetus)**.
- **5 variantes de Vetus** (communes, provisoires) : Rufa (rouge, feu), Lutea (jaune, électrique), Prasina (vert, nature), Cana (gris, force), Atra (noir, ténèbre). **36 cartes au total.**

## v0.14 (variantes de couleur)
- **Recoloration branchée** : une entrée de `src/personnages.json` peut être une *variante* d'un modèle (`"variante_de"` + `"teinte"` : Rouge, Bleu, Turquoise, Vert, Jaune, Orange, Violet, Rose, Blanc, Gris, Noir, Menthe ou Lavande). Seuls les pixels de la couleur de base changent ; la carte est recomposée avec le véhicule et le robot recolorés.
- **Aucun poids en plus** : les sprites d'une variante sont recolorés dans le navigateur, à la demande (fonction `tint`), à partir du modèle. Même résultat que `src/tools/recolor.py` (écart de 1 sur 255).
- **10 premières variantes communes (2★), provisoires** : scooter Formica (rouge, type feu) → Caerula (bleu), Viridis (vert), Flava (jaune), Rosea (rose), Alba (blanc), Nigra (noir) ; citadine Aqua (bleue) → Erythros (rouge), Xanthos (jaune), Leukos (blanc), Melas (noir). **31 cartes au total.**
- Le type découle de la couleur (rouge : feu, bleu : eau, vert : nature, jaune : électrique, rose : amour, blanc : glace, noir : ténèbre) : proposition à valider.
- `recolor.py` fonctionne maintenant avec n'importe quelle couleur de base (`base_hue`).
## v0.13 (nouveaux pilotes)
- **10 nouveaux pilotes** : Rhodon, Ferrum, Chloros, Cyanos, Kallista, Vigil, Vetus, Formica, Apis, Fulgur (21 cartes au total). Étoiles, types et particularités **provisoires** (`src/personnages.json`, champ `provisoire`). Fulgur est la première carte **extra-rare** (5★).
- Sources rangées dans `assets/sources/personnages/<dossier>/` : `fiche`, `saut`, `enjambement`, `transformation-dos`, `transformation-3-4`.
- `src/tools/build.py` : champ `ety` (origine du nom) repris dans le jeu ; variable `LEXI_SKIP_MISSING=1` pour tester avec un dépôt allégé (ignore les personnages dont les sources manquent).
- Nettoyage des lignes de sol des sprites d'Apis (transformation) et de Vetus (saut).
## v0.12 (progression des cartes)
- **Départ avec deux cartes seulement** (Pyros, Électron) ; les autres arrivent au fil du jeu. Les anciennes sauvegardes de test sont remises à zéro (cartes et tutoriel) : plus de Colosse ni d'Umbra d'office.
- **Collection** : seulement les cartes possédées, plus d'emplacements « ? », compteur « n cartes », **tri par rareté (étoiles) ou par domaine** (feu, électrique, énergie, eau, force, glace, amour, nature, ténèbre), pages automatiques. La rareté s'affiche dans la vue détaillée.
- **Choix du pilote** : seuls les pilotes possédés sont proposés.
- **Récompenses** : fin du tutoriel 1 = une carte **commune** garantie (une seule fois). Ensuite, après une course réussie (≥ 70 %), une carte est possible ; un beau score, un sans-faute ou un adversaire battu augmentent les chances de **rare** et d'**extra-rare** ; la malchance est compensée au fil des tirages ; carte garantie après 3 courses réussies sans carte. Tous les réglages sont dans le bloc `PR` du code.
- **Raretés** : commune, rare, extra-rare (« épique » compte désormais comme rare).
- **Adversaires-cartes** (prêts pour le chantier B, pas encore jouables) : `pickRival`, `rivalPower`, `winRival`.
- Détails des règles : `docs/progression-cartes.md`.

## v0.11 (origine des noms)
- **« Le savais-tu ? »** : l'explication du nom grec ou latin de chaque pilote s'affiche dans la vue détaillée de la Collection et à l'ouverture d'une nouvelle carte (champ `ety` de `src/personnages.json`).
- Nouvel outil `src/tools/recolor.py` : recoloration par code des pixels rouges d'une base (12 couleurs validées : rouge, bleu, turquoise, vert, jaune, orange, violet, rose, blanc, gris, noir, menthe, lavande). Pas encore branché au build.

## v0.10 (accueil, hub, tutoriel, pause)
- **Pause en course** : bouton ⏸ en haut à gauche (ou Échap) → REPRENDRE ou ACCUEIL (la course en cours est abandonnée, les cartes sont conservées). `H` = accueil depuis la pause.
- **Bouton « ⌂ Accueil »** sur le hub, le tutoriel, le choix du pilote et la collection.
- **Nouveau parcours** : Accueil → **Hub** (Tutoriel · Courses grisées « bientôt » · Collection) → **Tutoriel** (1 · Entraînement seul · 2 · Course contre un adversaire, verrouillée tant que l'entraînement n'est pas terminé, adversaire à venir) → choix du pilote → course → résultats → retour au tutoriel (✔ Terminé).
- **Noms des cartes** (racines grecques et latines) : Pyros, Électron, Colosse, Nox, Dynamis, Candide, Velox, Titan, Philia, Umbra, Aqua ; l'origine du nom s'affiche dans la vue détaillée de la collection (champ `ety`). À reporter dans `src/personnages.json` (voir `noms-cartes.json`).
- La Collection revient à l'écran d'où on l'a ouverte.

## v0.9.1 (correctif)
- **Bug corrigé : écran figé en fin de course** (décor, véhicule et boutons disparaissent, plus aucune commande). Cause : à l'arrivée, la position dépassait la longueur de la piste et le rendu plantait, ce qui arrêtait toute la boucle du jeu. Corrections : position bornée à l'arrivée et au rendu ; la boucle ne s'arrête plus jamais (une erreur est écrite dans la console, le jeu continue).
- **Cartes** : le robot est de nouveau DEVANT et la voiture (3/4 avant) DERRIÈRE (`src/tools/cartes.py`). À prendre en compte en relançant `python src/tools/build.py` avec les images sources.

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
