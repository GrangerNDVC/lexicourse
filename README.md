# Lexicourse

Jeu de course éducatif en pseudo-3D : chaque bonne réponse au vocabulaire des consignes fait avancer. Le joueur choisit sa forme (voiture rapide / robot lent et puissant) et se place sur la voie du bon mot.

## Jouer
Ouvrir `index.html` dans un navigateur (fichier unique, aucune installation).

| Action | Commande |
|---|---|
| Changer de voie | ← → ou clic sur une voie |
| Se transformer (robot débloqué) | Espace ou bouton à l'écran |
| Boost (jauge) | B ou Maj maintenu, ou bouton |
| Choisir un personnage possédé | 1 à 8 |
| Tests : tirer une carte / avancer la progression | K / N |

## Organisation du dépôt
```
index.html            jeu jouable (généré, ne pas modifier à la main)
src/
  template.html       code du jeu (sans images ni questions)
  questions/          banques de questions (une par course) en JSON
  audio/manifest.json événements du jeu → fichiers audio
  tools/build.py      assemble le jeu → index.html
assets/
  sources/            images brutes (personnages, décors, interface) et audio (musique, bruitages)
  prompts/            prompts utilisés (images, audio)
  teaser/             visuels de présentation du jeu
docs/                 feuille de route, règles de jeu, journal de bord, inventaire audio, captures
tests/                test rapide du jeu
firebase/             règles Firestore et configuration (voir firebase/README.md)
archives/             prototype initial
```

## Fabriquer index.html
```
pip install -r src/tools/requirements.txt
python src/tools/build.py
```
Relancer cette commande après toute modification de `src/` ou de `assets/sources/`.

## Test rapide (optionnel)
```
pip install playwright && playwright install chromium
python tests/smoke_test.py
```

## Ajouter des questions
Éditer `src/questions/consignes.json` : consigne, 4 mots, `bonne_reponse` (numéro du bon mot en commençant à 0) et explication. Garder des mots courts (ils s'affichent sur le portique).

## Ajouter un personnage ou une carte
1. Ouvrir `outils/generateur-de-prompts.html` : il donne, étape par étape, le prompt, **l'image à joindre** et **le nom du fichier** à créer (planche 8 vues, transformation de dos, saut, enjambement, carte de face).
2. Ranger les images dans `assets/sources/personnages/<nom>/` (`fiche`, `transformation-dos`, `saut`, `enjambement`, `carte`).
3. Ajouter une entrée dans `src/personnages.json` (le générateur la fabrique) : nom, famille, couleur, **étoiles** (2 à 5, choisies par toi), **type** de carte, hauteur à l'écran, particularité. **Ajouter à la fin de la liste.** La carte est composée automatiquement (fond du type + vues de face de la planche) ; mets un `carte.png` dans le dossier pour la remplacer par une carte faite à la main.
4. Lancer `python src/tools/build.py`.

Les personnages d'une même **famille** (même modèle, couleurs différentes) sont regroupés dans le menu avec des pastilles de couleur. Les cartes 5★ ne se gagnent qu'avec un **sans-faute**.

## Conventions
- **Versions** : numéro dans `CHANGELOG.md` et étiquette git (`git tag v0.6`), pas de copie du fichier.
- **Commits** : un message court au présent, un chantier à la fois (« Ajoute le sprint final »).
- **Images** : un dossier par personnage ou par piste, noms en minuscules avec tirets.

## Points de vigilance
- **Droits des images** : certains personnages ressemblent à des modèles existants. Garder le dépôt **privé** tant que des versions originales ne sont pas faites.
- **Données d'élèves** : jamais de nom réel ni de donnée personnelle dans le dépôt ; pour Firebase, ne publier ni clés privées ni comptes de service.

## Documentation
Voir `docs/` (feuille de route, règles de jeu, journal de bord).
