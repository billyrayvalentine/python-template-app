# A template for a python3 app with logging, config and some commandline args
# Requires Python >= 3.6

import sys
import configparser
import os
import logging
import argparse
import time

# Globals
CONFIG_FILE = '/etc/template-app.conf'

# Setup command line args
parser = argparse.ArgumentParser(description='template-app')
parser.add_argument('-d', '--debug', \
    choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'], \
    help='debug level', default='INFO')

args = parser.parse_args()

# Load config file
config = configparser.ConfigParser()
files = config.read(CONFIG_FILE)

# Exit 1 if config file cant be loaded
if len(files) == 0:
    print(f'Fatal - Could not load {CONFIG_FILE}')
    sys.exit(1)

# Load format, dateformat and log filename from config file
try:
    log_file = config.get('main', 'log_file')
except configparser.NoOptionError as e:
    print(f'Fatal - could not load log_file value from {CONFIG_FILE}')
    sys.exit(1)

# Set up logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', \
    datefmt='%Y/%m/%d %H:%M:%S', filename=log_file, level=args.debug)

logging.debug(f'Loaded log_file value {log_file} from {CONFIG_FILE}')
logging.info('Starting app')

# MAIN APP STARTS HERE
n = 1
while True:
    print(f'Hello {n}')
    logging.debug(f'Printed {n}')
    n += 1
    time.sleep(1)
