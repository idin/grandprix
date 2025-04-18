from grandprix.ergast.json import (
    get_race_results_json,
    get_season_schedule_json,
    get_qualifying_results_json,
    get_driver_standings_json,
    get_constructor_standings_json,
    get_lap_times_json,
    get_pit_stop_times_json,
    get_fastest_laps_json,
    get_ergast_json,
)

def test_get_ergast_data():
    data = get_ergast_json("current/last/results")
    assert data is not None
    assert "RaceTable" in data
    assert "Races" in data["RaceTable"]

def test_get_race_results_structure():
    results = get_race_results_json(2023, 1)
    assert isinstance(results, list)
    assert len(results) > 0

    sample = results[0]
    assert "Driver" in sample
    assert "Constructor" in sample
    assert "position" in sample
    assert "status" in sample
    assert "givenName" in sample["Driver"]
    assert "name" in sample["Constructor"]

def test_get_season_schedule():
    races = get_season_schedule_json(2023)
    assert isinstance(races, list)
    assert len(races) > 0
    assert "raceName" in races[0]

def test_get_qualifying_results():
    results = get_qualifying_results_json(2023, 1)
    assert isinstance(results, list)
    assert len(results) > 0
    assert "Q1" in results[0] or "Q2" in results[0] or "Q3" in results[0]

def test_get_driver_standings():
    standings = get_driver_standings_json(2023, 1)
    assert isinstance(standings, list)
    assert len(standings) > 0
    assert "points" in standings[0]
    assert "Driver" in standings[0]

def test_get_constructor_standings():
    standings = get_constructor_standings_json(2023, 1)
    assert isinstance(standings, list)
    assert len(standings) > 0
    assert "points" in standings[0]
    assert "Constructor" in standings[0]

def test_get_lap_times():
    laps = get_lap_times_json(2023, 1, "leclerc")
    assert isinstance(laps, list)
    if laps:
        assert "number" in laps[0]
        assert "Timings" in laps[0]

def test_get_pit_stop_times():
    stops = get_pit_stop_times_json(2023, 1, "leclerc")
    assert isinstance(stops, list)
    if stops:
        assert "driverId" in stops[0]
        assert "duration" in stops[0]

def test_get_fastest_laps():
    laps = get_fastest_laps_json(2023, 1)
    assert isinstance(laps, list)
    if laps:
        assert "FastestLap" in laps[0]
        assert "Time" in laps[0]["FastestLap"]
