# flask-controller

Use this in your command line.

    $ python flask-controller.py --help
    
    Usage: flask-controller.py command [options]

    Options:
      -h, --help  show this help message and exit

    Commands:
      create-project  Create flask project tree.
      create-tests    Create tests.
      create-app      Create flask app tree.

## Example


### Create project:

> $ python flask-controller.py create-project <your_project_name>

    $ python flask-controller.py create-project MyProject

take a look at project structure:
    
    $ tree MyProject
    MyProject/
    ├── app
    │   ├── decorators.py
    │   ├── email.py
    │   ├── exceptions.py
    │   ├── __init__.py
    │   ├── main
    │   │   ├── errors.py
    │   │   ├── forms.py
    │   │   ├── __init__.py
    │   │   └── views.py
    │   ├── models.py
    │   ├── static
    │   │   ├── css
    │   │   ├── fonts
    │   │   └── js
    │   └── templates
    │       └── index.html
    ├── config.py
    ├── manage.py
    ├── README.md
    └── tests
        └── __init__.py

### Create application:

> $ python flask-controller.py create-app <your_app_name>

    $ python flask-controller.py create-app application
    
take a look at application structure:

    $ tree application
    application/
    ├── errors.py
    ├── forms.py
    ├── __init__.py
    └── views.py
    
### Create tests:

> $ python flask-controller.py create-tests <comma,separated,modules>

    $ python flask-controller.py create-tests api,basics,models,selenium
    
take a look at tests structure

    $ tree tests
    tests/
    ├── __init__.py
    ├── test_api.py
    ├── test_basics.py
    ├── test_models.py
    └── test_selenium.py
