from typing import Tuple, Dict, List

import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time


# №12
# Вопрос: Какова эффективность работы службы привлечения клиентов?
# Гипотеза: Среднее число посетителей за период [ДЕНЬ/НЕДЕЛЯ/МЕСЯЦ/ВСЕ ВРЕМЯ/ДЕНЬ НЕДЕЛИ] равно: ...

@measure_execution_time
def compute_12(dataframe: pd.DataFrame) -> Tuple[float, str]:
    visitors: Dict[str, List[str]] = dict()

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[USER])
        date: str = f"{row[DAY]}#{row[MONTH]}#{row[YEAR]}"

        if date not in visitors.keys():
            visitors.update({date: []})

        if user_id not in visitors[date]:
            visitors[date].append(user_id)

    overall_sum: int = 0

    for amount_of_users in visitors.values():
        sum_for_day: int = len(amount_of_users)
        overall_sum += sum_for_day

    result: float = overall_sum / len(visitors)
    return (
        result,
        f"overall_sum={overall_sum}; visitors_count={len(visitors)}; result={result}"
    )
