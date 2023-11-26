# github_actions
Datascientest

> Path: 
> /home/ubuntu/Github/github_actions/**.github/workflows**
 

## Github - Introduction to CI / CD (FR)
multiple_shells.yaml
my_first_workflow.yml

## Github - Events & Actions (FR)

Tout d'abord, vous devez créer un script python qui contient des fonctions avec des assertions à tester. Pytest analysera toutes les fonctions de vos scripts mais il y a une condition : 
le nom de vos fonctions doit commencer par **test_.**

file_test.py

## Questions

Quel est la bonne pratique concernant l'emplacement des fichiers du workflow et les fichiers utilisés par le workflow ?
est-ce que tout dois se trouver dans le dossier ".github/workflows" ?

## Structure de l'arborescence

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