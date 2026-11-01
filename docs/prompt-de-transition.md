# Prompt de transition (à coller au début d'une nouvelle conversation)

Joindre : `lexicourse-depot-github.zip` (dépôt complet), le lien du document « Lexicourse — Feuille de route et dossier de prompts », et les nouvelles images.

---

Je suis Julie, professeure de français (4ème) à Rennes. Nous construisons ensemble **Lexicourse**, un jeu de course éducatif en pseudo-3D, en un seul fichier HTML, pour apprendre le vocabulaire des consignes (puis nature des mots, fonctions, synonymes/antonymes, formation des mots, niveaux de langue). Le projet est organisé en chantiers (feuille de route, 16 chantiers). Tu codes, je produis les images (IA) et je décide du design. Je me tutoie avec toi et je préfère des réponses concises, un chantier à la fois, des fichiers téléchargeables, et une validation de ma part avant d'intégrer de nouvelles images.

**Première étape : lis le dépôt joint** (`README.md`, `docs/journal-de-bord.md`, `docs/regles-de-jeu.md`, `docs/feuille-de-route.md`, `src/personnages.json`, `src/tools/build.py`), résume-moi l'état en 10 lignes, puis attends mon feu vert.

## État (version 0.9)
- Moteur pseudo-3D (virages, collines, panorama, décors), 4 voies, voie **verrouillée comme réponse** quelques secondes avant le portique ; le bloc de la bonne voie s'efface seulement si on y est.
- Voiture ⇄ robot (le robot se débloque après 4 portiques ; 55 % de la vitesse ; enjambe), saut, jauge de boost remplie par les bonnes réponses (+25 %, +50 % si bonne forme), sprint final sans question, vitesse de route croissante (tuto).
- **Écran d'accueil** illustré (`assets/sources/interface/accueil.png`) : emplacement du code à 4 chiffres (connexion pas encore branchée) et bouton « Jouer en invité ».
- **Menu** : le pilote se choisit AVANT la course seulement ; cartes regroupées par famille (variantes de couleur) avec pastilles ; pages ; écran **Collection** (cartes avec nom en bas, étoiles en haut à gauche, vue détaillée) ; résultats de course puis tirage de cartes.
- **Cartes** : fond de type (9 types : feu, électrique, énergie, eau, force, glace, amour, nature, ténèbre) + **voiture de 3/4 avant DEVANT et robot de face DERRIÈRE**, extraits de la planche 8 vues et composés automatiquement par `src/tools/cartes.py` ; version « voiture seule » tant que le robot n'est pas découvert (surprise du tutoriel). Une carte faite à la main (`carte.*`) n'est utilisée que si `"carte":"main"` dans `personnages.json`. Le nom (en bas) et les étoiles (en haut à gauche) sont ajoutés par le jeu.
- **Surprise du robot** : écran de découverte avec animation de transformation ; déclenchement provisoire après 4 portiques.
- 11 cartes : rouge (3★, départ), jaune (3★, départ), moto noire (4★), camion bleu (2★), moto verte (2★, sprites de la moto noire en attendant), + citadine blanche, formule 1, monster truck, camping-car, berline noire, citadine bleue simple (étoiles provisoires).
- Profil local par navigateur ; Firebase facultatif (règles dans `firebase/`).
- Outils : `outils/generateur-de-prompts.html` (donne le prompt, l'image à joindre, le nom du fichier), `python src/tools/build.py` (fabrique `index.html`), `python tests/smoke_test.py`.

## Décisions prises
- Étoiles = rareté (1 à 5) ; communes 2–4★ ; **extra-rares (5★) seulement par sans-faute** ; départ : rouge et jaune offertes.
- Cartes gagnées **après** la course (≥ 70 % de bonnes réponses = 1 carte, sans-faute = 2 cartes dont une pouvant être extra-rare, carte garantie après 3 courses sans carte) : règles provisoires.
- La rareté et le type de chaque carte sont décidés par moi dans `src/personnages.json`.
- **Cartes communes** : la citadine bleue simple (`voiture-bleue`, planche, saut, enjambement, transformation de dos) sert de base ; je veux la **recolorer par code** en toutes les couleurs (noir, blanc, gris, pastels…) + une ou deux autres formes (berline, scooter). Test concluant : on ne change que les pixels bleus (teinte, saturation, luminosité). Le type de la carte découle de la couleur.
- L'élève choisira aussi ses adversaires parmi ses cartes (bots) ; places vides = pilotes invités.
- Chaque personnage aura une particularité (propositions dans `personnages.json`, non implémentées) ; pouvoirs selon type ET étoiles, en gardant l'objectif pédagogique.
- Identifiant de connexion : code à 4 chiffres (Firebase), écran d'accueil illustré fourni (`assets/sources/interface/accueil.png`).

## À faire (priorité décroissante)
0. **Tutoriel avec rival** (conditions de victoire proposées dans `docs/regles-de-jeu.md`, à valider) : l'autre voiture de départ comme adversaire ; la victoire déclenche la surprise du robot ; écran de fin de tutoriel, possibilité de le passer ou de le rejouer de plus en plus vite.
1. **Recoloration par code** : entrées « variante » dans `personnages.json` (base, teinte, saturation, luminosité, type), génération des sprites et des cartes ; tirage aléatoire par quotas de rareté ; décider ce qui augmente les chances (série de bonnes réponses, sans-faute, régularité…).
2. **Connexion à 4 chiffres** (Firebase, un document par code ; l'emplacement est déjà sur l'écran d'accueil) puis **hub** : Tutoriel (indiquer quand il est terminé, pouvoir le passer, le reprendre en accélérant), Courses (choix), Collection.
3. **Pouvoirs des cartes** (type × étoiles) + implémentation des particularités.
4. **Adversaires** (bots) choisis dans la collection, classement, podium ; la victoire devient une condition de récompense.
5. Piste 2 canyon (images fournies dans `assets/sources/decors/piste2-desert/`), portiques fermé/ouvert, effets, icônes.
6. Courses thématiques (consignes courtes), puis audio (inventaire dans `docs/audio.md`), Firebase complet, mise en ligne, tablette.

## Règles de travail
- Ne pas utiliser de nouvelles images sans mon accord ; me dire quelles images joindre et comment les nommer.
- Tester dans un navigateur avant de livrer, mettre à jour `CHANGELOG.md`, `docs/journal-de-bord.md`, `docs/regles-de-jeu.md` et la feuille de route.
- Aucune donnée personnelle d'élève (pseudo ou code seulement). Dépôt privé (certains designs ressemblent à des modèles existants).
- Un seul fichier HTML autonome ; interface dessinée dans le canvas ; mêmes fonctions pour clavier, souris et tactile.
