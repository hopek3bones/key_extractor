# keyword Extractor
Programme serveur qui fait de traitement de langue naturelle (NLP).
Actuellement, ce programme permet d'extraire les mots clés les plus
important dans un texte.

<br/>

## Installation et configuration

### Installation de python3
```sh
sudo apt install python3
sudo apt install python3-pip
```
Il faut s'assurer de la version de python qui est installée. La version de python
utilisée est `python 3.9.12`. Tu peux aussi utiliser la version `3.8`.


### Installation de venv
```sh
sudo apt install python3-venv
```
OU
```sh
sudo pip3 install virtualenv
```

### Créer un environnement virtuel
```sh
python3 -m venv env
```
OU
```sh
virtualenv env -p python3
```

### Démarrage de l'environnement
```sh
source env/bin/activate
```

### Installation des dépendances
```sh
pip install -r requirements.txt
```
<br/>

### Démarrage du serveur de django
```
./manage.py runserver
```
Résultats dans le terminal, qui indique que tout va bien est :
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 21, 2022 - 07:53:49
Django version 3.2.6, using settings 'docs.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Utilisation
### Extration de mot-clés
Pour ouvrir l'API d'extraction de mot-clés, il faut taper le lien suivant
dans le navigateur : http://127.0.0.1:8000/api/get/keywords/ ensuite
peut essayer avec le code JSON suivant:

```json
{
"text":"Un réseau de télévision est un réseau de télécommunications destiné à la distribution de programmes télévisés. Cependant, le terme désigne désormais un groupement d'affiliés régionaux autour d'une chaîne de télévision centrale, offrant une programmation à plusieurs stations de télévision locales. Jusqu'au milieu des années 1980, la programmation télévisée de la plupart des pays du monde a été  dominée par un petit nombre de réseaux de diffusion. Bon nombre des premiers réseaux de télévision (comme la BBC, NBC ou CBS) se sont développés à partir de réseaux de radio existants."
}

```

<br/>
<br/>

