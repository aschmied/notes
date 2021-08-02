docker build . -t test-zombie:latest

docker run --rm ^
    --init ^
    -it ^
    --detach ^
    --name test-zombie ^
    -v D:\google_drive\work\docker\zombie-reaping:/host ^
    test-zombie:latest
