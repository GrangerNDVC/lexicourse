# Lexicourse

Jeu de course éducatif en pseudo-3D : chaque bonne réponse au vocabulaire des consignes fait avancer. Le joueur choisit sa forme (voiture rapide / robot lent et puissant) et se place sur la voie du bon mot.

## Jouer
Ouvrir `index.html` dans un navigateur (fichier unique, aucune installation).

| Action | Commande |
|---|---|
| Changer de voie | ← → ou clic sur une voie |
| Se transformer (robot débloqué) | Espace ou bouton à l'écran |
| Boost (jauge) | B ou Maj maintenu, ou bouton |
| Changer de personnage (tests) | 1 à 4 |
| Faire avancer la progression (tests) | N |

## Organisation du dépôt
```
index.html            jeu jouable (généré, ne pas modifier à la main)
src/
  template.html       code du jeu (sans images ni questions)
  questions/          banques de questions (une par course) en JSON
  tools/build.py      assemble le jeu → index.html
assets/
  sources/            images brutes générées (personnages, décors, interface)
  prompts/            prompts utilisés pour générer les images
  teaser/             visuels de présentation du jeu
docs/                 feuille de route, règles de jeu, journal de bord, captures
tests/                test rapide du jeu
firebase/             (futur) règles et configuration
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

## Ajouter un personnage
Créer `assets/sources/personnages/<nom>/` avec : `fiche`, `saut`, `enjambement`, `transformation-dos` (fond vert uni #00FF00, une seule vue par image, sans texte), puis ajouter une ligne dans `PERSOS` de `src/tools/build.py`.

## Conventions
- **Versions** : numéro dans `CHANGELOG.md` et étiquette git (`git tag v0.6`), pas de copie du fichier.
- **Commits** : un message court au présent, un chantier à la fois (« Ajoute le sprint final »).
- **Images** : un dossier par personnage ou par piste, noms en minuscules avec tirets.

## Points de vigilance
- **Droits des images** : certains personnages ressemblent à des modèles existants. Garder le dépôt **privé** tant que des versions originales ne sont pas faites.
- **Données d'élèves** : jamais de nom réel ni de donnée personnelle dans le dépôt ; pour Firebase, ne publier ni clés privées ni comptes de service.

## Documentation
Voir `docs/` (feuille de route, règles de jeu, journal de bord).
