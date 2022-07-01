# Project - URL Shortener API
***
## Title: 
URL Shortener

## Description : 
A REST api based URL shortener service built in Python programming language.

### Frameworks/components used:
1. Flask
2. SQLAlchemy

### Requirements(Softwares to be installed):
1. Docker (must)
2. Python3.8+ (not necessarily if Docker is installed)

## Installation & Usage:
### 1. With Docker
#### 1.1. Download project for git (currently points to dev branch)
```sh
git clone https://github.com/arana2743/project_url_shortener/tree/dev
```
#### 1.2. Go to the downloaded project folder 
```sh
cd project_url_shortener
```
#### 1.3. Launch application with Docker command
```sh
docker-compose up
```
**Note:** `Docker should be running for above to work`.
### 2. Without Docker (first two steps remains the same)
**Note:** For this to work `Python` must be installed (preferably version 3.7 or above)
#### 1.1. Download project for git (currently points to dev branch)
```sh
git clone https://github.com/arana2743/project_url_shortener/tree/dev
```
#### 1.2. Go to the downloaded project folder 
```sh
cd project_url_shortener
```
#### 1.3. Setup of virtual environment for Python and Install all required dependencies (from `requirements.txt` file provided in the project )
```sh
python -m venv env
pip install -r requirements.txt
```
#### 1.4. Setup is done, now launch the app locally
```sh
python app.py
```