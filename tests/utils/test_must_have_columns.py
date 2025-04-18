import pytest
import pandas as pd
from grandprix.utils import must_have_columns

@must_have_columns(["a", "b"])
def good_df():
    return pd.DataFrame({"a": [1], "b": [2]})

@must_have_columns(["a", "b"])
def missing_col():
    return pd.DataFrame({"a": [1]})

@must_have_columns("a", "b")
def good_df_2():
    return pd.DataFrame({"a": [1], "b": [2]})

@must_have_columns("a", "b")
def missing_col_2():
    return pd.DataFrame({"a": [1]})

@must_have_columns(["a"])
def not_a_dataframe():
    return {"a": 1}

@must_have_columns("a")
def not_a_dataframe_2():
    return {"a": 1}

@must_have_columns("b", "c", bring_to_front=True)
def good_df_and_bring_to_front():
    return pd.DataFrame({"a": [1], "b": [2], "c": [3]})

def test_must_have_columns_passes():
    df = good_df()
    assert isinstance(df, pd.DataFrame)
    assert "a" in df.columns and "b" in df.columns

def test_must_have_columns_raises_for_missing():
    with pytest.raises(KeyError, match="Missing columns"):
        missing_col()

def test_must_have_columns_raises_for_non_dataframe():
    with pytest.raises(TypeError, match="must return a pandas DataFrame"):
        not_a_dataframe()

def test_must_have_columns_passes_with_multiple_args():
    df = good_df_2()
    assert isinstance(df, pd.DataFrame)
    assert "a" in df.columns and "b" in df.columns

def test_must_have_columns_raises_for_missing_with_multiple_args():
    with pytest.raises(KeyError, match="Missing columns"):
        missing_col_2()

def test_must_have_columns_raises_for_non_dataframe_with_multiple_args():
    with pytest.raises(TypeError, match="must return a pandas DataFrame"):
        not_a_dataframe_2()

def test_must_have_columns_brings_to_front():
    df = good_df_and_bring_to_front()
    assert isinstance(df, pd.DataFrame)
    assert "b" in df.columns and "c" in df.columns
    assert df.columns[0] == "b" and df.columns[1] == "c"


