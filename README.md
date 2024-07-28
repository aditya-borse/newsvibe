# NewsVibe
# Description
This project is a Django-based web application that fetches and displays articles. The articles are fetched from an external source(the hindu,newsscientist), processed, and stored in a database. Each article has a title, description, thumbnail link, link, summary, and sentiment.

# Installation
Clone the repository: git clone https://github.com/aditya-borse/newsvibe.git

Navigate to the project directory: cd newsvibe

Install the required packages: pip install -r requirements.txt

Run the migrations: python manage.py migrate

Start the server: python manage.py runserver

# Usage
Once the server is running, you can access the application at http://localhost:8000.

# Code Structure
The main logic of the application is in the views.py file. This file contains a function that fetches the articles, processes them, and stores them in the database. Each article is represented as an instance of the article model.

The article model is defined in the models.py file. It has fields for the title, description, thumbnail link, link, summary, and sentiment of an article.

The articles are displayed in the home.html template. This template uses the Django templating language to loop over the articles and display their information.

scrapper file in mainapp is code that scraps the both website (the hindu and newscietist) and passes the thumbnai link, title, link , text and summary.

sentiment file in mainapp is code where we analyze the sentiment of text that we scrapped in scrapper.py

# License
This project is licensed under the MIT License.