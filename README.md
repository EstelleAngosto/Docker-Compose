# Introduction

Dans le cadre de l'ECUE 431 : Gestion de stockage des données de santé et virtualisation, nous avons eu l'occasion de
travailler avec plusieurs services permettant l'exécution de tâche virtuelle et qui facilite le déploiement en plusieurs
endroits d'une solution. Nous avons notamment travaillé avec Docker et lors de notre dernier TP, nous devions mettre en place
un fichier Docker Compose opérationnel afin de construire et de lancer en même temps plusieurs Docker Container.

Dans le sujet concernant les IAs, nous devions découper un algorithme de machine learning en trois parties :
_ Une partie qui prépare les données et qui les découpe en base de test et en base d'entrainement.
_ Une seconde partie qui va s'occuper de la phase d'entrainement du modèle et de son extraction.
_ Une troisième partie qui va tester le modèle et afficher le résultat.

Pour ma part, je suis restée sur l'estimation de prix de maison en Califorie.

# Installation de Docker

Pour installer Docker, nous avons suivi la succession de ligne de commande suivante :
`sudo apt update`
`sudo apt upgrade`
`sudo apt-get install  curl apt-transport-https ca-certificates software-properties-common`
`curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
`sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`
`sudo apt update`
`sudo apt install docker-ce`

# Structure du projet

Ce projet a été réalisé sur une machine virtuelle Ubuntu grâce à Vagrant.
Vous pourrez normalement retrouver le contenu de cette machine virtuelle dans les fichiers de ce dépôt Github.
Une fois les fichiers récupérés, vous pouvez lancer la machine avec la commande : `vagrant init`
Vous pourrez travailler dans la machine avec la commande : `vagrant ssh`

Concernant notre projet, nous avons créé un répertoire **DockerCompose_ML** dans lequel se trouve un fichier **compose.yml** pour faire
marcher notre Docker Compose et de trois dossiers, Base, Train et Test, pour représenter chaque partie du projet.

Dans chacun de ces répertoires, on trouve un script python, un fichier requirement.txt et un Dockerfile.
