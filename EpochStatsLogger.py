import sys
import csv
import os
import time
from keras import backend as K


class EpochStatsLogger(Callback):

    def on_train_begin(logs={}):
        filename = os.path.basename(sys.argv[0])[:-3]
        backend = K.backend()
        f = open('logs/{}_{}.csv'.format(filename, backend), 'w')
        log_writer = csv.writer(f)
        log_writer.writerow(['epoch', 'elapsed', 'loss',
                             'acc', 'val_loss', 'val_acc'])

    def on_train_end(logs={}):
        f.close()

    def on_epoch_begin(self, epoch, logs={}):
        start_time = time.time()

    def on_epoch_end(self, epoch, logs={}):
        log_writer.writerow([epoch, round(time.time() - start_time, 4),
                             logs.get('loss'),
                             logs.get('acc'),
                             logs.get('val_loss'),
                             logs.get('val_acc')])
