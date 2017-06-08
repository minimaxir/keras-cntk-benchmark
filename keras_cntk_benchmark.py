import os
import subprocess

if not os.path.exists('logs'):
    os.makedirs('logs')

test_files = [f for f in os.listdir("test_files") if f.endswith('.py')]
test_files.remove('CustomCallback.py')
backends = ['cntk', 'tensorflow']
docker_cmd = "docker run -it --rm -v $(pwd)/:/keras --name keras".split(" ")

for test_file in test_files:
    for backend in backends:
        statement = docker_cmd + ["-e", "KERAS_BACKEND='{}'".format(backend), "keras-cntk-cpu",
                                  "python3", "test_files/" + test_file]

        print(" ".join(statement))
        print("{} + {}".format(test_file, backend))

        os.system(" ".join(statement))
