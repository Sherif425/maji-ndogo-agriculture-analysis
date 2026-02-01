## 🌾 Maji Ndogo Agriculture Data Analysis

### 📌 Project Overview

This project analyzes agricultural survey data from **Maji Ndogo** to understand how **climate, soil, and geography** influence crop performance. The goal is to support data-driven decisions for deploying automated farming systems in optimal locations.

The project demonstrates **data engineering and data analysis skills**, including SQL joins, data cleaning, aggregation, and advanced filtering using Python and Pandas.

---

### 🛠️ Technologies Used

- Python
- Pandas
- SQLite
- SQLAlchemy
- Jupyter Notebook

---

### 📂 Dataset

- SQLite database containing:
  - Geographic features
  - Weather data
  - Soil & crop attributes
  - Farm management metrics

---

### 🔄 Project Workflow

1.  **Data Integration**
    - Joined 4 relational tables using SQL
    - Loaded data into Pandas

2.  **Data Cleaning**
    - Fixed schema misalignment
    - Corrected crop name spelling
    - Removed invalid negative elevations
    - Validated categorical consistency

3.  **Exploratory Analysis**
    - Crop distribution analysis
    - Soil fertility comparison
    - Climate and geography aggregation

4.  **Advanced Analysis**
    - Identified top-performing crops
    - Filtered optimal growing conditions
    - Applied multi-condition filtering logic

---

### 📊 Key Insights

- Certain crops consistently outperform others under specific climatic conditions
- Soil fertility varies significantly by soil type
- Optimal yields are linked to moderate temperatures and low pollution levels

---

### ▶️ How to Run

bash

Copy code

`pip install -r requirements.txt`

python

Copy code

`from src.data_loader import load_agriculture_data from src.data_cleaning import clean_crop_types, fix_elevation  df = load_agriculture_data("data/Maji_Ndogo_farm_survey_small.db") df = clean_crop_types(df) df = fix_elevation(df)`

---

### 👤 Author

**Sherif Mohamed**  
Data Engineer / Data Analyst
