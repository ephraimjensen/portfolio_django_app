# Overview

I wrote a web app using Django that I can use to showcase some of my software projects and to learn Django. I wanted to learn how use Django to make a web app that can query a database and dynamically generate pages. Upon arriving at the index, The user is directed to a homepage where they can see 3 of my projects and have the option to click a button to learn more. 

For part of this project, I followed a tutorial from RealPython.com, and copied some code from their website.

[Software Demo Video](https://www.loom.com/share/7303efc8477342a392833b20f635e8e2?sid=d4b4b9ef-e9b0-46d3-b748-deeaf4521575)

# Web Pages

I created 2 types of web pages, a homepage, and a project-specific page. The homepage displays three projects, shows a little information about each project, and has a pressable button that takes the user to that project's specific page. 

Each project is an entry in a SQLite database that Django creates from several Python Classes that have attributes. Each project has a name, a short and long description, a list of technologies used, and an image, with the option of adding an executable file and a video demo. When the homepage loads, the database is queried and all of these attributes are returned and dynamically filled for each project.

Once on the project-specific page, another query is made, this time only for one of the projects (identified by its primary key). The specific page then displays more information dynamically, omitting any potential absent information and including a bigger image, a longer description, and the technologies used to make the project, and the video demonstration. In addition to all that, if I later implement an in-browser demonstration for each project, this is where that would happen.

# Development Environment

I used Visual Studio Code to develop this software.

I created this software in Python using the Django and Bootstrap frameworks.

# Useful Websites

* [RealPython Django Tutorial](https://realpython.com/get-started-with-django-1/)
* [W3Schools Django Tutorial](https://www.w3schools.com/django/)


# Future Work

* Make projects demo-able
* Connect with GitHub
* Add more projects to the portfolio
* Add video to web app project