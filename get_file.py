import os 
import shutil
import sys
import pandas
import glob

if len(sys.argv) < 2:
    raise RuntimeError()

files_mp3 = glob.glob(os.path.join(os.getcwd(), "data/vn/*.mp3"))


for file_mp3 in files_mp3:
    if os.path.exists(file_mp3):
        os.remove(file_mp3)


path = sys.argv[1] 

df = pandas.read_table(os.path.join(os.getcwd(), 'data/vn/tests.tsv'))

for path_audio in df['path']:
    shutil.copyfile(os.path.join(path, path_audio), os.path.join(os.getcwd(), f'data/vn/%s'%path_audio))