import multiprocessing

from consts import MAX_NUMBER, NUM_PROCESSES
from utils import timer_decorator, get_end_index


def calculate_sum(start, end, result_queue):
    total = 0
    for i in range(start, end):
        total += i
    result_queue.put(total)

def main():
    processes = []
    result_queue = multiprocessing.Queue()
    chunk_size = MAX_NUMBER // NUM_PROCESSES

    @timer_decorator("multiprocessing")
    def exec():
        for i in range(NUM_PROCESSES):
            start = i * chunk_size + 1
            end = get_end_index(i, chunk_size, NUM_PROCESSES)

            process = multiprocessing.Process(target=calculate_sum, args=(start, end, result_queue))
            processes.append(process)

        for process in processes:
            process.start()

        for process in processes:
            process.join()

        total_sum = 0
        while not result_queue.empty():
            total_sum += result_queue.get()
        return total_sum
    
    exec()

if __name__ == "__main__":
    main()
