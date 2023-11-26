# github_actions
Datascientest

Path Workflow : /home/ubuntu/Github/github_actions/**.github/workflows**
Path Files : /home/ubuntu/Github/**github_actions/**

> Project, settings, Actions New repositories secrets:
```
    NAME : ACTIONS_RUNNER_DEBUG
    KEY: true
    NAME : ACTIONS_STEP_DEBUG
    KEY: true
```

## Github - Introduction to CI / CD (FR)
* multiple_shells.yaml
* my_first_workflow.yml

## Github - Events & Actions (FR)
* file_test.py = Resultats: logs_10.zip avec erreur, puis corrige selon Convention PEP8
* test_calculations.py ; > calculs.py = Perso

Tout d'abord, vous devez créer un script python qui contient des fonctions avec des assertions à tester. 
Pytest analysera toutes les fonctions de vos scripts mais il y a une condition : 
le nom de vos fonctions doit commencer par **test_.**


### Modifications apportees :

Espacement autour des Opérateurs : Ajout d'espaces autour des opérateurs +, -, et * pour améliorer la lisibilité.
Commentaires : Les commentaires commencent par une majuscule et sont placés sur une ligne distincte au-dessus du code auquel ils se réfèrent. Cela rend le code plus lisible et conforme aux standards de PEP 8.
Importation de Pytest : Comme discuté précédemment, l'importation de pytest n'est pas nécessaire pour ce script de test. Vous pouvez la supprimer pour un code plus propre, sauf si vous utilisez des fonctionnalités spécifiques de pytest.
L'erreur E501 signalée par flake8 indique qu'une ligne de votre code dépasse la limite maximale de 79 caractères recommandée par PEP 8.

> Ces ajustements rendront votre code conforme aux conventions de style PEP 8, qui sont largement adoptées dans la communauté Python pour maintenir la cohérence et la lisibilité du code.

### Questions

Quel est la bonne pratique concernant l'emplacement des fichiers du workflow et les fichiers utilisés par le workflow ?
est-ce que tout dois se trouver dans le dossier ".github/workflows" ?

Revoir les conventions PEP8 pour le code. 

## Structure de l'arborescence

```
ubuntu@ip-172-31-23-56:~/Github$ sudo apt  install tree
ubuntu@ip-172-31-23-56:~/Github$ tree -a 
.
└── github_actions
    ├── .git
    │   ├── COMMIT_EDITMSG
    │   ├── FETCH_HEAD
    │   ├── HEAD
    │   ├── branches
    │   ├── config
    │   ├── description
    │   ├── hooks
    │   │   ├── applypatch-msg.sample
    │   │   ├── commit-msg.sample
    │   │   ├── fsmonitor-watchman.sample
    │   │   ├── post-update.sample
    │   │   ├── pre-applypatch.sample
    │   │   ├── pre-commit.sample
    │   │   ├── pre-merge-commit.sample
    │   │   ├── pre-push.sample
    │   │   ├── pre-rebase.sample
    │   │   ├── pre-receive.sample
    │   │   ├── prepare-commit-msg.sample
    │   │   └── update.sample
    │   ├── index
    │   ├── info
    │   │   └── exclude
    │   ├── logs
    │   │   ├── HEAD
    │   │   └── refs
    │   │       ├── heads
    │   │       │   └── main
    │   │       └── remotes
    │   │           └── origin
    │   │               ├── HEAD
    │   │               └── main
    │   ├── objects
    │   │   ├── 03
    │   │   │   └── 6931241d0550068e2a92d68e55d0d05b0bddfb
    │   │   ├── 13
    │   │   │   └── ...
    │   │   ├── f8
    │   │   │   └── 29e79c3387497873d39e1f3c2ecf3ee37e19e7
    │   │   ├── info
    │   │   └── pack
    │   ├── packed-refs
    │   └── refs
    │       ├── heads
    │       │   └── main
    │       ├── remotes
    │       │   └── origin
    │       │       ├── HEAD
    │       │       └── main
    │       └── tags
    ├── .github
    │   └── workflows
    │       ├── control_tests.yaml
    │       ├── file_test.py
    │       ├── multiple_shells.yaml
    │       └── my_first_workflow.yml
    └── README.md

38 directories, 50 files
```