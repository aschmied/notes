import sys
import threading
import time

def main(argv):
    thread_type = argv[1] if len(argv) > 1 else None
    if thread_type == 'daemon':
        start_thread(daemon=True)
    else:
        start_thread(daemon=False)
    print('Done main')

def start_thread(daemon):
    thread = threading.Thread(target=thread_target, daemon=daemon)
    thread.start()

def thread_target():
    sleep_time = 5
    print('Thread sleeping for {} seconds'.format(sleep_time))
    time.sleep(sleep_time)
    print('Exiting thread')

if __name__ == '__main__':
    main(sys.argv)
