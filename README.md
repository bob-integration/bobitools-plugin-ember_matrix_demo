# Démo matrice Ember+ — plugin Bobi.Tools

Une matrice de démonstration **4×4** en mémoire pour [Bobi.Tools](https://github.com/bob-integration/bobitools),
qui sert à essayer le service [Ember+](https://github.com/bob-integration/bobitools-service-emberplus)
**sans matériel**.

## Ce que fait l'outil

- Déclare au service Ember+ une matrice `oneToN` de 4 sources (`SRC1`…`SRC4`) et
  4 destinations (`DST1`…`DST4`).
- Applique les commutations reçues d'un contrôleur broadcast ou de tout consumer Ember+.
- Affiche l'état courant des connexions (destination ← source).
- Sert d'exemple minimal de contributeur Ember+ : `GET ember/tree` déclare l'arbre,
  `POST ember/connect` applique un point de croisement (voir [`backend.py`](backend.py)).

## À savoir

L'état vit en mémoire : il revient à la diagonale (DST*n* ← SRC*n*) à chaque redémarrage de
Bobi.Tools.

## Prérequis

- Aucun : l'outil tourne dans Bobi.Tools.
- Le service [Ember+](https://github.com/bob-integration/bobitools-service-emberplus), qui
  publie la matrice sur le réseau.

## Installation

Dans Bobi.Tools : **Réglages → Outils → Catalogue**, bouton « Installer ». Ou, sur une machine
neuve, en une ligne :

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/bob-integration/bobitools/main/get.sh) --outils ember_matrix_demo
```

## In English

An in-memory 4×4 oneToN demo matrix for Bobi.Tools, used to try the Ember+ service and its
Matrix support without any hardware. It is also the smallest example of an Ember+
contributor (`ember/tree` + `ember/connect`). Requires the `emberplus` service.

## Licence

GPL-3.0-or-later — © 2026 BOBI SAS. Voir [LICENSE](LICENSE).
