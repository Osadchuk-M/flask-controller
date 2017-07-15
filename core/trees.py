PROJECT_TREE = {
    'project_name': {
        'app': {
            'main': {
                'files': ['__init__.py', 'errors.py', 'forms.py', 'views.py']
            },
            'static': {
                'dirs': ['css', 'fonts', 'js']
            },
            'templates': {
                'files': ['index.html']
            },
            'files': ['__init__.py', 'decorators.py', 'email.py', 'exceptions.py', 'models.py']
        },
        'tests': {
            'files': ['__init__.py']
        },
        'files': ['config.py', 'manage.py', 'README.md']
    }
}

APP_TREE = {
    'app_name': {
        'files': ['__init__.py', 'views.py', 'forms.py', 'errors.py']
    }
}

TESTS_TREE = {
    'tests': {
        'files': ['__init__.py']
    }
}
