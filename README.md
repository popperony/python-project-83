### Hexlet tests and linter status:
[![Actions Status](https://github.com/popperony/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/popperony/python-project-83/actions)
[![Python CI](https://github.com/popperony/python-project-83/actions/workflows/python_ci.yml/badge.svg)](https://github.com/popperony/python-project-83/actions/workflows/python_ci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/fd9c2413bc448990402f/maintainability)](https://codeclimate.com/github/popperony/python-project-83/maintainability)

### [Try the application](https://python-project-83-utn1.onrender.com/)

### Descriptions
This project implements an application based on the Flask framework. The app analyses the selected pages for SEO suitability

### Requirements
1. Python >=3.10
2. poetry >= 1.2.0
3. Flask >= 3.0.0
4. gunicorn >= 20.1.0


### To get started
1. Clone git repo:
  `git@github.com:popperony/python-project-83.git`
2. Go to directory page_analyzer:
  `cd page_analyzer`
3.  Configuring `poetry` to create a virtual environment:
  `poetry config virtualenvs.in-project true`
4.  Create virtual environment and Install dependencies
  `make install`
5. Start app 
  `make start`
