# DJANGO-petclinic

Application Pet Clinic construite avec le framework Django.

## Prerequis

- Python 3.10+ recommande
- `pip`
- (Optionnel) `git`

## Installation du projet

### 1) Cloner le projet

```bash
git clone <URL_DU_REPO>
cd DJANGO-petclinic
```

### 2) Creer et activer l'environnement virtuel Python

#### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si l'activation est bloquee par la policy PowerShell :

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

#### Windows (Git Bash)

```bash
python -m venv .venv
source .venv/Scripts/activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Installer les dependances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Initialiser la base de donnees

Depuis la racine du projet (`manage.py`) :

```bash
python manage.py makemigrations
python manage.py migrate
```

## Creer un super utilisateur (admin Django)

```bash
python manage.py createsuperuser
```

Ensuite, connectez-vous sur l'admin Django :

- URL admin : `http://127.0.0.1:8000/admin/`

## Demarrer le serveur de developpement

```bash
python manage.py runserver
```

Application accessible sur :

- `http://127.0.0.1:8000/`

## Ou se trouve la base de donnees ?

Par defaut, ce projet utilise SQLite avec le fichier :

- `db.sqlite3` (a la racine du projet)

## Commandes utiles (quotidien)

### Verifier les migrations en attente

```bash
python manage.py showmigrations
python manage.py makemigrations --check --dry-run
```

### Ouvrir un shell Django

```bash
python manage.py shell
```

### Lancer les tests

```bash
python manage.py test
```

### Collecter les fichiers statiques (si necessaire)

```bash
python manage.py collectstatic
```

### Desactiver l'environnement virtuel

```bash
deactivate
```

## Reinitialiser rapidement la base SQLite (developpement uniquement)

> Attention : supprime toutes les donnees locales.

#### Windows (PowerShell)

```powershell
Remove-Item db.sqlite3
python manage.py migrate
```

#### macOS / Linux / Git Bash

```bash
rm -f db.sqlite3
python manage.py migrate
```

## Depannage (erreurs frequentes)

### 1) `python` n'est pas reconnu

Sous Windows, essayez d'abord :

```powershell
py --version
py -m venv .venv
```

Puis remplacez `python` par `py` dans les commandes si necessaire.

### 2) L'environnement virtuel ne s'active pas (PowerShell)

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 3) `ModuleNotFoundError: No module named 'django'`

Le plus souvent, le venv n'est pas actif ou les dependances ne sont pas installees :

```bash
pip install -r requirements.txt
```

### 4) `You have unapplied migrations`

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5) Le port 8000 est deja utilise

Demarrer sur un autre port :

```bash
python manage.py runserver 8001
```

Ou liberer le port sous Windows :

```powershell
Get-NetTCPConnection -LocalPort 8000 | Select-Object -ExpandProperty OwningProcess
Stop-Process -Id <PID> -Force
```

### 6) Le superuser existe deja

Si vous avez oublie le mot de passe :

```bash
python manage.py changepassword <username>
```

### 7) Base SQLite verrouillee (`database is locked`)

Actions conseillees :

- Arreter le serveur Django en cours (`Ctrl+C`)
- Fermer les shells qui utilisent la base
- Relancer le serveur avec `python manage.py runserver`


