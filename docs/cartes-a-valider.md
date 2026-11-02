# Cartes à valider — sprites 12 à 27 (état au 01/11)

Rien n'est intégré tant que cette table n'est pas validée. Colonnes à remplir : **Étoiles** (rareté) et, si tu veux, corriger nom / type.
Types possibles : feu, électrique, énergie, eau, force, glace, amour, nature, ténèbre.

| Sprite | Véhicule | Nom proposé | Origine | Type proposé | Étoiles (à remplir) | À régler avant intégration |
|---|---|---|---|---|---|---|
| 12 | berline vert menthe | Viridis | latin *viridis*, vert | nature | | transformations dans un style différent de la planche, du saut et de l'enjambement |
| 13 | citadine rose | Rhodon | grec *rhodon*, rose | amour | | planche « kawaii » (sourire, roues dorées) ≠ autres images |
| 14 | SUV gris foncé | Ferrum | latin *ferrum*, fer | force | | enjambement manquant ; saut très petit (119 px, flou) |
| 15 | citadine verte à bande blanche | Chloros | grec *chlôros*, vert | nature | | rien de bloquant |
| 16 | coccinelle turquoise | Cyanos | grec *kyanos*, bleu sombre | glace | | rien de bloquant |
| 17 | cabriolet blanc, robot féminin | Kallista | grec *kallista*, la plus belle | amour | | pare-brise transparent (le fond se verra à travers) |
| 18 | camion de pompiers rouge | Vigil | latin *vigil*, éveillé (les *vigiles* de Rome) | eau | | **saut manquant** (`saut_sprite_18`) |
| 19 | citadine rouge | Rubra | latin *rubra*, rouge | feu | | planche seule ; c'est le sprite 20 recoloré : carte à part ou recoloration par code ? |
| 21 | scooter rouge, robot à antennes | Formica | latin *formica*, la fourmi (formique) | nature | | **base recolorable** (comme le 20) : démo faite, voir `demo_recoloration.png` ; le nom Formica serait pour la version rouge |
| 22 | hatchback bleue rétro | Vetus | latin *vetus*, vieux (vétéran) | force | | saut très petit (114 px, flou) ; liseré noir sur les bords de l'enjambement (je recadre) |
| 26 | moto jaune, robot à échappements | Apis | latin *apis*, l'abeille | énergie | | voir ci-dessous (fichiers à clarifier) |
| 27 | supercar bleu néon | Fulgur | latin *fulgur*, l'éclair (fulgurant) | électrique | | rien de bloquant |

Sprite 20 (citadine bleue, **Aqua**) : déjà dans le jeu, je ne le réintègre pas sauf nouvelles images.
Numéros non reçus : 23, 24, 25 (en cours de retouche chez toi).

## Sprite 26 : points à clarifier
- `sprite_26.png` montre le robot jaune de dos en 3 poses (marche) : est-ce l'**enjambement** ? Il n'y a pas de fichier `enjambement_sprite_26`.
- `transformation1_sprite_26` contient **10 vignettes** (moto, moto avec ailes, robot de dos, robot de face…) sur 2 lignes, avec des lignes de sol noires. Je ne peux pas deviner l'ordre : indique les 6 vignettes à garder dans l'ordre, ou régénère une seule ligne de 6 images de dos sans ligne de sol.
- `transformation2_sprite_26` (3/4) reçue : propre, 6 images en ligne. Elle ne sert pas pour l'instant.
- Si tu régénères la transformation de dos, je peux la remplacer par cette ligne de 6 images de 3/4 si tu préfères l'angle.

## Remarque
Plusieurs véhicules sont bleus (Aqua, Vetus, Fulgur, Colosse) : à distinguer par le type et les étoiles.
