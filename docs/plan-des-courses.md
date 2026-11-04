# Plan des courses : ce qu'on a, ce qui manque, une spécificité par course

## Éléments reçus (03/11)
| Univers | Portique | Obstacles | Décor de bord de route |
|---|---|---|---|
| Ville / néon (piste actuelle) | ✔ | ✔ modules fermé / ouvert (barrière, mur, eau ou lave avec pont, cônes, tremplin) | ✔ |
| Neige | ✔ | ✔ (barrière, verglas, bûches, bloc de neige, étang gelé, tremplin, cônes) | ✔ |
| Port | ✘ | ✔ | ✔ |
| Volcan | ✘ | ✔ | ✔ |
| Lune | ✘ | ✔ (`obstacles.jfif` : lune ou générique ?) | ✔ |
| Désert | ✔ | ✘ | ✔ (`obstacles_desert.jfif` : arche, cactus, panneau, rocher, crâne, hutte, flèche) |
Communs : arche de départ et d'arrivée, tapis de boost.

## Ce qui manque
- Portiques du port, du volcan et de la lune (déclinables par recoloration de celui de la neige).
- Désert : vrais obstacles (barrière basse, ornière, tremplin, cônes).
- Un panorama de ciel par univers (en partie par code).
- Les versions « ouvert » des obstacles ne sont pas indispensables : l'obstacle de la bonne voie peut glisser ou disparaître par code (elles rendraient seulement l'ouverture plus visible).

## Une spécificité par course (propositions, toujours au service de la pédagogie)
| Course | Nouvelle commande | Pédagogie |
|---|---|---|
| Port : « Marche des containers » | marche du robot : on maintient ↑ pour avancer à son rythme et on marche sur les bons mots d'un petit texte | relever verbes, adjectifs… dans une phrase |
| Neige : « Verglas » | la voiture glisse, il faut anticiper les virages | nature des mots en rafale, 4 voies |
| Volcan : « Pont de lave » | tremplins et trous de lave, le pont n'apparaît que sur la bonne voie | synonymes et antonymes |
| Lune | gravité faible : sauts longs, on choisit son atterrissage | fonctions (sujet, COD…) |
| Désert | dunes et enchaînement de virages | formation des mots (préfixes, suffixes) |
| Grand Prix final | marche, saut et virages mélangés | niveaux de langue, révisions |
Règle : chaque course a son entraînement seul, où la nouvelle commande est expliquée avant la course.

## Mécanismes à coder
Glissade (verglas), marche contrôlée (dalles-mots), sauts de gravité lunaire, ponts conditionnels, tapis de boost. Déjà là : virages, collines, sauts, enjambement, voie verrouillée, jauge de boost.
