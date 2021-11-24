# Django Web Scrapper

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/al-jaber-nishad/django-job-scrapper.git
$ cd django-job-scrapper
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.



## Walkthrough

# ![Django DRF Example App](django-jobs-scrapper.png)

### Bd-Jobs
This portion shows all the available Django Stack jobs inside Bangladesh. And the informations are scrapped from `www.careerjet.com`.

### Ind-Jobs
Available remote Django Stack internships in India will be shown here. These informations are scrapped from `www.internshala.com`.