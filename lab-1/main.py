from typing import Tuple, List

from mapper import map_logs_to_dataframe
from reader import load_logs_from_file
import LogDTO

if __name__ == '__main__':
    data: Tuple[List[LogDTO], int] = load_logs_from_file("../data/access.log")
    print("Accessed data")
    df = map_logs_to_dataframe(data[0])
    print(df)
