#!/usr/bin/python3
"""
    script that reads stdin line by line and computes metrics
"""
import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
my_cache = []


def interrupt_handler():
    print_metrics(my_cache[0], my_cache[1])
    sys.exit(0)


def print_metrics(total_file_size, status_code_counts):
    if total_file_size and status_code_counts:
        if my_cache:
            my_cache[0] = total_file_size
            my_cache[1] = status_code_counts
            print(f"Total file size: {total_file_size}")
            sorted_codes = sorted(status_code_counts.keys())
            for code in sorted_codes:
                print(f'{code}: {status_code_count[code]}')
        else:
            my_cache.append(total_file_size)
            my_cache.append(status_code_counts)
            print(f"Total file size: {total_file_size}")
            sorted_codes = sorted(status_code_counts.keys())
            for code in sorted_codes:
                print(f'{code}: {status_code_count[code]}')
    else:
        pass


def parse_input(line):
    total_file_size = 0
    line_count = 0
    if line:
        std_inputs = line.split()

        if len(std_inputs) >= 9 and std_inputs[8].isdigit():
            status_code = std_inputs[7]
            file_size = std_inputs[8]

            total_file_size += int(file_size)
            line_count += 1

            if status_code.isdigit():
                status_code = int(status_code)
                if status_code in status_codes:
                    status_code_count[status_code] += 1
                    return total_file_size, status_code_count
                else:
                    return


if __name__ == '__main__':
    count = 1
    my_list = []
    try:
        for values in sys.stdin:
            value_1, value_2 = parse_input(values)
            if count % 10 == 0:
                print_metrics(value_1, value_2)
            else:
                count += 1
    except KeyboardInterrupt:
        raise
