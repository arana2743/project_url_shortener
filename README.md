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

## Installation:
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

## API Usage:
- API Endpoints:
Once the installation is done successfully, app will be running on port `5000` and the url for local setup will look like : `localhost:5000` or `0.0.0.0:5000`.
- Below are relevant REST Endpoints available in the app:
```
localhost:5000/
localhost:5000/shorten_url
localhost:5000/stats
```

- Now to shorten the url - `/shorten_url`, which accepts the request in POST method along with original_url (which needs to be shortened) in json format as below:
```
{
    "original_url": "https://www.example.com"
}
```
 - Sample command to test (via curl command utility):
```sh
curl --location --request POST 'localhost:5000/shorten_url' \
--header 'Content-Type: application/json' \
--data-raw '{
    "original_url": "https://www.example.com"
}'
```
Sample Data returned from above command:

```sh
{
  "original_url": "https://www.slice.com",
  "short_url": "y5GNC"
}
```
Now to use the above short url, need to add the short_url string returned to our app's root url
```
"localhost:5000/" + "y5GNC" = "localhost:5000/y5GNC"
 i.e.  (root-url) + (shortened-url-string) = (shortened-url)
```