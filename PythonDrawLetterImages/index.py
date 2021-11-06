import os

os.chdir('Fonts')

i = 0

for f in os.listdir():

    i = i + 1
    file_name, file_ext = os.path.splitext(f)
    
    new_name = '{}-{}{}'.format(i, file_name, file_ext)

    print(new_name)