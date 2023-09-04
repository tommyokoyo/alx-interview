import datetime
import random

def output_line():
    return("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
            random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
            datetime.datetime.now(),
            random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
            random.randint(1, 1024)))

def word_split(word):
    return word.split(' ')


if __name__ == '__main__':
    my_split_var = word_split(output_line())
    print(my_split_var)
    print(f"len: {len(my_split_var)}")
    print(f" file size: {my_split_var[8]} [8]")
    print(f"Status code: {my_split_var[7]} [7]")
