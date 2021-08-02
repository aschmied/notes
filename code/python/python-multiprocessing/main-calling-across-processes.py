import multiprocessing
import os
import signal
import sys
import time

class Runnable:
    def __init__(self):
        self._stop = False

    def stop(self):
        self._stop = True

    def run(self):
        print('Starting')
        i = 0
        while not self._stop:
            print('Running')
            time.sleep(1)
            if i > 10:
                print('Quitting after 10 seconds')
                self._stop = True
            i += 1
        print('Exiting')


def main():
    runnable = Runnable()
    process = multiprocessing.Process(target=runnable.run, args=())
    process.start()
    # runnable.stop()
    process.join()
    print('stop switch is {}'.format(runnable._stop))


if __name__ == '__main__':
    main()
