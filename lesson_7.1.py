import os
import shutil

dir_name_root = os.path.join('my_project')
dirs = ['settings', 'mainapp', 'adminapp', 'authapp']
#my_project
if not os.path.exists(dir_name_root):
    os.mkdir(dir_name_root)

os.chdir(dir_name_root)

#settings, mainapp, adminapp, authapp
for dir in dirs:
    if not os.path.exists(dir):
        os.mkdir(dir)

print(os.listdir())
