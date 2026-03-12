from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image
import numpy as np


# Page settings
st.set_page_config(
    page_title="Airbnb Price Analysis",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)
sns.set_theme(style="whitegrid")


# Helper functions
def format_currency(value):
    return f"${value:,.2f}"


def format_number(value):
    return f"{value:,.2f}"


@st.cache_data
def load_data():
    base_path = Path(__file__).resolve().parent
    file_path = base_path / "data" / "processed" / "airbnb_cleaned.csv"

    if not file_path.exists():
        st.error(f"File not found: {file_path}")
        st.stop()

    return pd.read_csv(file_path)

# Load data
df = load_data()

# Title
st.title("Airbnb Price Analysis - New York")
st.markdown(
    "Interactive dashboard for exploratory analysis of Airbnb listings, pricing patterns, "
    "location behavior, and accommodation characteristics."
)
st.divider()

# Sidebar filters
st.sidebar.header("Filters")

regions = st.sidebar.multiselect(
    "Select region",
    options=sorted(df["neighbourhood_group"].dropna().unique()),
    default=sorted(df["neighbourhood_group"].dropna().unique())
)

room_types = st.sidebar.multiselect(
    "Select accommodation type",
    options=sorted(df["room_type"].dropna().unique()),
    default=sorted(df["room_type"].dropna().unique())
)

price_range = st.sidebar.slider(
    "Price range",
    min_value=int(df["price"].min()),
    max_value=int(df["price"].max()),
    value=(int(df["price"].min()), int(df["price"].max()))
)

review_range = st.sidebar.slider(
    "Number of reviews",
    min_value=int(df["number_of_reviews"].min()),
    max_value=int(df["number_of_reviews"].max()),
    value=(int(df["number_of_reviews"].min()), int(df["number_of_reviews"].max()))
)

availability_range = st.sidebar.slider(
    "Availability (days per year)",
    min_value=int(df["availability_365"].min()),
    max_value=int(df["availability_365"].max()),
    value=(int(df["availability_365"].min()), int(df["availability_365"].max()))
)


# Apply filters
filtered_df = df[
    (df["neighbourhood_group"].isin(regions)) &
    (df["room_type"].isin(room_types)) &
    (df["price"].between(price_range[0], price_range[1])) &
    (df["number_of_reviews"].between(review_range[0], review_range[1])) &
    (df["availability_365"].between(availability_range[0], availability_range[1]))
].copy()


# Empty result handling
if filtered_df.empty:
    st.warning("No data found for the selected filters. Please adjust the filters and try again.")
else:
    
    # KPI section
    st.subheader("Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total listings", f"{len(filtered_df):,}")
    col2.metric("Average price", format_currency(filtered_df["price"].mean()))
    col3.metric("Median price", format_currency(filtered_df["price"].median()))
    col4.metric("Average reviews", format_number(filtered_df["number_of_reviews"].mean()))

    st.divider()

    
    # Charts row 1
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Price distribution")
        fig1, ax1 = plt.subplots(figsize=(10, 5))
        sns.histplot(filtered_df["price"], bins=40, kde=True, ax=ax1)
        ax1.set_title("Price distribution")
        ax1.set_xlabel("Price")
        ax1.set_ylabel("Frequency")
        st.pyplot(fig1)

    with col_right:
        st.subheader("Price by accommodation type")
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        sns.boxplot(data=filtered_df, x="room_type", y="price", ax=ax2)
        ax2.set_title("Price by accommodation type")
        ax2.set_xlabel("Accommodation type")
        ax2.set_ylabel("Price")
        st.pyplot(fig2)

    st.divider()

    # Charts row 2
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Average price by region")
        price_by_region = (
            filtered_df.groupby("neighbourhood_group")["price"]
            .mean()
            .sort_values(ascending=False)
        )

        fig3, ax3 = plt.subplots(figsize=(10, 5))
        sns.barplot(x=price_by_region.index, y=price_by_region.values, ax=ax3)
        ax3.set_title("Average price by region")
        ax3.set_xlabel("Region")
        ax3.set_ylabel("Average price")
        st.pyplot(fig3)

    with col_right:
        st.subheader("Reviews vs price")
        fig4, ax4 = plt.subplots(figsize=(10, 5))
        sns.scatterplot(
            data=filtered_df,
            x="number_of_reviews",
            y="price",
            alpha=0.5,
            ax=ax4
        )
        ax4.set_title("Reviews vs price")
        ax4.set_xlabel("Number of reviews")
        ax4.set_ylabel("Price")
        st.pyplot(fig4)

    st.divider()

    # Geographic chart
    st.subheader("Geographic distribution of listings")

    project_root = Path(__file__).resolve().parent
    images_dir = project_root / "images"

    map_candidates = [
        images_dir / "nyc_map.jpg",
        images_dir / "nyc_map.jpeg",
        images_dir / "nyc_map.png",
    ]

    map_path = next((path for path in map_candidates if path.exists()), None)

    if map_path is None:
        st.warning("Map image not found in the images folder. The dashboard is running without the background map.")
    else:
        map_img = Image.open(map_path)
        map_img = np.array(map_img)

        lon_min, lon_max = -74.255, -73.695
        lat_min, lat_max = 40.485, 40.925
        fig_map, ax_map = plt.subplots(figsize=(12, 8))

        ax_map.imshow(
            map_img,
            extent=[lon_min, lon_max, lat_min, lat_max],
            aspect="auto",
            alpha=0.9,
            zorder=1
        )

        scatter = ax_map.scatter(
            filtered_df["longitude"],
            filtered_df["latitude"],
            c=filtered_df["price"],
            cmap="viridis",
            alpha=0.35,
            s=8,
            edgecolors="none",
            zorder=2
        )

        ax_map.set_xlim(lon_min, lon_max)
        ax_map.set_ylim(lat_min, lat_max)
        ax_map.set_title("Geographic distribution of prices")
        ax_map.set_xlabel("Longitude")
        ax_map.set_ylabel("Latitude")

        cbar = plt.colorbar(scatter, ax=ax_map)
        cbar.set_label("Price")

        st.pyplot(fig_map)
    
    # Filtered table + download
    st.subheader("Filtered data table")

    display_columns = [
        "neighbourhood_group",
        "neighbourhood",
        "room_type",
        "price",
        "minimum_nights",
        "number_of_reviews",
        "reviews_per_month",
        "availability_365"
    ]

    available_display_columns = [col for col in display_columns if col in filtered_df.columns]
    table_df = filtered_df[available_display_columns].copy()

    numeric_cols = table_df.select_dtypes(include="number").columns
    table_df[numeric_cols] = table_df[numeric_cols].round(2)

    st.dataframe(table_df, use_container_width=True)

    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name="airbnb_filtered_data.csv",
        mime="text/csv"
    )