import multiprocessing
import sys
import time

def main():
    processes = []
    for process_id in range(5):
        processes.append(multiprocessing.Process(target=run, args=(process_id,)))

    for process in processes:
        process.start()

    print('Bailing out')
    for process in processes:
        process.kill()
    
    sys.exit(1)

def run(id):
    print('Starting process {}'.format(id))

    while True:
        time.sleep(1.0)
    
    print('Exiting process {}'.format(id))

if __name__ == '__main__':
    main()
