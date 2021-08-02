import multiprocessing
import time

def main():
    shared_dict = multiprocessing.Manager().dict()
    shared_dict['blah'] = ['blerg']

    processes = []
    for process_id in range(2):
        processes.append(multiprocessing.Process(target=run, args=(process_id, shared_dict)))

    for process in processes:
        process.start()

    for process in processes:
        process.join()

def run(id, d):
    print('Starting process {}'.format(id))
    if id==0:
        e = d['blah'].copy()
        e[0] = 'foo'
        d['blah'] = e
    if id==1:
        time.sleep(2)
        print('blah[0] is {}'.format(d['blah'][0]))

if __name__ == '__main__':
    main()
