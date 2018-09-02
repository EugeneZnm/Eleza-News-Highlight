# Eleza-News-Highlight

## Built by [EUGENE NZIOKI](https://github.com/EugeneZnm)

## Description

A news aggregator showing news articles from various publishers; with users being able to select a publisher, view articles from them along with their image, description and time of creation.

## User Requirements

 1. Your users should be able to see various news sources and select the ones they prefer
 2. Your users should be able to see all the news articles from that news source
 3. The user should see the image description and time the news article was created.
 4. The user should also be able to click on an article and read it fully from the news source.

## Features

 -[x] List multiple news sources
 -[ ] Listing of articles from the selected news source
 -[x] Categorisation of news networks
 -[ ] Using flask sessions to save users article snippet
 -[ ] Using of browser cookies to store favourite news sources
 -[ ] Redirection of user to articles  

## Installation

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.

* Tested on Debian Linux
* Python 3.6.4

## Cloning of the respository
   * In terminal:
   
    $ git clone https://github.com/EugeneZnm/Eleza-News-Highlight
    
## Creating the Virtual Environment

    sudo apt-get install python3.6-venv
    python3.6 -m venv virtual
    source virtual/bin/activate

## Install Dependencies

    pip3 install -r requirements
    
## Required Libraries     
   * Flask==0.12.2
   * Flask-Bootstrap==3.3.7.1
   * Flask-Script==2.0.6
   * gunicorn==19.7.1
   
## Running Tests

    python3 manage.py test
    
## Running the web app 
    python3 manage.py server
   
   open app in browser by default on 127.0.0.1:5000

## Live Demo

This web app can be accessed from the following link:

    https://....   
    
## Quick Start

    usage: manage.py [-?] {server,test,shell,runserver} ...

    positional arguments:
      {server,test,shell,runserver}
        server              Runs the Flask development server i.e. app.run()
        test                Run the unit tests.
        shell               Runs a Python shell inside Flask application context.
        runserver           Runs the Flask development server i.e. app.run()
    
    optional arguments:
      -?, --help            show this help message and exit
      
## Technology Used

   * Python3.6
   * Flask   
   * Heroku
   
## License Information

   MIT License

Copyright(c) 2018

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.