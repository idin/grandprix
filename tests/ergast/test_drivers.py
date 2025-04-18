from grandprix.ergast import get_drivers, add_driver_metadata
import pandas as pd

def test_get_drivers():
    df = get_drivers(year=2024)
    assert 'driver_id' in df.columns

    # some drivers: Lando, Albon, Russell
    nando = df[df['last_name'] == 'Norris']
    assert len(nando) == 1
    assert nando['first_name'].iloc[0] == 'Lando'

    albon = df[df['last_name'] == 'Albon']
    assert len(albon) == 1
    assert albon['first_name'].iloc[0] == 'Alexander'

    russell = df[df['last_name'] == 'Russell']
    assert len(russell) == 1
    assert russell['first_name'].iloc[0] == 'George'

    existing_nationalities = ['British', 'Danish', 'French', 'Monegasque', 'German', 'Dutch']
    non_existing_nationalities = ['Italian', 'Brazilian']
    
    non_exsiting = set(non_existing_nationalities) & set(df['nationality'].unique())
    assert len(set(existing_nationalities) & set(df['nationality'].unique())) == len(existing_nationalities)
    assert len(non_exsiting) == 0

 
def test_add_driver_metadata():
    df = pd.DataFrame({
        'first_name': ['Lando', 'Alexander', 'George'],
        'last_name': ['Norris', 'Albon', 'Russell']
    })
    df = add_driver_metadata(df)
    assert 'driver_id' in df.columns
    assert 'date_of_birth' in df.columns
    assert 'url' in df.columns
    assert df.shape[0] == 3
