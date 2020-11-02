# Semaine de Formation du 2 au 6 novembre 2020 - M2-IOT  

_______________

# Au programme 🤖

* Lundi 2 novembre :
	* Rapels docker & ML 
  
* Mardi 3 novembre :   
	* Deploiement & production 
		* Streamlit et FastAPI 
		* Test sur le cloud Heroku
  
* Mercredi 4 novembre : 
	* Workshop PostgreSQL 
	* Début mini-projet

* Jeudi 5 novembre : 
	* Mini Projet   

* Vendredi 6 novembre :   
	* soutenance projet


_______________



## Suivi 📈

Créer un repo github et faire a minima deux pushs par jour (matin : 11h30 & aprem : 16h30) afin que je vois ou vous en êtes 👌


## Rappels Docker et ML 👨‍🎓

Docker est un logiciel libre permettant de lancer des applications dans des conteneurs logiciels.
Il ne s'agit pas de virtualisation, mais de conteneurisation, une forme plus légère qui s'appuie sur certaines parties de la machine hôte pour son fonctionnement. Cette approche permet d'accroître la flexibilité et la portabilité d’exécution d'une application, laquelle va pouvoir tourner de façon fiable et prévisible sur une grande variété de machines hôtes, que ce soit sur la machine locale, un cloud privé ou public, etc. Plus d'information sur la documentation officielle [ici](https://docs.docker.com/v17.09/). 

Docker a été inventé pour résoudre un probleme classique que nous avons tous rencontré en informatique. 
Un meme parle toujours mieux que milles mots : 
<div style="text-align:center">
<img src="https://external-preview.redd.it/aR6WdUcsrEgld5xUlglgKX_0sC_NlryCPTXIHk5qdu8.jpg?auto=webp&s=5fe64dd318eec71711d87805d43def2765dd83cd">
</div>


### Vos missions 


**Quickstart** 

* comprendre la différence entre images et containers et à quoi sert un `Dockerfile` 
* installer docker sur votre machine (Ubuntu de préférence) 
* lancer votre premier container ubuntu, l'équivalent du *hello-world* de docker  
* regarder si votre container est bien lancer 
* faire un résumé type `cheat sheet` des principales commandes dockers relatives aux images et containers 
* vérifier en vous connectant à votre container qu'il est bien `up` et qu'il s'aggit bien 
* **(bonus)** lancer un petit container applicatif en python avec docker 


**TP 1 - DS Sand box container**

* coder un container type *data engineering sandbox* à partir d'une image Ubuntu contenant : 
	* un espace de travail appelé workspace 
	* python3, pip3 et vim 
	* une installation automatique du fichier `requirements.txt`
	* un set up des credentials git pour l'utilisateur du container
	* une exposition du port 8000 
	* pour finir le container devra lancer jupyter notebook avec votre git clonné à la racine 
	* **(bonus)** inclure un environement virutelle deep-learning `Python 3.8.0` (sous forme `ipykernel`) et installer `tensorFlow` et `scikit-learn` dessus
* Lancer le container avec docker-compose 
	* Se renseigner sur la syntaxe `yml` et les fichier `.yaml`
	* Ecrire un fihier `docker-compose.yml` qui contient le service conteneurisé de la question precedente
	* Se renseigner sur les volumes et les networks docker
* faire un push de votre travail sur votre repo.  

#### Dire ce que font les commandes suivantes avant de les appliquer     
```bash
$ sudo groupadd docker
$ sudo gpasswd -a $USER docker
```


## Deploiement & production 🛰

Un déploiement est l’action d’installer du logiciel sur un environnement (cloud ou physique) et une une mise en production est l’action de procurer ce logiciel aux utilisateurs (valeur métier). 

### Dans notre cas nous allons parler d'API. 

Une API (Application Programmable Interface) est un ensemble de fonctions permettant à une application d'offrir des services à d'autres logiciels. Une API peut être distribué localement dans un programme informatique ou au contraire peut avoir vocation a être utilisée par un plus grand nombre d'acteurs.

Dans ce cours nous nous intéressons surtout au API Web, c'est-à-dire celles qui permettent de fournir une interface accessible en ligne. Cela est le cas lorsque l'on effectue une requête à un serveur afin que l'on reçoive le résultat d'un traitement. 

### REST

L'architecture REST est, depuis $10$ ans, une des architectures les plus utilisées. En effet, elle est rapide a mettre en place, extrêmement puissante et répond à une très large majorité des cas. Par exemple, supposons que l'on souhaite un ensemble de programmes (site Web, application Smartphone) permettant de réserver et de gérer ses vols d'avions. Une architecture REST pourrait centraliser les fonctionnalités comme le montre le diagramme suivant.

![Exemple d'architecture REST](https://i.ytimg.com/vi/UQwjytQzoqE/maxresdefault.jpg)


### Les Routes

Les requêtes HTTP se caractérisent par des **routes** : il s'agit d'un chemin permettant de structurer l'accessibilité des opérations. Reprenons l'exemple de gestion de vols d'avions :
- la route http://monserveur.com/list permet de lister les vols disponibles
- la route http://monserveur.com/fly permet d'ajouter ou modifier un vol
- la route http://monserveur.com/action/disconnect permet de déconnecter l'utilisateur
Cette structuration permet ainsi d'organiser toutes les fonctionnalités disponibles via l'API de manière cohérente et ergonomique. Les routes *list*, *fly* et *action/disconnect* sont donc définies par l'architecte logiciel dans le code de l'API.

### Les verbes HTTP

La philosophie de l'architecture REST est de proposer une route permettant d'effectuer un traitement en rapport avec une action précise. Par exemple, la route *fly* permet d'ajouter ou modifier un vol, mais comment spécifie-t-on précisement si l'on souhaite ajouter, modifier ou supprimer un vol ? C'est ainsi que les verbes HTTP ont été conçus pour faciliter cette interaction :

- **GET** effectue une lecture
- **POST** crée une donnée
- **PUT** met à jour une donnée
- **DELETE** supprime une donnée

#### Les principaux codes HTTP 

Lorsque l'on effectue une requête, un code HTTP est automatiquement fourni. Ce code permet d'identifier le résultat d'une requête ou d'indiquer une éventuelle erreur lors du traitement d'une requête. Les plus connues sont :

* 200 : Succès
* 400 : Erreur de syntaxe
* 404 : Introuvable
* 403 : Interdit
* 500 : Erreur interne
	
Lorsque l'on code une API REST, il est fortement conseillé de fournir des codes HTTP spécifiques pour informer les utilisateurs de l'état d'une requête.

Plus d'informations [ici](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP) 👀

Avant de construire une API on va sortir de notre localhost et voir ce que ca peut donner sur le web. Pour cela on va s'intéresser à un framework python [streamlit](https://www.streamlit.io) qui permet de deployer rapidement des models ainsi que des visualisation rapide. 


**TP2 - Streamlit Introduction** 

* Parcourir le tutorail de streamlit.io 
* Télecharger le dataset suivant : https://drive.google.com/file/d/1OEWrVjE7B2d23-eQrTMcJpRJMxoB6iUH/view?usp=sharing 
* faite un script `algo.py` qui á partir des données, les clean, effectue la pipeline ci-dessous et sort un fichier dump du model entrainer. 
```
clf = make_pipeline(
    TfidfVectorizer(stop_words=get_stop_words('en')),
    OneVsRestClassifier(SVC(kernel='linear', probability=True))
)
```
	* Se renseigner sur les algorithmes de la pipeline ci-dessus et les differents paramètres de ces derniers 
* Créer une application streamlit qui prend un texte en entrée et renvoie une probabilité suivant les 3 classes du fichier.   
* **(bonus)** deployer un algorithme ML sur le dataset de votre choix avec streamlit 
* **(bonus)** realiser une mini app avec le workflow data complet (de la collecte, data analyse, ml et l'affichage de vos résultats)
* faire un push de votre travail sur votre repo.  

*PS : pour ce TP nous ne nous occuperons pas des performances de l'algorithme deployé.* 


**TP3 - FastAPI Introduction** 

* se renseigner sur les API de façon générale et à quoi cela sert, quel interet peut avoir une entreprise à développer des services API
* se renseigner sur FastAPI et faire une petite application qui renvoie `hello word`, expliquer ce qu'est une route. Expliquer la difference entre les fonction classique et les fonctions `async`. 
* Que fait la class `BaseModel` et comment l'utilise t'on?
* charger un dump d'un model ML et faite une route prediction (vous pouvez vous appuyer sur le dataset fournit au TP2 ou bien prendre les data de votre choix. 
* faire un repo `/test` à la racine de votre projet et insérer un fichier `/test/test_api.sh` pour tester votre api
* **(bonus)** mettre en production un model ML à partir des data de votre choix
* **(bonus)** containeriser votre api avec Docker 
* faire un push de votre travail sur votre repo.  


**TP4 - Deploiement & production avec Heroku** 

* Regarder l'exemple en ligne de : https://www.heroku.com
	* faite un résumé du workflow de déploiement ainsi que des principales commandes 
* Deployer un algorithme de ML sur les données de votre choix (attention Heroku ne vous donne pas accès à plus de 500Mo dans sa version gratuite, vous devez donc optimiser au mieux la place de votre image Docker)
* **(bonus)** deployer votre application sur GCP 

## Workshop postgreSQL & Docker 🚀



src : http://b3d.bdpedia.fr/docstruct.html 


**TP5 - PostgreSQL & Docker** 

* lancer un container postgresql et familiarisez vous avec la cli (commande `psql`)
* ecrire un fichier `docker-compose.yml` avec un service `database`, un fichier d'environement `database.env` et un volume `database-data`
	* Pourquoi utiliser un fichier d'environement ?
	* Pourquoi monter un volume ?  
* Run le container et entrer dedans afin d'insérer une base de données avec au moins 5 champs. 
	* run le container avec `docker exec`
	* run le container avec `docker-compose run` 
	* Expliquer la difference entre ses commandes
	* Que fait le fichier `docker-entrypoint.sh` à la racine du container?  
* Executer une requête afin de vérifier que les données sont bien en base.  
* **(bonus)** faite un dump de votre container et restaurez le
* **(bonus)** faite un script python qui effectue les opération CRUD sur votre base de données docker. 

- - - - - 

## Les ressources utiles 👀

### Les bases en rapide
- python doctor : https://python.doctor
- glossaire ml/ia : https://developers.google.com/machine-learning/glossary 
- Cheat sheet ml/ia : https://ml-cheatsheet.readthedocs.io/en/latest/

### POstgreSQL
- quick tuto : https://www.tutorialspoint.com/postgresql/index.htm
- practical command : https://www.postgresqltutorial.com/psql-commands/ 


### Pour les api 
- FastAPI doc : https://fastapi.tiangolo.com

### Docker 
- doc : https://www.docker.com
- how to write a dockerfile : https://www.educative.io/edpresso/how-do-you-write-a-dockerfile | https://www.codementor.io/@aviaryan/writing-your-first-dockerfile-7e0rjhual 
- plus de détail : https://takacsmark.com/dockerfile-tutorial-by-example-dockerfile-best-practices-2018/ 
- best practice : https://engineering.bitnami.com/articles/best-practices-writing-a-dockerfile.html 
- pour aller plus loin : https://www.katacoda.com/courses/container-runtimes 
