# Progression des cartes (v0.12)

## Raretés
Commune (2★), Rare (3–4★, « épique » compris), Extra-rare (5★). Cartes de départ : Pyros et Électron (3★). Aucune carte extra-rare n'existe encore dans `personnages.json`.

## Quand gagne-t-on une carte ?
| Moment | Carte |
|---|---|
| Fin du tutoriel 1 (entraînement seul), la première fois | une carte **commune** garantie |
| Fin du tutoriel 2 (course contre un adversaire) | une carte **rare** garantie — *prévu, le tutoriel 2 n'est pas encore jouable* |
| Autre course terminée avec ≥ 70 % de bonnes réponses | 50 % de chance d'une carte, +15 % par point de chance ; garantie après 3 courses réussies sans carte |
| Adversaire-carte battu en course | on obtient **cette** carte — *chantier B* |

Une carte tirée est toujours une carte que l'élève ne possède pas.

## Points de chance (« beaux exploits »)
Course à ≥ 85 % : +1 · sans-faute : +2 · adversaire battu : +2. À brancher plus tard : score boosté (jauge de boost).

## Qualité de la carte tirée
Base : 70 % commune, 27 % rare, 3 % extra-rare. Chaque point de chance : +10 points de rare, +6 points d'extra-rare. Chaque tirage sans rare : +6 points de rare ; sans extra-rare : +1,5 point (la malchance est compensée). Plafonds : rare 60 %, extra-rare 35 %.
Simulation (cartes actuelles, sans extra-rare) : chance 0 → 71 % commune / 29 % rare ; chance 2 → 44 % / 56 % ; chance 3 → 27 % / 73 %.

## Rythme (simulation avec les 11 cartes actuelles, 9 à gagner)
Course à 75 % : environ 15 courses pour tout obtenir ; à 90 % : environ 11 ; sans-faute : environ 11. Avec une collection plus grande, le rythme ralentit de lui-même. Leviers pour ralentir : `chance` (50 %), `PITY` (3), `base`.

## Adversaires-cartes (chantier B)
À chaque course, une carte non possédée peut s'inviter (jamais la même deux courses de suite : `prof.lastRival`). Niveau de l'adversaire : commune 0,45 · rare 0,70 · extra-rare 0,95 (`rivalPower`). Battue, elle est obtenue.

## Questions ouvertes
- Rejouer l'entraînement donne-t-il encore des cartes (aujourd'hui oui, avec la chance) ?
- Faut-il ralentir le rythme quand la collection grandit ?
- Quelles cartes seront extra-rares (aucune pour l'instant) ?
- Définition du « score boosté » pour les points de chance.
