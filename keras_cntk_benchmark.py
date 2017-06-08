import os
import subprocess

if not os.path.exists('logs'):
    os.makedirs('logs')

test_files = os.listdir("test_files")
backends = ['cntk', 'tensorflow']

for test_file in test_files:
    for backend in backends:
        statement = ["keras-cntk", "-e", "KERAS_BACKEND='{}'".format(backend),
                     "python3", "test_files/" + test_file]

        # https://stackoverflow.com/a/13143013
        subprocess.Popen("exec " + " ".join(statement),
                         stdout=subprocess.PIPE, shell=True)
