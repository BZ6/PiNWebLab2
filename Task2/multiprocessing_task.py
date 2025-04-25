import multiprocessing
import time

from connection import init_db
from urls import urls
from parse_and_save import parse_and_save


def main():
    init_db()
    
    processes = []
    start_time = time.time()

    for url in urls:
        process = multiprocessing.Process(target=parse_and_save, args=(url,))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    print(f"Multiprocessing execution time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
