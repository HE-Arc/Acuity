# Acuity

## Descriptif

Acuity est une application web _mobile first_ permettant aux individus d'une population d'évaluer leurs fréquentations. A la manière, de l'application dans l'épisode "Chute libre" de Black Mirror, chaque personne peut donner des notes aux autres en fonction de leurs agissements. La moyenne est calculée d'après toutes ses notes et est visible par tous. L'interface pour noter et commenter les utilisateurs se fait par la lecture d'un code QR que l'on pourrait imaginer porté par tous.

## Ranking

Une personne peut donner comme note, un nombre entier compris entre 0 et 5. La moyenne de chaque utilisateur est elle, affichée comme décimale avec un chiffre après la virgule. Chaque note a un coefficient; celui-ci est calculé d'après la moyenne de la personne qui juge. Le coefficient peut donc varier, par exemple: si la moyenne de la personne qui m'a noté hier baisse, ma moyenne va changer en fonction. 

Une personne ne peut juger quelqu'un d'autre qu'une seule fois. Si je souhaite voter à nouveau pour un individu, mon ancienne note est modifiée.

## Contenu

### MVP

- Register / Login / Logout
- Page profil personnel avec code QR (lien pour noter le profil)
- Page d'accueil (description et détails de l'app)
- Page du classement
- Page profil à noter (profil autres utilisateurs)

### Secondaire

- Scan de code QR _in app_
- Création et affichage de commentaire lors de la notation

### Optionnel

- Création d'évennements exclusif aux notes des utilisateurs
- Graphique d'évolution des notes d'un utilisateur

https://hackmd.io/@3-timeshare/SklbkGlCt
