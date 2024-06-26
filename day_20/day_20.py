###Python PIP - Python Package Manager###
# What is PIP?
# PIP stands for Preferred installer program. We use pip to install different Python packages. Package is a Python module that can contain one or more modules or other packages.

# Installing PIP
# asabeneh@Asabeneh:~$ pip install pip

# Checking the version of pip
# pip --version

# Installing a package using pip
# asabeneh@Asabeneh:~$ pip install numpy
# asabeneh@Asabeneh:~$ pip install numpy

# Uninstalling a package using pip
# asabeneh@Asabeneh:~$ pip install numpy

# Listing all installed packages
# pip list

# Showing information about a package
# pip show packagename --verbose

# PIP freeze (Generate installed Python packages with their version and the output is suitable to use it in a requirements file.)
# pip freeze > requirements.txt

# Reading from URL (requests - it allows to open a network connection and to implement CRUD(create, read, update and delete) operations.)
#pip install requests

import requests # importing the request module

url = 'https://randomuser.me/api/' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page
print(response.json()) # gives the json data from the page

# Creating a Package
from mypackage import arithmetics, greet
print(arithmetics.add_numbers(1, 2, 3, 5))
print(arithmetics.subtract(5, 3))
print(arithmetics.multiple(5, 3))
print(arithmetics.division(5, 3))
print(arithmetics.remainder(5, 3))
print(arithmetics.power(5, 3))
print(greet.greet_person('Rasyid', 'Annas'))

# Further Information About Packages
# Database
# SQLAlchemy or SQLObject - Object oriented access to several different database systems
# pip install SQLAlchemy

# Web Development
# Django - High-level web framework.
# pip install django
# Flask - micro framework for Python based on Werkzeug, Jinja 2. (It's BSD licensed)
# pip install flask

# HTML Parser
# Beautiful Soup - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.
# pip install beautifulsoup4
# PyQuery - implements jQuery in Python; faster than BeautifulSoup, apparently.

# XML Processing
# ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. --Note: Python 2.5 and up has ElementTree in the Standard Library

# GUI
# PyQt - Bindings for the cross-platform Qt framework.
# TkInter - The traditional Python user interface toolkit.

# Data Analysis, Data Science and Machine learning
# Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.
# Pandas: is a data analysis, data science and a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis.
# SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
# Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
# TensorFlow: is a machine learning library built by Google.
# Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.

# Network:
# requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)
# pip install requests