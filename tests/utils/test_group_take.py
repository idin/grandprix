import pandas as pd
from grandprix.utils import aggregate

def test_group_take():
    df = pd.DataFrame({
        "group": ["x", "x", "x", "y", "y", "y"],
        "value": [None, 5, 6, 50, 60, None],
        'year': [2020, 2022, 2021, 1999, 1990, 1995]
    })
    take_first = aggregate(df, group_by="group", method="first", mean_columns="value", min_columns="year", max_columns="year", skipna=True)

    take_first_should_be = pd.DataFrame({
        "group": ["x", "y"],
        "value": [5.0, 50.0],
        "value_mean": [5.5, 55.0],
        "year_min": [2020, 1990],
        "year_max": [2022, 1999]
    })
    print(take_first)
    print(take_first_should_be)
    assert take_first.equals(take_first_should_be)

    take_last = aggregate(df, group_by="group", method="last", skipna=True)
    take_last_should_be = pd.DataFrame({
        "group": ["x", "y"],
        "value": [6.0, 60.0]
    })
    assert take_last.equals(take_last_should_be)

    take_first_with_na = aggregate(df, group_by="group", method="first", skipna=False)
    take_first_with_na_should_be = pd.DataFrame({
        "group": ["x", "y"],
        "value": [None, 50.0]
    })
    assert take_first_with_na.equals(take_first_with_na_should_be)

    take_last_with_na = aggregate(df, group_by="group", method="last", skipna=False)
    take_last_with_na_should_be = pd.DataFrame({
        "group": ["x", "y"],
        "value": [6.0, None]
    })
    assert take_last_with_na.equals(take_last_with_na_should_be)
