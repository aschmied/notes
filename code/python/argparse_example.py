import argparse
from datetime import datetime
from datetime import timezone
import sys

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'

def _datetime_arg(string):
    try:
        return datetime.strptime(string,
            DATETIME_FORMAT).replace(tzinfo=timezone.utc)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f'Expected datetime in "{DATETIME_FORMAT}"')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=sys.argv[0], description='Example argparse usage')
    # parser.add_argument('--dry-run', default=False, action='store_true',
    #     help='Logs what the script would do but does not modify data')
    # parser.add_argument('url', metavar='URL', type=str,
    #                 help='URL to POST to')
    # parser.add_argument('--timeout-seconds', type=float, default=1.0,
    #                 help='Timeout in seconds')
    # parser.add_argument('--input-path', type=str, required=True
    #                 help='Location of input file')
    parser.add_argument('--urls', type=str, nargs='+',
        help='Space-delimited list of URLs to process')
    parser.add_argument('filename', type=str, help='Output filename')

    # parser.add_argument('--start-datetime', type=_datetime_arg,
    #                     required=False, metavar=DATETIME_FORMAT,
    #                     help='Preferred origin start time. In UTC')

    args = parser.parse_args(sys.argv[1:])
    print(args.urls)
    print(args.filename)
