def clean_crop_types(df):
    df['Crop_type'] = df['Crop_type'].replace({
        'Cassaval': 'Cassava',
        'Wheatn': 'Wheat',
        'Teaa': 'Tea'
    })
    return df

def fix_elevation(df):
    df['Elevation'] = df['Elevation'].abs()
    return df
