# Effective Stream Analysis with Data Science Technologies

In the business world, customer feedback is highly important. Some companies provide a feedback system for the customers, but only a small amount of the customers actually uses this practical opportunity. The real feedback comes from the news and from online streams. These are either written by, or for the customers. These are usually the main sources for the companies. Some bigger companies order statistics and summaries from analyzer companies. These companies collect, clean and analyze the data that comes from online streams and news sources.
The task is about finding a solution to automate these collecting, filtering, cleaning, and analyzing processes. The task includes getting familiar with popular data analytic systems, server side development, and creation of a client software. The process starts with the collection of data, and ends with the result of the analysis. The main result of the task is a website that shows if a keyword is a positive or a negative phrase according to the streams. 


#Modules
##Scraping

This module scrapes the news portals. The portals rss link should be included in "rss_site.links.json" file. This module also clean the data and write it into the database.

##Word2Vec

This module takes the cleaned data and generate the word vectors.

##PrepareCorpus

This module is supposed to be built. It can be used as a executable. This module takes the searched expression and select all the relevant content out of the cleaned data, and write the created corpus to the database.

##SentimentalService

This module is supposed to be built. It can be used as a executable. This module takes the created corpus and return its positive percent.

##Website

This module is a PHP website. It uses the PrepareCorpus and SentimentalService to display positive percent of the searched word.