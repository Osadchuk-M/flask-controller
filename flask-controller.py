import os
import scriptine

PROJECT_TREE = {
    'project_name': {
        'app': {
            'auth': None,
            'main': None,
            'static': {
                'css': None,
                'fonts': None,
                'js': None
            },
            'templates': None
        },
        'tests': None
    }
}

def make_dirs_from_dict(d, current_dir='./'):
    for key, val in d.items():
        os.mkdir(os.path.join(current_dir, key))
        if type(val) == dict:
            make_dirs_from_dict(val, os.path.join(current_dir, key))

def create_project_command(name):
    """
    Create flask project tree.
    
    :param name: project name
    """
    project_tree = {}
    project_tree[name] = PROJECT_TREE.pop('project_name')
    make_dirs_from_dict(project_tree)
    

if __name__ == '__main__':
    scriptine.run()
