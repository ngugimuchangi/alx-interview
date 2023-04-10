#!/usr/bin/python3
'''Log module that parses logs, computes stats and prints them'''


import sys
# from typing import Dict, Tuple


def log_parser(log):
    """
    Parses log into different fields
    """
    log = log.replace('"', '').replace('-', '')
    log_fields = log.split()
    file_size = int(log_fields[-1])
    status_code = log_fields[-2]
    return status_code, file_size


def validate_format(log):
    """
    Validates log format
    """
    return True if len(log.split()) == 9 else False


def print_log(file_size, status_codes) -> None:
    """
    Prints out log files
    """
    sorted_status_codes = dict(list(sorted(status_codes.items())))
    print('File size: {}'.format(file_size))
    for key, value in sorted_status_codes.items():
        print("{}: {}".format(key, value))


def main():
    """
    Reads logs from std in and prints out statistic
    on status code and file size
    """
    status_codes_count = {}
    total_size = 0
    log_count = 0
    try:
        for log in sys.stdin:
            log_count += 1
            if not validate_format(log):
                continue
            status_code, file_size = log_parser(log)
            total_size += file_size
            entry = {status_code: status_codes_count.get(status_code, 0) + 1}
            status_codes_count.update(entry)
            if not log_count % 10:
                print_log(file_size, status_codes_count)
    except KeyboardInterrupt:
        print_log(file_size, status_codes_count)


if __name__ == '__main__':
    main()
