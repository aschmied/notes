# Use Python 3+ and AWS CLI from this branch:
#   https://github.com/aschmied/aws-cli/tree/hotfix/4778-force-ascii-in-json-formatter
# cd to the repo root and `python setup.py install`
# This works around https://github.com/aws/aws-cli/issues/4778

# If you see this error:
#
#  'charmap' codec can't encode character '\u2713' in position 6: character maps to <undefined>
#
# then follow the steps here to enable UTF-8 in Windows consoles
#
#   https://stackoverflow.com/a/57134096/2833126
#
# and upgrade to a Python3 AWSCLI if you use the MSI installer:
#
#  https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html#python3-msis

LOG_STREAM_NAME = 'kubernetes.var.log.containers.<stuff>.log'
START_TIME = '2021-03-07 14:20:00'
END_TIME = '2021-03-07 16:40:00'

from datetime import datetime
import io
import json
import subprocess
import sys

def main():
    forward_token = None
    iteration = 0
    events = ['']
    total_events_count = 0
    while len(events) > 0:
        print('Fetching batch number {}'.format(iteration + 1))
        content = read_logs(forward_token)
        events, forward_token = parse_logs(content)
        with open('log.txt', 'a') as f:
            write_events_to_file(f, events)
        total_events_count += len(events)
        print('Wrote {} events this iteration, {} total'.format(len(events), total_events_count))
        
        iteration += 1

def read_logs(forward_token):
    command = [
        'aws',
        'logs',
        'get-log-events',
        '--profile=nmx-prod',
        '--region=us-east-1',
         # ASCII-JSON is added in the aws-cli fork mentioned in the comment header. It
         # is required on Windows to work around "'charmap' codec can't encode character"
         # errors on output redirection.
        #'--output=ascii-json',
        '--output=json',
        '--log-group-name=kubernetes',
        '--log-stream-name={}'.format(LOG_STREAM_NAME),
        '--start-time={}'.format(datetime_to_milliseconds_since_epoch(parse_datetime_string(START_TIME))),
        '--end-time={}'.format(datetime_to_milliseconds_since_epoch(parse_datetime_string(END_TIME))),
        '--start-from-head'
    ]
    if forward_token:
        command.append('--next-token={}'.format(forward_token))

    return execute_command(command)

def parse_datetime_string(string):
    return datetime.strptime(string, '%Y-%m-%d %H:%M:%S').replace(tzinfo=None)

def datetime_to_milliseconds_since_epoch(dt):
    epoch = datetime.utcfromtimestamp(0)
    seconds_since_epoch = (dt - epoch).total_seconds()
    return 1000 * int(seconds_since_epoch)

def execute_command(command):
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    stdout, stderr = popen.communicate()
    if stderr or popen.returncode != 0:
        print(stderr)
        print('Command failed with return code {}. Aborting: {}'.format(popen.returncode, " ".join(command)))
        sys.exit(1)
    return stdout

def parse_logs(content):
    parsed = json.loads(content)
    forward_token = parsed.get('nextForwardToken')
    events = parsed.get('events')
    return events, forward_token

def write_events_to_file(file, events):
    if not events:
        return

    for event in events:
        line = process_event(event)
        file.write('{}\n'.format(line))

def process_event(event):
    # timestamp = extract_timestamp(event)
    # time = datetime.datetime.utcfromtimestamp(timestamp)
    message = extract_message(event)
    return message

# def extract_timestamp(event):
#     return float(event['timestamp']) / 1000.0

def extract_message(event):
    message = json.loads(event['message'])
    return message['log'].strip()

if __name__ == '__main__':
    main()
