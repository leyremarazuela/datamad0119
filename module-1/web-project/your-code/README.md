# Guided Project: API and Web Data Scraping

## Overview

The goal of this project is to choose both an API to obtain data from and a web page to scrape. For the API portion of the project, we will  make calls to our chosen API, successfully obtain a response, request data, convert it into a Pandas data frame, and export it as a CSV file. For the web scraping portion of the project, we will scrape the HTML from our chosen page, parse the HTML to extract the necessary information, and save the results to a CSV file if it is tabular data.

In this project we will investigate the biggest venture capital firms in the world, through a variety of measures such as location and assets owned. Meanwhile, we will link this information to an API that allows people to find out more details about each company.

Overall the project consists of a series of steps as outlined below. 

---
## Intro: Understand data

1. Web scraping from Wikipedia page on list of VC firms = 'https://en.wikipedia.org/wiki/List_of_venture_capital_firms'
   Understand table & tinker with console to know nomenclature and tags related to each object in the DOM
2. Find Wikipedia API that allows you to search for specific Wikipedia page on each VC firm

# # Step 1 : Get a comprehensive list of all VC firms

# # Step 2 : Check whether Wikipedia has a webpage for each firm through API

# # Step 2 : Get a summary from Wikipedia page of specific firm 

# # Step 3 : Combine both data sources horizontally so that each row has a column in which summary of company is introduced

# # Step 4 : Export as clean CSV file
---

## References
* [Requests Library Documentation: Quickstart](http://docs.python-requests.org/en/master/user/quickstart/)
* [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Stack Overflow Python Requests Questions](https://stackoverflow.com/questions/tagged/python-requests)
* [StackOverflow BeautifulSoup Questions](https://stackoverflow.com/questions/tagged/beautifulsoup)

### Deliverables

* **A Jupyter Notebook (.ipynb) file** that contains the code used to work with your API and scrape your web page.
* **An output folder** containing the outputs of your API and scraping efforts.
* **A ``README.md`` file** containing a detailed explanation of your approach and code for retrieving data from the API and scraping the web page as well as your results, obstacles encountered, and lessons learned.

