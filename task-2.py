# task2.py - Data manipulation and examples (>=50 lines)
class SimpleLogger:
    def __init__(self):
        self.logs = []

    def info(self, message):
        entry = f"INFO: {message}"
        self.logs.append(entry)
        print(entry)

    def warn(self, message):
        entry = f"WARN: {message}"
        self.logs.append(entry)
        print(entry)

    def error(self, message):
        entry = f"ERROR: {message}"
        self.logs.append(entry)
        print(entry)

def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

def unique_preserve_order(seq):
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def chunk_list(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i+size]

def main():
    logger = SimpleLogger()
    logger.info("Starting task2 main")
    nested = [1, [2, 3], [4, [5, 6]], 7]
    print("Flattened:", flatten_list(nested))
    print("Unique:", unique_preserve_order([1,2,2,3,1,4,3]))
    for chunk in chunk_list(list(range(12)), 5):
        print("Chunk:", chunk)
    logger.info("Finished task2 main")

if __name__ == "__main__":
    main()
