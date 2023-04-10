#!/usr/bin/python3
"""
Log stats module
"""
import sys


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
    status_codes_count = {"200": 0, "301": 0, "400": 0, "401": 0,
                          "403": 0, "405": 0, "500": 0}
    total_size = 0
    log_count = 0
    try:
        for log in sys.stdin:
            log_count += 1
            if not validate_format(log):
                continue
            status_code, file_size = log_parser(log)
            total_size += file_size
            if status_code in status_codes_count.keys():
                status_codes_count[status_code] += 1
            if not log_count % 10:
                print_log(file_size, status_codes_count)
    except KeyboardInterrupt:
        print_log(file_size, status_codes_count)


if __name__ == '__main__':
    main()
