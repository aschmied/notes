import multiprocessing
import os
import signal
import sys
import time

def main():
    stop = multiprocessing.Value('b', False, lock=False)

    processes = []
    for process_id in range(5):
        processes.append(multiprocessing.Process(target=run, args=(process_id, stop)))

    for process in processes:
        process.start()

    while not stop:
        if not are_processes_alive(processes):
            stop.value = True
            time.sleep(1)
            kill_all(processes)

    for process in processes:
        process.join()

    print('Exiting main')

def run(id, stop):
    print('Starting process {}'.format(id))

    if id == 3:
        while True:
            time.sleep(1.0)

    if id == 4:
        raise ValueError('{}'.format(id))

    while not stop.value:
        time.sleep(1.0)
    
    print('Exiting process {}'.format(id))

def are_processes_alive(processes):
    return all(map(is_process_alive, processes))

def is_process_alive(process):
    is_alive = process.is_alive()
    if not is_alive:
        print('Child {} pid {} has exited with code {}'.format(process, process.pid, process.exitcode))
    return is_alive

def kill_all(processes):
    return all(map(kill, processes))

def kill(process):
    os.kill(process.pid, signal.SIGTERM)


if __name__ == '__main__':
    main()
