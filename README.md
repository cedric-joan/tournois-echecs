# Projet 4 - Tournois-D'échec

## Description

"Projet 4 - Tournois-d'échec" est un programme à réaliser dans le cadre de la formation diplômante d'OpenClassrooms "Développeur d'application Python".

Ce projet a comme but de mettre en place un tournoi d'échecs (système suisse) dont le déroulement de base est : 

1) L'utilisateur crée un nouveau tournoi.
2) L'utilisateur ajoute huit joueurs par tournoi.
3) L'ordinateur génère des paires de joueurs pour le premier round.
4) L'utilisateur entre les résultats des matchs du round.
5) L'ordinateur génère des nouvelles paires de joueurs jusqu'à ce que les 4 rounds soient joués, et que le tournoi soit terminé.
6) L'utilisateur peux afficher les rapports:
- Liste de tous les joueurs par ordre alphabétique.
- Liste de tous les tournois.
- nom et dates d'un tournoi donné.
- Liste des joueurs du tounois par ordre alphabétique.
- Liste de tous les tours du tournois et de tous les matchs du tour.


Les consignes techniques à développer/suivre sont :
- La conformité avec la PEP8.
- Un code maintenable que possible afin d'éviter les bugs.
- La mise en place du modèle MVC (Model-View-Controller).
- Le peluchage du code grâce à Flake8.
- L'utilisation de TinyDB pour la base de données.

## Installation

Python version : 3.9
<création du venv>
python3 -m venv env

Les dépendances sont listées dans le fichier `requirements.txt`.
Lancer :

```
pip install -r requirements.txt
```

## Use
Lancer le script :

```
python main.py
```

## Code Quality

Flake8 est utilisé pour la mise en forme et le nettoyage du code.
La configuration se trouve dans le fichier `.flake8` 
Pour démarrer, executer:
```
flake8_report_generator.py
```

