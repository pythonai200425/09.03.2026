import threading
import time

def count_numbers(n: int) -> None:
    total = 0
    for i in range(n):
        total += i


def main() -> None:
    start = time.time()

    t1 = threading.Thread(target=count_numbers, args=(50_000_000,))
    t2 = threading.Thread(target=count_numbers, args=(50_000_000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    #count_numbers(100_000_000)

    end = time.time()
    print(f"Total time with threads: {end - start:.2f} seconds")


if __name__ == "__main__":
    main()