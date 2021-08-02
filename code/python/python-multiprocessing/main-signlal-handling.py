import multiprocessing
import signal
import sys
import time

def main():
    signal.signal(signal.SIGTERM, lambda signum, frame: signal_handler('main', signum, frame))
    
    processes = []
    for process_id in range(5):
        processes.append(multiprocessing.Process(target=run, args=(process_id,)))

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print('Exiting main')

def run(id):
    print('Starting process {}'.format(id))
    signal.signal(signal.SIGTERM, lambda signum, frame: signal_handler(id, signum, frame))
    while True:
        time.sleep(1)
    print('Exiting process {}'.format(id))

def signal_handler(process, signum, frame):
    print('sig_handler called in {} for signal number {}'.format(process, signum))
    sys.exit()

if __name__ == '__main__':
    main()
