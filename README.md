# Fampay-backend-assignment
An API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Language / Frameworks involved
* __Languages__
  - Python
* __Tech Stack__
  - Django
  - DRF (REST APIs)
  - Celery
  - Redis
* __Database__
  - __Development__: SQLite
# Basic Requirements:

- [X] Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- [X] A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- [X] A basic search API to search the stored videos using their title and description.
- [X] Dockerize the project.
- [X] It should be scalable and optimised.

# Bonus Points:

- [ ] Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- [X] Make a dashboard to view the stored videos with filters and sorting options (optional)
- [X] Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.
    - Ex 1: A video with title *`How to make tea?`* should match for the search query `tea how`

## Basic Setup

1. - [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) will be required for the development environment.
   - Make sure that you install both of them specific to your OS and version (Linux, Windows, Mac)
2. Clone or Download the repository:

  ```shell
  git clone https://github.com/partha2000/Fampay-backend-assignment.git
  ```

## Build Instructions
1. `cd Fampay-backend-assignment`
2. Build the docker image
   - `docker-compose build`
   - It might take a while to for the initial build
3. Run docker 
    - `docker-compose up` --> To start the containers
    -  `docker-compose up --remove-orphans`  --> To kill any stray containers
4. Setup the virtual environment for development. Refer to the *Setting up the environment*
## Setting up the virtual environment
_Always make sure you have python 3 and are using virtualenv to install and manage your packages. Django would not work with python 2.x versions._

__Run these commands inside the root directory of the project__
1. `pip3 install virtualenv`		-> Install the virtualenv library
2. `virtualenv -p python3 .venv`	-> Create a virtual environment
3. `source .venv/bin/activate`		-> Get inside the virtual environment
4. `pip install --upgrade pip`		-> get upgraded to pip3
5. `pip install -r requirements.txt`-> Thereafter install all the packages as per the reqirements.txt
   
_Running migrations is not required as it has alredy been added to `docker-compose.yml`. In case there is any issue due to migrations 
   not being applied you can always run `python mange.py makemigrations` followed by `python manage.py migrate` inside the 
   virtual environment._

## API Endpoints
- `localhost:8000/`
  -  GET request to this endpoint returns the stored video data in a paginated response sorted in descending order of published datetime
- `localhost:8000/searchVideo/`
  - GET request with proper query parameters(ordering & search) will search the stored videos using their title and description along with option for ordering.
  - Eg. `http://127.0.0.1:8000/searchVideo/?ordering=-pub_date_time&search=live` will fetch all video details having "live" in their title or description in descending order of published date and time.

You can use the web browsable API of the server or [Postman](https://www.postman.com/) to test the API.

## Possible issues
In case of any issue run these commands:
- `docker system prune` 
  - If you get the error message `docker-compose INTERNAL ERROR: cannot create temporary directory`