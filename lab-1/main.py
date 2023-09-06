from reader import load_logs_from_file

if __name__ == '__main__':
    data = load_logs_from_file("../data/access.log")
    print(data[0][0])
