import time

from TH_help.sometest import make_async


@make_async
def create_file(que):
    lines = 'empty'
    with open('thistext.txt', 'rb') as file:
        lines = file.readlines()
        time.sleep(4)
        # que.put(str(lines))
    return lines


if __name__ == '__main__':
    thr_ret = create_file()

    inp = input('please enter your name\n')
    print(inp)
    print('inside main')
    print(thr_ret)
