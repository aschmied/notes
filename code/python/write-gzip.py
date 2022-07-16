import gzip

with gzip.open('out.txt.gz', 'wt') as f:
    f.write('blah blah\n')
