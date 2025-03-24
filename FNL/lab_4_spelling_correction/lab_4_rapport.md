# Labo 4 – Correcteur Orthographique

## Objectif

Implémenter un correcteur orthographique en Python basé sur des opérations simples d’édition et un dictionnaire de fréquences extrait de Wikipédia.

## Fonctions principales

**Opérations d’édition (spelling_correction.py)**

- `ajouter_lettre(mot)` : ajoute une lettre à toutes les positions du mot.
- `supprimer_lettre(mot)` : supprime une lettre à chaque position.
- `substituer_lettre(mot)` : remplace chaque lettre par toutes les lettres de l’alphabet.
- `transposer_lettres(mot)` : échange deux lettres contiguës.
- `edits1(mot)` : retourne l’ensemble des mots à une distance d’édition 1.

**Chargement du dictionnaire**

- `load_dictionary(filename)` : charge un dictionnaire `mot -> fréquence` depuis un fichier `.tsv` et crée un second index `mot_sans_accent -> mot le plus fréquent`.

**Correction d’un mot**

- `correct_spelling(mot, dictionnaire, index_sans_accents)` : retourne la meilleure correction en cherchant dans :
  1. les mots à 1 edit présents dans le dictionnaire
  2. les versions sans accents
  3. sinon, retourne le mot original

## Tests

Les fonctions ont été testées dans `test_spelling_correction.py`.  

## Améliorations

L’accuracy a été améliorée grâce à la gestion des accents avec la bibliothèque `unidecode`.

Résultats d’évaluation sur le corpus de test :

1. 2000 articles : accuracy = 51.7%  
2. 200'000 articles : accuracy = 52.3%  
3. 200'000 articles + gestion des accents : accuracy = 72.58%

Un dictionnaire plus grand contient plus de mots rares, de noms propres et de fautes fréquentes, ce qui peut dégrader la précision sans traitement supplémentaire.

## Non implémenté

La correction avec 2 erreurs (2 edits) n’a pas été implémentée.
