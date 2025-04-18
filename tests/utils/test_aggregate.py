from grandprix.utils.aggregate import *
import pytest
import pandas as pd

@pytest.fixture
def df1():

    lando_points = [None, 10, 20]
    oscar_points = [10, None]
    george_points = [30, 40]
    alexander_points = [60, 70]

    lando_races = [1, 2, None]
    oscar_races = [3, 3]
    george_races = [4, 5]
    alexander_races = [6, 7]

    lando_team = ['McLaren'] * 3
    oscar_team = ['McLaren'] * 2
    george_team = ['Mercedes'] * 2
    alexander_team = ['Williams'] * 2

    return pd.DataFrame(
        {
            'first_name': ['Lando'] * 3 + ['Oscar'] * 2 + ['George'] * 2 + ['Alexander'] * 2,
            'points':     lando_points + oscar_points + george_points + alexander_points,
            'races':      lando_races + oscar_races + george_races + alexander_races,
            'team':       lando_team + oscar_team + george_team + alexander_team
        }
    )

def test_first_points_dropna(df1):
    should_be = pd.DataFrame(
        {
            'first_name': ['Lando', 'Oscar', 'George', 'Alexander'],
            'first_points': [10.0, 10.0, 30.0, 60.0]
        }
    ).sort_values(by='first_name').reset_index(drop=True)
    output = aggregate(df1, group_by='first_name', first_points=First('points')).sort_values(by='first_name').reset_index(drop=True)
    assert output.equals(should_be)

def test_first_points_no_dropna(df1):
    should_be = pd.DataFrame(
        {
            'first_name': ['Lando', 'Oscar', 'George', 'Alexander'],
            'first_points': [None, 10.0, 30.0, 60.0]
        }
    ).sort_values(by='first_name').reset_index(drop=True)
    output = aggregate(df1, group_by='first_name', first_points=First('points', drop_na=False)).sort_values(by='first_name').reset_index(drop=True)
    assert output.equals(should_be)

def test_last_points_dropna(df1):
    should_be = pd.DataFrame(
        {
            'first_name': ['Lando', 'Oscar', 'George', 'Alexander'],
            'last_points': [20.0, 10.0, 40.0, 70.0]
        }
    ).sort_values(by='first_name').reset_index(drop=True)
    output = aggregate(df1, group_by='first_name', last_points=Last('points')).sort_values(by='first_name').reset_index(drop=True)
    assert output.equals(should_be)

def test_max_min_points(df1):
    should_be = pd.DataFrame(
        {
            'first_name': ['Lando', 'Oscar', 'George', 'Alexander'],
            'max_points': [20.0, 10.0, 40.0, 70.0],
            'min_points': [10.0, 10.0, 30.0, 60.0]
        }
    ).sort_values(by='first_name').reset_index(drop=True)
    output = aggregate(df1, group_by='first_name', max_points=Max('points'), min_points=Min('points')).sort_values(by='first_name').reset_index(drop=True)
    assert output.equals(should_be)

def test_first_races_dropna(df1):
    should_be = pd.DataFrame(
        {
            'first_name': ['Lando', 'Oscar', 'George', 'Alexander'],
            'first_races': [1.0, 3.0, 4.0, 6.0]
        }
    ).sort_values(by='first_name').reset_index(drop=True)
    output = aggregate(df1, group_by='first_name', first_races=First('races', drop_na=True)).sort_values(by='first_name').reset_index(drop=True)
    print(output)
    print(should_be)
    assert output.equals(should_be)

def test_last_races_no_dropna(df1):
    should_be = pd.DataFrame(
        {
            'first_name': ['Lando', 'Oscar', 'George', 'Alexander'],
            'last_races': [None, 3.0, 5.0, 7.0]
        }
    ).sort_values(by='first_name').reset_index(drop=True)
    output = aggregate(df1, group_by='first_name', last_races=Last('races', drop_na=False)).sort_values(by='first_name').reset_index(drop=True)
    print(output)
    print(should_be)
    assert output.equals(should_be)


def test_mean_points_last_races_dropna(df1):
    should_be = pd.DataFrame(
        {
            'first_name': ['Lando', 'Oscar', 'George', 'Alexander'],
            'mean_points': [15.0, 10.0, 35.0, 65.0],
            'last_races': [2.0, 3.0, 5.0, 7.0]
        }
    ).sort_values(by='first_name').reset_index(drop=True)
    output = aggregate(df1, group_by='first_name', mean_points=Mean('points'), last_races=Last('races', drop_na=True)).sort_values(by='first_name').reset_index(drop=True)
    print(output)
    print(should_be)
    assert output.equals(should_be)


