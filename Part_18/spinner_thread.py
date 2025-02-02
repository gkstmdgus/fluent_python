import threading
import itertools
import time
import sys

class Signal:
    go = True

def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(1)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status))

def slow_function(wait_time=3):
    time.sleep(wait_time)
    return 42

def supervisor():
    signal = Signal()
    spinner = threading.Thread(
        target=spin,
        args=('Thinking!', signal)
    )
    print('spinner oject: ', spinner)
    spinner.start()
    result = slow_function(5)
    signal.go = False
    spinner.join()
    return result

def main():
    result = supervisor()
    print('Answer: ', result)

if __name__ == "__main__":
    main()