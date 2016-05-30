import tempfile, subprocess, glob

temp_dir = tempfile.mkdtemp()
path = 'https://github.com/sgmap/openfisca-paris.git'
return_code = subprocess.call('git clone ' + path + ' ' + temp_dir + ' &> /dev/null', shell = True)
print("Return code:")
print(return_code)
content_folder = glob.glob(temp_dir + '/*.*')
print("Content of the folder:")
print(content_folder)
assert len(content_folder) > 0
