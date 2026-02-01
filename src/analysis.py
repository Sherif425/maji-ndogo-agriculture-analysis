def explore_crop_distribution(df, crop):
    subset = df[df['Crop_type'] == crop]
    return subset['Rainfall'].mean(), subset['Elevation'].mean()

def analyse_soil_fertility(df):
    result = df.groupby('Soil_type')['Soil_fertility'].mean()
    result.index.name = 'Soil_Type'
    return result

def climate_geography_influence(df, column):
    return (
        df.groupby(column)[
            ['Elevation','Min_temperature_C','Max_temperature_C','Rainfall']
        ].mean().reset_index()
    )

def find_ideal_fields(df):
    avg_yield = df['Standard_yield'].mean()
    return (
        df[df['Standard_yield'] > avg_yield]
        .groupby('Crop_type')
        .size()
        .sort_values(ascending=False)
        .index[0]
    )

def find_good_conditions(df, crop_type):
    avg_yield = df['Standard_yield'].mean()
    result = df[
        (df['Crop_type'] == crop_type) &
        (df['Standard_yield'] > avg_yield) &
        (df['Ave_temps'] >= 12) & (df['Ave_temps'] <= 15) &
        (df['Pollution_level'] < 0.0001)
    ]
    return result.iloc[:, 1:]
