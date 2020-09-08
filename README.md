# RealTimeTrainInfo

Small project to parse XML data from Irish Rail real time data (http://api.irishrail.ie/realtime/)

API calls, parsing and webserver hosting are all contained in app.py
  - requests library is used to fetch XML using above API
  - xml.etree.ElementTree used to parse XML as element tree
  - Flask hosts the webserver and pases train info to HTML using render template

Templates folder contains files to be rendered by flask
  - HTML served by flask
  - Jinja code used to dynamically render based on train data (https://jinja.palletsprojects.com/en/2.11.x/)

![List of incoming trains](images/screen1.png?raw=true)
 ( --- )
![No trains listed](images/screen2.png?raw=true)
