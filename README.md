# Blogpost

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/santoshshresthasaiju/Blogpost.git 
$ cd Blogpost
```
Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
# for windows 
$ env\Scripts\activate
```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal session operates in a virtual environment set up.

Once `pip` has finished downloading all the dependencies:
```sh
(env)$ cd blog
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Key Features
1. Post Management: Create, view, comment on posts.
2. User Authentication: Secure login and registration.
3. Forms: Django ModelForms for post/comment creation.
4. Templates: Responsive Bootstrap 5 templates.
5. Pagination: For post lists.
6. Messages Framework: Success/failure notifications.
7. Search: Filter posts by title/content.
8. User Profiles: Display user posts on profile pages.