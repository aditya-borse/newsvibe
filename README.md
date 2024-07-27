# NewsVibe

## Barebons UI 
![NewsVibe UI](/home/aditya/projects/newsvibe/newsvibe_ui.png)

## Basic plan 

1. Create a new Django project and app

2. Web scraping
   - libraries: requests, beautifulsoup4
   - a scraper function to extract news from target websites

3. Sentiment analysis
   - library: TextBlob
   - a function to analyze sentiment of news titles

4. Database model
   - a django model for news articles
   - fields for title, link, sentiment, and summary
   - database migrations

5. Django views
   - a view for the news list page (home page)
   - a view for the article detail page
   - scraping and sentiment analysis into views

6. templates
   - base template
   - a template for the news list page
   - a template for the article detail page

7. URL routing
   - URL patterns for the news list and article detail pages

8. Basic frontend

9. Deploy