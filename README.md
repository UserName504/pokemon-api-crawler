# pokemon-api-crawler

A web API displaying data from [PokeAPI](https://pokeapi.co/). Made using the [Django REST framework](https://www.django-rest-framework.org/).

The following tutorial was used as a basis point: https://docs.docker.com/samples/django/

The `.gitignore` file ws inspired by: https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/

## Setup

Be sure to use a virtual environment:
> ```sh
> $ python3 -m venv venv
> ```

To activate the virtual environment:
> ```sh
> $ source venv/bin/activate
> ```

Upon activation, run `pip list`. Only `pip` and `setuptools` should be installed in the virtual environment.

Once the venv has been activated, install requirements:
> ```sh
> $ pip install -r requirements.txt
> ```

To run:
> ```sh
> $ docker-compose up
> ```

View the server via the following:
`localhost:8000`
