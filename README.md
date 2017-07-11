# flask-controller
___
Use this in your command line.

    % python flask-controller.py --help
    
    Usage: flask-controller.py command [options]

    Options:
      -h, --help  show this help message and exit

    Commands:
      create-project  Create flask project tree.

## Example
___

### Create project:

> % python flask-controller.py create-project <your_project_name>

    python flask-controller.py create-project MyProject
    Done!

take a look a project structure:
    
    % tree MyProject
    MyProject/
    ├── app
    │   ├── auth
    │   ├── main
    │   ├── static
    │   │   ├── css
    │   │   ├── fonts
    │   │   └── js
    │   └── templates
    └── tests
