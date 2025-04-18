import pandas as pd

from grandprix.ergast.json import (
    get_season_schedule_json,
    get_race_results_json,
    get_qualifying_results_json,
    get_driver_standings_json,
    get_constructor_standings_json,
    get_lap_times_json,
    get_pit_stop_times_json,
    get_fastest_laps_json,
)

from grandprix.ergast.df import (
    convert_season_schedule_json_to_df,
    convert_race_results_json_to_df,
    convert_qualifying_results_json_to_df,
    convert_driver_standings_json_to_df,
    convert_constructor_standings_json_to_df,
    convert_lap_times_json_to_df,
    convert_pit_stop_times_json_to_df,
    convert_fastest_laps_json_to_df,
)

def test_convert_season_schedule():
    json = get_season_schedule_json(2023)
    df = convert_season_schedule_json_to_df(json)
    assert not df.empty
    assert "race_name" in df.columns
    assert "round" in df.columns

def test_convert_race_results():
    json = get_race_results_json(2023, 1)
    df = convert_race_results_json_to_df(json)
    assert not df.empty
    assert "driver" in df.columns
    assert "position" in df.columns
    assert "finish_time" in df.columns

def test_convert_qualifying_results():
    json = get_qualifying_results_json(2023, 1)
    df = convert_qualifying_results_json_to_df(json)
    assert isinstance(df, pd.DataFrame)
    if not df.empty:
        assert "q1_time" in df.columns
        assert "driver" in df.columns

def test_convert_driver_standings():
    json = get_driver_standings_json(2023, 1)
    df = convert_driver_standings_json_to_df(json)
    assert isinstance(df, pd.DataFrame)
    if not df.empty:
        assert "points" in df.columns
        assert "driver" in df.columns

def test_convert_constructor_standings():
    json = get_constructor_standings_json(2023, 1)
    df = convert_constructor_standings_json_to_df(json)
    assert isinstance(df, pd.DataFrame)
    if not df.empty:
        assert "constructor" in df.columns
        assert "points" in df.columns

def test_convert_lap_times():
    json = get_lap_times_json(2023, 1, "leclerc")
    df = convert_lap_times_json_to_df(json)
    assert isinstance(df, pd.DataFrame)
    if not df.empty:
        assert "lap_time" in df.columns
        assert "driver_id" in df.columns

def test_convert_pit_stop_times():
    json = get_pit_stop_times_json(2023, 1, "leclerc")
    df = convert_pit_stop_times_json_to_df(json)
    assert isinstance(df, pd.DataFrame)
    if not df.empty:
        assert "duration" in df.columns
        assert "stop_number" in df.columns

def test_convert_fastest_laps():
    json = get_fastest_laps_json(2023, 1)
    df = convert_fastest_laps_json_to_df(json)
    assert isinstance(df, pd.DataFrame)
    if not df.empty:
        assert "fastest_lap_time" in df.columns
        assert "fastest_lap_speed" in df.columns
