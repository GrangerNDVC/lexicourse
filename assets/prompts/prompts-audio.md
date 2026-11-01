# Prompts audio (copier-coller tels quels)

Outils possibles : génération de musique (Suno, Udio…), génération de bruitages (ElevenLabs Sound Effects…), ou banques libres (voir `assets/sources/audio/README.md`). Chaque prompt est complet. Nom du fichier à donner : indiqué au-dessus du prompt.

## Musique

Conseil : pour les 3 couches de la piste 1, génère d'abord la version **intense** avec export des pistes séparées (stems), puis fabrique les versions moyenne et calme en coupant des pistes (batterie, lead). Trois générations séparées ne seront presque jamais synchronisées.

### musique_menu.mp3 — écran titre et choix du personnage

```
Instrumental synthwave, cyberpunk night city, 100 BPM, warm analog synths, soft arpeggios, light drums, mysterious but friendly, seamlessly loopable, no vocals, 90 seconds.
```

### musique_tutoriel.mp3 — tutoriel (route lente)

```
Instrumental chillwave, relaxed 90 BPM, soft pads, gentle plucked synth melody, light beat, calm and curious mood for learning, seamlessly loopable, no vocals, 90 seconds.
```

### musique_piste1_calme.mp3 — course piste 1, couche calme (route lente)

```
Instrumental synthwave racing music, 120 BPM, key of A minor, only soft pads, a warm bass and a light arpeggio, no drums, calm night driving feeling, seamlessly loopable, no vocals, 64 bars.
```

### musique_piste1_moyen.mp3 — course piste 1, couche moyenne

```
Instrumental synthwave racing music, 120 BPM, key of A minor, steady four on the floor drums, a driving bassline, pads and a light arpeggio, confident energy, seamlessly loopable, no vocals, 64 bars.
```

### musique_piste1_intense.mp3 — course piste 1, couche intense (route rapide)

```
Instrumental synthwave racing music, 120 BPM, key of A minor, full energy, fast arpeggios, a bright lead synth, heavy drums and driving bass, exciting and fast, seamlessly loopable, no vocals, 64 bars.
```

### musique_sprint.mp3 — sprint final

```
Instrumental high energy synthwave drum and bass, 140 BPM, urgent final lap, pulsing bass, rising synth stabs, intense but not scary, seamlessly loopable, no vocals, 60 seconds.
```

### musique_podium.mp3 — podium (jingle)

```
Short triumphant victory fanfare, synthwave brass and bright synths, ending on a clear final chord, no vocals, 8 seconds.
```

### musique_fin.mp3 — fin de partie sans podium (jingle)

```
Short gentle encouraging jingle, positive try again feeling, soft synths, ending on a clear final note, no vocals, 5 seconds.
```

## Bruitages

### sfx_ui_clic.mp3 (dossier sfx/ui/) — clic sur un bouton

```
Soft futuristic UI button click, short and crisp, 0.2 seconds.
```

### sfx_ui_personnage.mp3 (dossier sfx/ui/) — choix d'un personnage

```
Quick electronic swoosh with a small confirm blip, character selection in a racing game, 0.4 seconds.
```

### sfx_ui_verrouille.mp3 (dossier sfx/ui/) — bouton verrouillé (robot pas encore débloqué)

```
Low dull denied buzz, option locked, short and not harsh, 0.4 seconds.
```

### sfx_course_decompte.mp3 (dossier sfx/course/) — bip du décompte 3-2-1

```
Single clean countdown beep, mid pitch, racing game, 0.3 seconds.
```

### sfx_course_depart.mp3 (dossier sfx/course/) — signal de départ

```
Higher pitched start beep with a short rising sweep, racing game GO signal, 0.6 seconds.
```

### sfx_course_moteur-voiture.mp3 (dossier sfx/course/) — moteur en forme voiture (boucle, hauteur selon la vitesse)

```
Seamless looping futuristic sports car engine hum, steady mid revs, 2 seconds loop with no click at the loop point.
```

### sfx_course_moteur-robot.mp3 (dossier sfx/course/) — déplacement en forme robot (boucle)

```
Seamless looping heavy robot walking, soft servo motors and muffled mechanical steps, 2 seconds loop with no click at the loop point.
```

### sfx_course_changement-voie.mp3 (dossier sfx/course/) — changement de voie

```
Quick light sideways whoosh, 0.25 seconds.
```

### sfx_course_tour.mp3 (dossier sfx/course/) — passage de la ligne, nouveau tour

```
Checkpoint passing double beep, bright and clean, 0.5 seconds.
```

### sfx_course_depassement.mp3 (dossier sfx/course/) — on double un adversaire

```
Fast whoosh passing by with a doppler effect, racing, 0.8 seconds.
```

### sfx_course_depasse.mp3 (dossier sfx/course/) — un adversaire nous double

```
Deeper whoosh passing by with a doppler effect, being overtaken, 0.8 seconds.
```

### sfx_course_sprint.mp3 (dossier sfx/course/) — annonce du sprint final

```
Short alarm horn and rising siren sting announcing the final sprint, 1.5 seconds.
```

### sfx_course_arrivee.mp3 (dossier sfx/course/) — ligne d'arrivée

```
Race finish horn blast with a short crowd cheer, 2 seconds.
```

### sfx_questions_consigne.mp3 (dossier sfx/questions/) — une nouvelle consigne apparaît

```
Subtle soft notification blip as a new question appears, 0.3 seconds.
```

### sfx_questions_verrou.mp3 (dossier sfx/questions/) — la voie (la réponse) est verrouillée

```
Mechanical lock-in click with a short electronic confirm tone, 0.3 seconds.
```

### sfx_questions_bonne.mp3 (dossier sfx/questions/) — bonne réponse

```
Bright cheerful rising two-note success chime, game, 0.8 seconds.
```

### sfx_questions_mauvaise.mp3 (dossier sfx/questions/) — mauvaise réponse (doux, pas humiliant)

```
Soft low descending wrong-answer buzz, gentle and child friendly, not harsh, 0.7 seconds.
```

### sfx_questions_bloc-disparait.mp3 (dossier sfx/questions/) — le bloc de la bonne voie s'efface

```
Energy barrier dissolving with a short sparkling whoosh, 0.7 seconds.
```

### sfx_questions_collision.mp3 (dossier sfx/questions/) — collision avec un bloc

```
Heavy dull impact crash into a plastic barrier with a short rattle, 0.8 seconds.
```

### sfx_questions_serie.mp3 (dossier sfx/questions/) — série de bonnes réponses

```
Short triumphant combo fanfare, three quick rising notes, 1 second.
```

### sfx_formes_transformation-robot.mp3 (dossier sfx/formes/) — voiture vers robot

```
Cartoon mechanical transformation, metal panels sliding and clicking, servo whirs, a sports car turning into a robot, 0.8 seconds.
```

### sfx_formes_transformation-voiture.mp3 (dossier sfx/formes/) — robot vers voiture

```
Reverse mechanical transformation, a robot folding back into a sports car, panels clicking shut, engine revving at the end, 0.8 seconds.
```

### sfx_formes_recharge.mp3 (dossier sfx/formes/) — transformation de nouveau disponible

```
Small bright ready ping, ability recharged, 0.3 seconds.
```

### sfx_formes_robot-debloque.mp3 (dossier sfx/formes/) — déblocage du robot

```
Short heroic unlock fanfare with a metallic power-up sound, 2 seconds.
```

### sfx_formes_saut.mp3 (dossier sfx/formes/) — saut de la voiture

```
Spring suspension jump takeoff with a whoosh, sports car jumping, 0.6 seconds.
```

### sfx_formes_atterrissage.mp3 (dossier sfx/formes/) — atterrissage de la voiture

```
Car landing thud with a short suspension squeak, 0.5 seconds.
```

### sfx_formes_enjambement.mp3 (dossier sfx/formes/) — enjambement du robot

```
Heavy robot footstep stepping over an obstacle, metallic thud with a servo whine, 0.7 seconds.
```

### sfx_boost_debut.mp3 (dossier sfx/boost/) — activation du boost

```
Rocket flame ignition whoosh with rising pitch, 0.8 seconds.
```

### sfx_boost_boucle.mp3 (dossier sfx/boost/) — boost en cours (boucle)

```
Seamless looping continuous jet flame roar, 2 seconds loop with no click at the loop point.
```

### sfx_boost_fin.mp3 (dossier sfx/boost/) — fin du boost

```
Flame fading out with a sputter, 0.6 seconds.
```

### sfx_boost_jauge-pleine.mp3 (dossier sfx/boost/) — jauge de boost pleine

```
Energy fully charged ping with a sparkle, 0.6 seconds.
```

### sfx_ambiance_applaudissements.mp3 (dossier sfx/ambiance/) — podium

```
Crowd applause and cheering, 3 seconds with a natural fade out.
```
