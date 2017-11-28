import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("backend", nargs="?", type=str, default='all')
args = parser.parse_args()

if not os.path.exists('logs'):
    os.makedirs('logs')

test_files = [f for f in os.listdir("test_files") if f.endswith('.py')]
test_files.remove('CustomCallback.py')
backends = ['cntk', 'tensorflow'] if args.backend == 'all' else ['tensorflow']
docker_cmd = "sudo nvidia-docker run -it --rm -v $(pwd)/:/keras --name keras"

for test_file in test_files:
    for backend in backends:
        statement = docker_cmd + \
            " -e KERAS_BACKEND='{}' minimaxir/keras-cntk python3 test_files/{}".format(
                backend, test_file)

        print(statement)
        print("{} + {}".format(test_file, backend))

        os.system(statement)
