import pandas as pd
from grandprix.utils import dict_of_dicts_to_df

def test_dict_of_dicts_to_df():
    data = {
        "driver1": {"team": "Mercedes", "points": 25},
        "driver2": {"team": "Red Bull", "points": 18},
    }
    df = dict_of_dicts_to_df(data, index_column_name="driver")

    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) == {"driver", "team", "points"}
    assert len(df) == 2
    assert df.loc[df["driver"] == "driver1", "team"].values[0] == "Mercedes"
    assert df.loc[df["driver"] == "driver2", "points"].values[0] == 18
