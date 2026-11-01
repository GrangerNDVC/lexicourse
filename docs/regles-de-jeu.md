# Règles de jeu (version 0.9)

- **Menu** : le joueur choisit son pilote parmi ses cartes **avant** la course ; impossible de changer en cours de course. Les cartes d'un même modèle (couleurs différentes) sont regroupées ; une pastille de couleur par variante.
- **Voies** : 4 voies. ← → ou clic sur une voie. La voie est **verrouillée comme réponse** quelques secondes avant le portique.
- **Portiques** : une consigne, 4 mots sur 4 panneaux, 4 voies bloquées. Bonne réponse = le bloc de ta voie s'efface ; mauvaise = collision, perte de vitesse, explication.
- **Formes** : voiture (rapide ; saute les obstacles bas et les rampes) / robot (55 % de la vitesse, enjambe les gros obstacles). Transformation 0,6 s + 3 s de recharge. Le robot se débloque après 4 portiques.
- **Progression** : la vitesse de la route augmente à chaque portique réussi.
- **Jauge de boost** : bonne réponse +25 %, +50 % si la forme était la bonne. Boost à la demande (≈ 3,5 s pour une jauge pleine).
- **Sprint final** : les 20 % de fin de tour sans question ; voie libre, ou boost + bonne forme pour franchir.
- **Fin de course** : écran de résultats puis cartes (règles provisoires) :
  - 70 % de bonnes réponses ou plus : 1 carte (communes, rares, épiques ; les communes sortent le plus souvent) ;
  - **sans-faute** : 2 cartes, la seconde pouvant être **extra-rare** (seul moyen d'en obtenir) ;
  - carte garantie après 3 courses sans carte.
- **Cartes** : étoiles (2 à 5) et type (feu, électrique, énergie, eau, force, glace, amour, nature, ténèbre) choisis dans `src/personnages.json`. Départ : rouge et jaune (3★). Les 5★ ne s'obtiennent que par un sans-faute. Écran Collection pour voir toutes ses cartes.
- **Profil** : pseudo (sans nom réel) et code de classe ; collection sauvegardée dans le navigateur, et sur Firebase si configuré.
- **Accueil** : écran illustré ; code à 4 chiffres (bientôt) ou « Jouer en invité ».
- **Surprise du robot** : tant qu'il n'est pas découvert, les robots n'apparaissent ni sur les cartes ni dans le menu ; la découverte se fait dans le tutoriel (provisoire : après 4 portiques).
- **Tutoriel (à implémenter, proposition)** : 6 portiques, route plafonnée à 50 % de la vitesse maximale ; rival = l'autre voiture de départ (90 % de l'allure idéale, 6 bonnes réponses sur 10) ; victoire = être devant à l'arrivée ET au moins 4 bonnes réponses sur 6 ; la victoire (ou le dépassement) déclenche la surprise du robot ; en cas de défaite : « Revanche » avec un rival plus faible à chaque essai ; fin du tuto = écran de bilan, courses débloquées, tutoriel rejouable (niveaux de plus en plus rapides).
- **À venir** : adversaires (choisis parmi ses cartes), particularités des personnages, écran d'accueil illustré, courses thématiques.
