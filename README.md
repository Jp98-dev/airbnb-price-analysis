[🇧🇷 Versão em Português](README.pt-BR.md)

# 🏙️ Airbnb Price Analysis — New York City

## About the Project

This project presents a complete **Exploratory Data Analysis (EDA)** of Airbnb listings in New York City. The main objective is to understand the key factors that influence listing prices and identify meaningful patterns related to accommodation type, location, reviews, and availability.

In addition to the notebook-based analysis, the project includes an **interactive dashboard built with Streamlit**, allowing users to explore the dataset through filters and visualizations.

This project was designed not only as a technical exercise, but also as a **portfolio project** focused on demonstrating practical analytical skills, data storytelling, and project organization.

---

## 💼 Business Context

Pricing is one of the most important variables in short-term rental marketplaces. Understanding how listing prices vary by region, accommodation type, review volume, and availability can support better strategic decisions for hosts, analysts, and marketplace stakeholders.

This analysis aims to answer practical questions such as:

- Which accommodation types are priced higher?
- Which areas of New York City concentrate premium listings?
- Are highly reviewed listings associated with lower or higher prices?
- How does listing availability relate to price behavior?
- Which neighborhoods stand out in terms of average price?

---

## 🎯 Objective

Analyze Airbnb listing data to identify pricing patterns and generate business insights from the dataset.

---

## 📂 Dataset

| Field | Details |
|---|---|
| **Source** | New York City Airbnb Open Data |
| **Original file** | `AB_NYC_2019.csv` |
| **Processed file** | `airbnb_cleaned.csv` |

---

## 🛠️ Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook
- Pillow

---

## 📁 Project Structure

```bash
airbnb-price-analysis
│
├── app.py
├── README.md
├── README.pt-BR.md
├── requirements.txt
├── .gitignore
│
├── data
│   ├── raw
│   │   └── AB_NYC_2019.csv
│   └── processed
│       └── airbnb_cleaned.csv
│
├── images
│   ├── correlacao.png
│   ├── distribuicao_precos.png
│   ├── mapa_geografico_precos.png
│   ├── nyc_map.jpg
│   ├── outliers_preco.png
│   ├── preco_por_regiao.png
│   ├── preco_por_tipo.png
│   ├── reviews_vs_preco.png
│   └── top10_bairros_preco.png
│
└── notebooks
    └── airbnb_eda.ipynb
```

---

## 🔄 Project Workflow

The project was developed in the following stages:

1. Data loading
2. Data understanding and initial inspection
3. Data cleaning and preprocessing
4. Exploratory data analysis
5. Visualization of key variables and relationships
6. Business insight generation
7. Interactive dashboard creation with Streamlit

---

## 🧹 Data Preparation

The preprocessing stage included:

- Inspection of data types
- Handling of missing values
- Removal of irrelevant columns
- Treatment of extreme values for price analysis
- Creation of a cleaned dataset for analysis and dashboard use

---

## ❓ Main Analysis Questions

- Which accommodation type has the highest average price?
- Which regions concentrate the most expensive listings?
- Is there a relationship between price and number of reviews?
- How does availability relate to listing prices?
- Which neighborhoods have the highest average prices?

---

## 🔍 Core Exploratory Analyses

### 1. Price Distribution
A distribution analysis was used to understand the overall price behavior of listings and identify skewness and concentration patterns.

### 2. Outlier Identification
Boxplots were used to identify extreme values in the price variable and improve the quality of the visual analysis.

### 3. Price by Accommodation Type
A comparative analysis of listing prices by `room_type` was performed to evaluate how accommodation type affects pricing.

### 4. Average Price by Region
Average prices were analyzed by `neighbourhood_group` to highlight the most expensive boroughs.

### 5. Reviews vs. Price
A scatterplot analysis was used to inspect the relationship between listing popularity and price levels.

### 6. Geographic Price Distribution
Listings were plotted geographically over a New York City map to visualize spatial price concentration.

### 7. Top Neighborhoods by Average Price
A neighborhood-level ranking was created to identify local premium pricing clusters.

---

## 💡 Main Insights

- **Entire home/apartment** listings tend to have the highest average prices
- **Manhattan** concentrates the most expensive listings
- Listings with **more reviews** tend to show more competitive pricing patterns
- **Location** is one of the strongest drivers of price variation
- Neighborhood-level analysis shows **strong differences even within the same borough**

---

## 🚀 Advanced Analytical Extensions

### 1. Price Segmentation by Borough and Room Type
Combine both dimensions to identify how pricing behavior changes within each borough for each accommodation type.

### 2. Neighborhood Premium Index
Create a premium index by comparing each neighborhood's average price with the city-wide average price.

### 3. Price per Minimum Stay
Create derived metrics such as:
- `price_per_minimum_stay = price * minimum_nights`
- `price_per_night_minimum = price / minimum_nights`

### 4. Professional Host Proxy Analysis
Use the number of listings per host as a proxy for identifying commercial or professional hosts.

### 5. Review Intensity Analysis
Segment listings by review volume categories or quartiles and compare average prices.

### 6. Availability Segmentation
Create availability bands and compare prices across low, medium, and high availability groups.

### 7. Correlation-Focused Numeric Analysis
Expand the analysis of numerical relationships involving price, availability, minimum nights, and review activity.

---

## 📊 Dashboard

The project includes an **interactive dashboard built with Streamlit**. Users can filter listings by region, accommodation type, price range, number of reviews, and availability.

### Main Dashboard Features

- KPI cards with summary metrics
- Price distribution visualization
- Price by accommodation type
- Average price by region
- Reviews vs. price analysis
- Geographic distribution of listings on the NYC map
- Top 10 neighborhoods by average price
- Filtered data table with CSV download option

---

## 📓 Notebook

The notebook version of the analysis is available at:

```
notebooks/airbnb_eda.ipynb
```

It contains:

- Dataset inspection
- Preprocessing steps
- Exploratory analysis
- Visualizations
- Conclusions and business insights

---

## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/Jp98-dev/airbnb-price-analysis.git
```

### 2. Enter the project folder
```bash
cd airbnb-price-analysis
```

### 3. Create and activate a virtual environment
```bash
python -m venv .venv
```

**On Windows:**
```bash
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit dashboard
```bash
streamlit run app.py
```

---

## ✅ Results

This project demonstrates practical skills in:

- Data cleaning
- Exploratory data analysis
- Feature-oriented thinking
- Business insight generation
- Data visualization
- Dashboard development
- Project organization for portfolio presentation

---

## 🔮 Future Improvements

Possible next steps for this project include:

- Implementing the advanced analytical extensions listed above
- Adding richer statistical summaries
- Improving dashboard layout and visual polish
- Deploying the Streamlit app online
- Expanding the analysis with predictive modeling

---

## 👤 Author

**João Paulo Araújo Maciel**