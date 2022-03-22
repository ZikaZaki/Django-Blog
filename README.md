# Django-Blog

[![Open in Visual Studio Code](https://img.shields.io/badge/|-Open%20in%20VS%20Code-1CA2F1.svg?style=flat&logo=visual-studio-code&logoColor=1CA2F1)](https://open.vscode.dev/ZikaZaki/Django-Blog)
![Python](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=ffdd54&color=3670A0)
![Django](https://img.shields.io/badge/django%20framework-%23092E20.svg?style=flat&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap%20v4-%23563D7C.svg?style=flat&logo=bootstrap&logoColor=white)
![Licence](https://img.shields.io/github/license/zikazaki/django-blog)
[![Visits Badge](https://badges.pufler.dev/visits/zikazaki/django-blog)](https://github.com/zikazaki/django-blog)

# Description

A __Django Blog Application__ built using Django framework. It is designed with all CRUD functionalities using Class-Based Views. This project is for beginners who want to learn Django framework.

## Installation

- First of all, you need to download Python from [here](https://python.org/downloads/), and install it on your computer.

- Clone the repository into a new folder.

    ```bash
    git clone https://github.com/ZikaZaki/Django-Blog.git
    ```

- Open the __Django-Blog__ folder in __Visual Studio Code__. If you don't have __VS Code__ you can download it from [here](https://code.visualstudio.com/download/).

- Create a __virtual environment__ and activate it using the following commands.

    ```bash
    python -m venv venv
    ```

    ```bash
    venv\Scripts\activate
    ```

- Once the virtual environment is activated, type the following commands in your shell in order to move to the __DBlog__ folder and install the __requirements.txt__ file.

    ```bash
    cd .\DBlog\
    ```

    ```bash
    pip install -r requirements.txt
    ```

- After installing the __requirements.txt__ file type the following commands in order to migrate all the tables to the database.

    ```bash
    python manage.py makemigrations
    ```
    
    ```bash
    python manage.py migrate
    ```

- After the migration process, type the following command to create an __admin user__ for the project.

    ```bash
    python manage.py createsuperuser
    ```
    


## Usage

Go to the __DBlog__ folder and run

```bash
python manage.py runserver
```

Then go to the browser and enter the url **http://127.0.0.1:8000/**


## Admin Login

You can access the django admin page at **http://127.0.0.1:8000/admin** and login with username and password specified in the 'createsuperuser' step. The default username is 'admin' and the default passowrd is 'admin'.

Also a new admin user can be created using

```bash
python manage.py createsuperuser
```

### Instructions

- Fork this Repository
- Clone your forked repository
- Add your scripts
- Commit & Push
- Create a pull request
- Star this repository
- Wait for Pull Request to merge
- Celebrate, your first step into the open Source World and contribute more

#### Note: When you Add a project Add it to the README for ease of finding it.

#### Note: Please do not put the project link to reference your local forked repo. Always link it to this repo after it's been merged with main.

## Contribution 🙌

Contributions are welcome, and they are greatly appreciated ❤️! Every little bit helps, and credit will always be given.


please star ⭐ the repo and feel free to make pull requests.