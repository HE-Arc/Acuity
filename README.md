# Acuity

## Description

Acuity est une application web _mobile first_ permettant aux individus d'une population d'évaluer leurs fréquentations. A la manière, de l'application dans l'épisode "Chute libre" de Black Mirror, chaque personne peut donner des notes aux autres en fonction de leurs agissements. La moyenne est calculée d'après toutes ses notes et est visible par tous. L'interface pour noter et commenter les utilisateurs se fait par la lecture d'un code QR que l'on pourrait imaginer porté par tous.

## Ranking

Une personne peut donner comme note, un nombre entier compris entre 0 et 5. La moyenne de chaque utilisateur est elle, affichée comme décimale avec un chiffre après la virgule. Une personne ne peut juger quelqu'un d'autre qu'une seule fois. Si je souhaite voter à nouveau pour un individu, mon ancienne note est modifiée.

## Installation

### Requirements

Installing required python dependencies in the newly created virtual environement

```bash
# In project root
pip install -r requirements.txt
```

Running the application locally

```bash
# /acuityproject/acuityclient/
npm install
npm run serve
```

```bash
# /acuityproject/
pip manage.py runserver
```

## Dependencies

### NodeJS

- @qvant/qui-max v0.9.1
- axios v0.26.0
- core-js v3.8.3
- qrcode.vue v3.3.3
- vue v3.2.13
- vue-material-design-icons v5.0.0
- vue-resource v1.5.3
- vue-router v4.0.13
- vue-sweetalert2 v5.0.2
- vuex v4.0.2
