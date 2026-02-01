import pandas as pd
from sqlalchemy import create_engine

def load_agriculture_data(db_path):
    engine = create_engine(f"sqlite:///{db_path}")
    
    query = """
    SELECT
        g.Field_ID,
        g.Elevation,
        g.Latitude,
        g.Longitude,
        g.Location,
        g.Slope,
        w.Rainfall,
        w.Min_temperature_C,
        w.Max_temperature_C,
        w.Ave_temps,
        s.Soil_fertility,
        s.Soil_type,
        s.pH,
        f.Pollution_level,
        f.Plot_size,
        f.Annual_yield,
        f.Crop_type,
        f.Standard_yield
    FROM geographic_features g
    LEFT JOIN weather_features w ON g.Field_ID = w.Field_ID
    LEFT JOIN soil_and_crop_features s ON g.Field_ID = s.Field_ID
    LEFT JOIN farm_management_features f ON g.Field_ID = f.Field_ID
    """
    
    return pd.read_sql_query(query, engine)
