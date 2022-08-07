## General Features

- Uses only HTML, so pages are very fast and responsive
- Messaging feature is built from scratch, no tutorials watched
- Has Users, Documents, Grades and Communication apps

### Users

- 2 types - **Student** and **Instructor**, **Admin** is managed by django default admin stuff
- **Course** can be registered by admin

### Grades

- simple grades out of 100 (intended)

### Documents

- Upload on any cloud and add document using link on admin page

### Communication

- Has **announcement** for courses
- Has **Reply** for the announcement
- Has **Messages** to message people

# Known Issues

- Grades can be added in courses in which the student has not registered. To be fixed later by adding some forms and checks
- Reply isn't in threads. Can be fixed later by setting target of replies
- More forms needed so that dependence on admin page becomes less
- More permission checks to be implemented
- Using no CSS/JS makes site look bad. It loads fast though.
- Admin has to do almost everything, forms in the future will divide this work
- No email feature added

# DevClub Assignment 5

You have learnt about backend engineering with Django in our session. Now use it to create a web application by yourself!

## DevClub LMS (Learning Management System)

You must have used **Moodle** in your courses, where both instructors and students login, and for each course, the instructor uses the platform to share resources, send announcements, release grades, conduct quizzes and what not!

Your task is to create your own such a learning management system using Django, where you can add functionalities as per your own creativity!

### We would recommend you to have these apps inside the project:

- Users (to store auth logic, and models for `Instructor`, `Student`, `Course`, `Admin`)
- Grades (to store logic for sharing grades for any assessment, and models for let's say a class `Grade`)
- Documents (for Instructor to upload `Docs` like lecture notes for the course)
- Quizzes (this can have models for a `QuestionBank` containing `Question`'s which form a `Quiz`)
- Communication (to work on features like Course-wide `Announcements`, `Reply`ing in threads to announcements, sending personal `Messages`)

Try to implement as many features as you can, but make sure to plan the structure of the project and database schemas well!

### Bonus:

- Deploy on Heroku
- Create documentation for any RESTful APIs created with documenter on postman
- Markdown support for Communication
- Email: For registration, password reset, notifications, instructor custom message
- Bulk upload from CSV for grades, quizzes
- Generating PDF: Print digitally signed transcript
- Add security features for the quizzes

## Submission Instructions

- **FORK** this repository, by clicking the "Fork" button on top right
- `clone` the forked repo into your machine, and `cd` into the Repo Folder such that you are in same directory level as `manage.py`
- If on macOS, run `python3 -m venv env`, otherwise `python -m venv env`
- Now activate the virtual environment by `source env/bin/activate`
- See if the environment is correctly set by running `pip list`, it should be mostly empty
- Install dependencies with `pip install -r requirements.txt`
- We have already started a dummy project called `DevClubLMS` for you
- Now, you can use `python manage.py runserver` to start the dev server or `python manage.py startapp <appname>` to create a new app inside this project
- After completing the assignment, append instructions to run your project, along with explanation of features etc in this README
- It would be nice if you can host it on Heroku and also give a documentation of each endpoint through postman
- Finally submit with your details in the [Google Form](https://forms.gle/XSidrfbrsEZuDYfy6)
- You do NOT need to make any pull requests to this repo

# Resources

- [Slides used in the session](https://docs.google.com/presentation/d/e/2PACX-1vQbtDDGQonkIoGu68VrINL2s3sQcfiH5XVnk-iU26nk16DFBGsDabichsqhdtBvowPvpxaIbFLAV2h3/pub?slide=id.p)
- Introduction to Python and Django by [Programming With Mosh](https://youtu.be/_uQrJ0TkZlc)
- Detailed Django Tutorials by [Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- [Mozilla's Tutorials](https://developer.mozilla.org/en-US/docs/Learn/Server-side) on Server Side Programming with Django
- [Django Official Docs](https://www.djangoproject.com/start/)
- [Talk](https://youtu.be/lx5WQjXLlq8) on how Instagram uses Django at production, and also [_the time when Justin Beiber almost crashed Instagram!_](https://youtu.be/lx5WQjXLlq8?t=715)
- Advice on Backend Engineering by [Hussein Nasser](https://www.youtube.com/c/HusseinNasser-software-engineering)
- Guide for Deploying Python apps on [Heroku](https://devcenter.heroku.com/categories/python-support)
- Guide for [Postman Documenter](https://learning.postman.com/docs/publishing-your-api/documenting-your-api/)
