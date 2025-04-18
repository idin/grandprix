# Grand Prix Utils

This directory contains utility functions and classes for data manipulation and processing in the Grand Prix project.

## Files

### Filter.py
Contains the `Filter` and `Filters` classes for flexible data filtering operations on pandas DataFrames, lists, and sets.

### group_take.py
Provides functionality for grouping and aggregating data with the `aggregate` function, supporting various aggregation methods including first, last, mean, min, and max.

### merge_data.py
Contains functions for merging data:
- `join`: Merges two DataFrames with intelligent column handling
- `join_with_dict`: Merges a DataFrame with dictionary data

### dict_of_dicts_to_df.py
Contains the `dict_of_dicts_to_df` function for converting nested dictionaries to pandas DataFrames.

### bring_columns_to_front.py
Contains utilities for DataFrame column management:
- `bring_columns_to_front`: Reorders DataFrame columns
- `must_have_columns`: Decorator for ensuring required columns exist in DataFrame outputs

## Usage

These utilities are designed to work together to provide a comprehensive set of data manipulation tools. They are particularly useful for:
- Data filtering and transformation
- DataFrame merging and joining
- Column management and validation
- Data aggregation and grouping

## Examples

### Filter

```python
import pandas as pd
from grandprix.utils.Filter import Filter

# Create a DataFrame
df = pd.DataFrame({
    'driver': ['Hamilton', 'Verstappen', 'Leclerc', 'Norris'],
    'team': ['Mercedes', 'Red Bull', 'Ferrari', 'McLaren'],
    'points': [100, 95, 80, 70]
})

# Filter by a single value
filter1 = Filter(column='team', values='Mercedes')
result1 = filter1.apply(df)
# Returns only Hamilton's row

# Filter by a range
filter2 = Filter(column='points', min_value=80, max_value=100)
result2 = filter2.apply(df)
# Returns rows for Hamilton, Verstappen, and Leclerc

# Combine filters
combined_filter = filter1 & filter2
result3 = combined_filter.apply(df)
# Returns only Hamilton's row (both conditions met)
```

### Aggregate

```python
import pandas as pd
from grandprix.utils.aggregate import aggregate, Mean, Max, First, Last

# Create a DataFrame
df = pd.DataFrame({
    'driver': ['Hamilton', 'Hamilton', 'Verstappen', 'Verstappen'],
    'race': ['Monaco', 'Silverstone', 'Monaco', 'Silverstone'],
    'position': [1, 2, 2, 1],
    'points': [25, 18, 18, 25]
})

# Aggregate by driver
result = aggregate(
    df,
    group_by='driver',
    avg_position=Mean('position'),
    max_points=Max('points'),
    first_race=First('race'),
    last_race=Last('race')
)
# Returns a DataFrame with one row per driver and the specified aggregations
```

### Merge Data

```python
import pandas as pd
from grandprix.utils.merge_data import join, join_with_dict

# Create DataFrames
drivers_df = pd.DataFrame({
    'driver_id': [1, 2, 3],
    'name': ['Hamilton', 'Verstappen', 'Leclerc'],
    'team': ['Mercedes', 'Red Bull', 'Ferrari']
})

results_df = pd.DataFrame({
    'driver_id': [1, 2, 3],
    'race': ['Monaco', 'Monaco', 'Monaco'],
    'position': [1, 2, 3],
    'points': [25, 18, 15]
})

# Merge DataFrames
merged_df = join(drivers_df, results_df, on='driver_id')
# Returns a DataFrame with driver information and race results

# Merge with dictionary
driver_stats = {
    1: {'wins': 100, 'poles': 100},
    2: {'wins': 30, 'poles': 20},
    3: {'wins': 10, 'poles': 15}
}

merged_with_stats = join_with_dict(drivers_df, driver_stats, on_column='driver_id')
# Returns a DataFrame with driver information and their stats
```

### Dict of Dicts to DataFrame

```python
from grandprix.utils.dict_of_dicts_to_df import dict_of_dicts_to_df

# Create a nested dictionary
driver_data = {
    'Hamilton': {'team': 'Mercedes', 'nationality': 'British', 'wins': 100},
    'Verstappen': {'team': 'Red Bull', 'nationality': 'Dutch', 'wins': 30},
    'Leclerc': {'team': 'Ferrari', 'nationality': 'Monégasque', 'wins': 10}
}

# Convert to DataFrame
df = dict_of_dicts_to_df(driver_data, index_column_name='driver')
# Returns a DataFrame with driver as a column and their attributes as other columns
```

### Bring Columns to Front

```python
import pandas as pd
from grandprix.utils.bring_columns_to_front import bring_columns_to_front, must_have_columns

# Create a DataFrame
df = pd.DataFrame({
    'race': ['Monaco', 'Silverstone', 'Spa'],
    'date': ['2023-05-28', '2023-07-16', '2023-07-30'],
    'winner': ['Hamilton', 'Verstappen', 'Leclerc'],
    'points': [25, 25, 25]
})

# Reorder columns
reordered_df = bring_columns_to_front(df, columns=['date', 'winner'])
# Returns DataFrame with 'date' and 'winner' columns first

# Use the decorator to ensure columns exist and are at the front
@must_have_columns('driver', 'points')
def process_data(df):
    # Process the data
    return df

# The decorator will ensure 'driver' and 'points' columns exist and are at the front
```

## Dependencies
- pandas
- numpy
