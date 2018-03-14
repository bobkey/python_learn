import os
  
def get_file_names(path_name):
    print path_name
    file_names = os.listdir(path_name)
    for name in file_names:
        if os.path.isdir(name):
            get_file_names(os.path.abspath(name))
        else:
            print name
  
get_file_names(os.getcwd())