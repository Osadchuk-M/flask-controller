import os
import scriptine

from core.functions import make_dirs_from_dict


def create_project_command(project_name, path='./'):
    """
    Create flask project tree.
    
    :param project_name: project name
    """
    from core.trees import PROJECT_TREE
    project_tree = {}
    project_tree[project_name] = PROJECT_TREE.pop('project_name')
    make_dirs_from_dict(project_tree, path)
    
def create_app_command(app_name, path='./'):
    """
    Create flask app tree.

    :param app_name: application name
    :param path: path/to/your/app
    """
    from core.trees import APP_TREE
    app_tree = {}
    app_tree[app_name] = APP_TREE.pop('app_name')
    make_dirs_from_dict(app_tree, path)

def create_tests_command(modules, path='./'):
    """
    Create tests
    
    :param modules: list of modules, to be created
    """
    from core.trees import TESTS_TREE
    tests_tree = TESTS_TREE
    for module in modules.split(','):
        tests_tree['tests']['files'].append('test_'+module+'.py')
    make_dirs_from_dict(tests_tree, path)
    

if __name__ == '__main__':
    scriptine.run()
