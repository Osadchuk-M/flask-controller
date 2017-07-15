import os

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
