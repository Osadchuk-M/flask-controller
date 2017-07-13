import os
import scriptine

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

def make_files_from_list(files, current_dir='./'):
	for f in files:
		open(os.path.join(current_dir, f), 'a').close()

def make_dirs_from_list(dirs, current_dir='./'):
	for d in dirs:
		os.mkdir(os.path.join(current_dir, d))

def make_dirs_from_dict(d, current_dir='./'):
    for key, val in d.items():
    	if key == 'files':
    		make_files_from_list(val, current_dir)
    	elif key == 'dirs':
    		make_dirs_from_list(val, current_dir)
    	else:
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

