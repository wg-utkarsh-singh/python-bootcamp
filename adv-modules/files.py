import os
import queue


def rec_print_files(dir_name):
    dirs = queue.Queue()
    dirs.put(dir_name)
    while dirs.qsize():
        dir_name = dirs.get()
        with os.scandir(dir_name) as entries:
            print(f"{dir_name}: ")
            for entry in entries:
                if entry.is_file():
                    print(f"\t{entry.name}")
                elif entry.is_dir():
                    dirs.put(os.path.join(dir_name, entry.name))


if __name__ == "__main__":
    rec_print_files(
        "C:\\Users\\usingh\\OneDrive - WatchGuard Technologies Inc\\Documents\python-bootcamp"
    )
