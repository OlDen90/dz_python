import os

ROOT = os.path.dirname(__file__)
dir_root = 'my_project'
dir_1 = os.path.join('settings')
dir_2 = os.path.join('mainapp')
dir_3 = os.path.join('adminapp')
dir_4 = os.path.join('authapp')
# dir_ = [os.path.join(dir_1), os.path.join(dir_2),
#         os.path.join(dir_3), os.path.join(dir_4)]

dir_path = os.path.join(dir_root, dir_1)

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

dir_path = os.path.join(dir_root, dir_2)

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

dir_path = os.path.join(dir_root, dir_3)

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

dir_path = os.path.join(dir_root, dir_4)

if not os.path.exists(dir_path):
    os.makedirs(dir_path)
