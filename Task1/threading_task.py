import threading

from consts import MAX_NUMBER, NUM_THREADS
from utils import timer_decorator, get_end_index


def calculate_sum(start, end, result, index):
    total = 0
    for i in range(start, end):
        total += i
    result[index] = total

def main():
    threads = []
    result = [0] * NUM_THREADS
    chunk_size = MAX_NUMBER // NUM_THREADS

    @timer_decorator("threading")
    def exec():
        for i in range(NUM_THREADS):
            start = i * chunk_size + 1
            end = get_end_index(i, chunk_size, NUM_THREADS)

            thread = threading.Thread(target=calculate_sum, args=(start, end, result, i))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        return sum(result)

    exec()

if __name__ == "__main__":
    main()
