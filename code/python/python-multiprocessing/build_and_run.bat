call docker build . -t nanometrics/python-multiprocessing:latest
call docker run --detach --rm --name python-multiprocessing nanometrics/python-multiprocessing:latest
