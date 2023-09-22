from typing import Tuple, Set, Dict

import pandas as pd
from pandas.core.groupby import DataFrameGroupBy

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time
from lab_1.util.extensions import is_add_request


# №11
# Вопрос: Какова эффективность работы службы привлечения клиентов?
# Гипотеза: Коэффициент становление клиентом из посетителя за период [ДЕНЬ/НЕДЕЛЯ/МЕСЯЦ/ВСЕ ВРЕМЯ/ДЕНЬ НЕДЕЛИ] равен: ...

@measure_execution_time
def compute_11(dataframe: pd.DataFrame) -> Tuple[float, str]:
    users: Set[str] = set()
    customers: Set[str] = set()

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[USER])
        url: str = str(row[ENDPOINT])

        if is_add_request(url)[0]:
            customers.add(user_id)
        users.add(user_id)

    result: float = len(customers) / len(users)
    return (
        result,
        f"customers_size={len(customers)}; users_size={len(users)}; result={result}"
    )


@measure_execution_time
def _plot_for_day(grouped_dataframe: pd.DataFrame) -> None:
    # Подсчет датафрейма {День: значение}
    # sns.hist по значениям
    data: DataFrameGroupBy = grouped_dataframe.groupby(grouped_dataframe.TIMESTAMP.dayofyear)
    print(data)

    pass
