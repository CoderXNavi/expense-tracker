# Expense Tracker Application
# Data Science Industrial Training Project

import streamlit as st
import pandas as pd
import plotly.express as px
import os
import base64
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Student Expense Tracker",
    page_icon=":material/account_balance_wallet:",
    layout="centered"
)

DATA_FILE = "data/expenses.csv"

# Function to load data from CSV
def load_data():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
        df.to_csv(DATA_FILE, index=False)
        return df
    try:
        df = pd.read_csv(DATA_FILE)
        if not df.empty:
            df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce").fillna(0)
            df["Description"] = df["Description"].fillna("-")
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

# Function to save data to CSV
def save_data(df):
    df.to_csv(DATA_FILE, index=False)

# Load existing data
df = load_data()

# Helper to encode image for background CSS
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

img_b64 = get_base64_image("assets/banner.jpg")
if img_b64:
    hero_bg_desktop = f"background: linear-gradient(to right, rgba(255, 255, 255, 0.96) 42%, rgba(255, 255, 255, 0.72) 68%, rgba(255, 255, 255, 0.25) 100%), url('data:image/jpeg;base64,{img_b64}'); background-size: cover; background-position: center right;"
    hero_bg_mobile = f"background: linear-gradient(rgba(255, 255, 255, 0.88), rgba(255, 255, 255, 0.93)), url('data:image/jpeg;base64,{img_b64}'); background-size: cover; background-position: center;"
else:
    hero_bg_desktop = "background-color: #f8fafc;"
    hero_bg_mobile = "background-color: #f8fafc;"

# Custom CSS: Fully responsive layout, sharp tables, clean mobile styles
st.markdown(f"""
<style>
    /* Hide the form enter helper overlay to avoid text overlap */
    [data-testid="InputInstructions"] {
        display: none !important;
    }

    /* Dark sidebar toggle button (visible when closed) */
    [data-testid="collapsedControl"], [data-testid="stSidebarCollapsedControl"] {
        background-color: #0f172a !important;
        border-radius: 8px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.25) !important;
        top: 14px !important;
        left: 14px !important;
    }
    [data-testid="collapsedControl"] svg, [data-testid="stSidebarCollapsedControl"] svg {
        fill: #ffffff !important;
        color: #ffffff !important;
        stroke: #ffffff !important;
    }
    [data-testid="stSidebarCollapseButton"] button {
        color: #0f172a !important;
    }

    /* Sharp text rendering in table (fixes canvas blur on high-DPI screens) */
    [data-testid="stDataFrame"] canvas {
        image-rendering: -webkit-optimize-contrast !important;
        image-rendering: crisp-edges !important;
    }

    /* Responsive Hero Banner */
    .hero-card {{
        {hero_bg_desktop}
        border-radius: 18px;
        padding: 32px 28px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }}
    .hero-content {{
        max-width: 62%;
    }}
    .hero-badge {{
        background-color: #fee2e2;
        color: #b91c1c;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        display: inline-block;
    }}
    .hero-title {{
        margin: 10px 0 8px 0;
        font-size: clamp(22px, 3.5vw, 30px);
        font-weight: 800;
        color: #0f172a;
        line-height: 1.25;
    }}
    .hero-desc {{
        font-size: 13.5px;
        color: #475569;
        margin: 0 0 10px 0;
        line-height: 1.45;
    }}
    .hero-sub {{
        font-size: 11.5px;
        color: #64748b;
        font-weight: 500;
    }}

    /* Mobile screens (Samsung Galaxy, iPhone, etc.) */
    @media (max-width: 640px) {{
        .hero-card {{
            {hero_bg_mobile}
            padding: 18px 16px !important;
            margin-bottom: 14px !important;
        }}
        .hero-content {{
            max-width: 100% !important;
        }}
        .hero-title {{
            font-size: 21px !important;
            margin: 8px 0 6px 0 !important;
            word-break: normal !important;
        }}
        .hero-desc {{
            font-size: 12px !important;
            margin-bottom: 8px !important;
        }}
    }}

    /* Metric cards styling */
    .metric-card-red {{
        padding: 14px 18px;
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        border-left: 5px solid #d32f2f;
        margin-bottom: 8px;
    }}
    .metric-card-blue {{
        padding: 14px 18px;
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        border-left: 5px solid #1976d2;
        margin-bottom: 8px;
    }}
    .metric-card-amber {{
        padding: 14px 18px;
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        border-left: 5px solid #f57c00;
        margin-bottom: 8px;
    }}
    .metric-title {{
        font-size: 11px;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 2px;
        font-weight: 600;
    }}
    .metric-value-red {{
        font-size: 20px;
        font-weight: 700;
        color: #c62828;
    }}
    .metric-value {{
        font-size: 20px;
        font-weight: 700;
        color: #0f172a;
    }}
</style>
""", unsafe_allow_html=True)

# --- HERO BANNER ---
st.markdown("""
<div class="hero-card">
    <div class="hero-content">
        <span class="hero-badge">Personal Finance & Analytics</span>
        <h1 class="hero-title">Smart Expense Tracking.</h1>
        <p class="hero-desc">Record daily expenditures, monitor your budget, and explore interactive spending insights with ease.</p>
        <span class="hero-sub">Data Science Industrial Training Project</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Categories list
categories = ["Food", "Transportation", "College & Books", "Shopping", "Entertainment", "Bills", "Other"]

# Color palette for charts
EXPENSE_COLORS = [
    "#d32f2f",  # Food (crimson)
    "#1976d2",  # Transportation (blue)
    "#388e3c",  # College & Books (green)
    "#f57c00",  # Shopping (amber)
    "#7b1fa2",  # Entertainment (purple)
    "#0097a7",  # Bills (cyan)
    "#757575"   # Other (slate gray)
]

# --- SIDEBAR: ADD EXPENSE FORM ---
st.sidebar.subheader("Add New Expense")

with st.sidebar.form(key="expense_form", clear_on_submit=True):
    date = st.date_input("Date", value=datetime.today())
    category = st.selectbox("Category", categories)
    amount = st.number_input(
        "Amount (Rs.)",
        min_value=0.0,
        value=None,
        step=10.0,
        placeholder="Type amount here (e.g. 150)"
    )
    description = st.text_input("Short Description", placeholder="e.g. Canteen lunch")
    
    submit_button = st.form_submit_button(label="Save Expense", icon=":material/save:")

if submit_button:
    if amount is None or amount <= 0:
        st.sidebar.warning("Please enter an amount greater than 0.")
    else:
        new_row = pd.DataFrame({
            "Date": [str(date)],
            "Category": [category],
            "Amount": [amount],
            "Description": [description.strip() if description.strip() else "-"]
        })
        df = pd.concat([df, new_row], ignore_index=True)
        save_data(df)
        st.sidebar.success("Expense recorded successfully!")
        st.rerun()

# --- MAIN DASHBOARD ---

if df.empty:
    st.info("No expense records found yet. Use the sidebar on the left to add your first expense.")
else:
    # Summary Metrics Row
    total_spent = df["Amount"].sum()
    total_records = len(df)
    avg_spent = total_spent / total_records if total_records > 0 else 0

    metric_col1, metric_col2, metric_col3 = st.columns(3)
    with metric_col1:
        st.markdown(f"""
        <div class="metric-card-red">
            <div class="metric-title">Total Spent</div>
            <div class="metric-value-red">Rs. {total_spent:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    with metric_col2:
        st.markdown(f"""
        <div class="metric-card-blue">
            <div class="metric-title">Total Records</div>
            <div class="metric-value">{total_records}</div>
        </div>
        """, unsafe_allow_html=True)
    with metric_col3:
        st.markdown(f"""
        <div class="metric-card-amber">
            <div class="metric-title">Average per Entry</div>
            <div class="metric-value">Rs. {avg_spent:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # Clean Two-Tab Interface with Clean Icons
    tab1, tab2 = st.tabs([
        ":material/table_view: All Records",
        ":material/analytics: Charts & Breakdown"
    ])

    # --- TAB 1: ALL RECORDS ---
    with tab1:
        filter_col1, filter_col2 = st.columns(2)
        with filter_col1:
            selected_cat = st.selectbox("Filter by Category", ["All"] + categories)
        with filter_col2:
            search_desc = st.text_input("Search Description", placeholder="Type keywords...")

        # Apply filtering
        filtered_df = df.copy()
        if selected_cat != "All":
            filtered_df = filtered_df[filtered_df["Category"] == selected_cat]
        if search_desc:
            filtered_df = filtered_df[filtered_df["Description"].str.contains(search_desc, case=False, na=False)]

        st.caption(f"Showing {len(filtered_df)} record(s)")
        
        # Display clear, formatted columns with crisp text
        st.dataframe(
            filtered_df,
            width="stretch",
            hide_index=True,
            column_config={
                "Date": st.column_config.TextColumn("Date"),
                "Category": st.column_config.TextColumn("Category"),
                "Amount": st.column_config.NumberColumn(
                    "Amount (Rs.)",
                    format="Rs. %.2f"
                ),
                "Description": st.column_config.TextColumn("Description")
            }
        )

        # Silent Actions (Download CSV and Quiet Delete)
        action_col1, action_col2 = st.columns([1, 1])
        with action_col1:
            csv_data = filtered_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download as CSV",
                icon=":material/download:",
                data=csv_data,
                file_name="my_expenses.csv",
                mime="text/csv"
            )

        with action_col2:
            with st.expander("Remove an Entry"):
                options_list = [
                    f"#{i} | {row['Date']} | {row['Category']} | Rs. {row['Amount']:,.2f} | {row['Description']}"
                    for i, row in df.iterrows()
                ]
                selected_option = st.selectbox("Select entry to delete:", options_list)
                if st.button("Delete Selected Entry", icon=":material/delete:"):
                    selected_idx = df.index[options_list.index(selected_option)]
                    df = df.drop(index=selected_idx).reset_index(drop=True)
                    save_data(df)
                    st.rerun()

    # --- TAB 2: CHARTS & BREAKDOWN ---
    with tab2:
        # Category aggregation
        cat_group = df.groupby("Category")["Amount"].sum().reset_index()
        cat_group = cat_group.sort_values(by="Amount", ascending=False).reset_index(drop=True)
        total_exp = cat_group["Amount"].sum()

        if not cat_group.empty and total_exp > 0:
            top_category = cat_group.iloc[0]["Category"]
            top_amt = cat_group.iloc[0]["Amount"]
            top_pct = (top_amt / total_exp) * 100
            st.info(f"Top Expense: **{top_category}** accounts for **Rs. {top_amt:,.2f}** ({top_pct:.1f}% of all spending).")

        # 1. Ranked Category Bar Chart
        st.write("##### Spending by Category (Ranked)")
        fig_bar = px.bar(
            cat_group,
            x="Category",
            y="Amount",
            text="Amount",
            labels={"Amount": "Total Spent (Rs.)", "Category": ""},
            color="Category",
            color_discrete_sequence=EXPENSE_COLORS
        )
        fig_bar.update_traces(
            texttemplate="Rs. %{text:,.2f}",
            textposition="outside",
            cliponaxis=False
        )
        fig_bar.update_layout(
            showlegend=False,
            margin=dict(t=30, b=30, l=20, r=20),
            yaxis=dict(title="Amount (Rs.)", showgrid=True, gridcolor="#f1f5f9"),
            xaxis=dict(title="")
        )
        st.plotly_chart(fig_bar, width="stretch")

        st.markdown("---")

        # 2. Percentage Share Pie Chart
        st.write("##### Expense Distribution (Percentage)")
        fig_pie = px.pie(
            cat_group,
            names="Category",
            values="Amount",
            color_discrete_sequence=EXPENSE_COLORS
        )
        fig_pie.update_traces(
            textinfo="label+value+percent",
            texttemplate="<b>%{label}</b><br>Rs. %{value:,.0f}<br>(%{percent})",
            insidetextorientation="horizontal"
        )
        fig_pie.update_layout(
            margin=dict(t=20, b=20, l=20, r=20),
            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
        )
        st.plotly_chart(fig_pie, width="stretch")

        st.markdown("---")

        # 3. Daily Spending Timeline
        st.write("##### Daily Spending Timeline")
        date_group = df.groupby("Date")["Amount"].sum().reset_index()
        date_group = date_group.sort_values("Date")
        
        try:
            date_group["Date_Display"] = pd.to_datetime(date_group["Date"]).dt.strftime("%d %b %Y")
        except Exception:
            date_group["Date_Display"] = date_group["Date"].astype(str)

        fig_date = px.bar(
            date_group,
            x="Date_Display",
            y="Amount",
            text="Amount",
            labels={"Amount": "Amount (Rs.)", "Date_Display": "Date"},
            color_discrete_sequence=["#d32f2f"]
        )
        fig_date.update_traces(
            texttemplate="Rs. %{text:,.2f}",
            textposition="outside",
            cliponaxis=False,
            width=0.3 if len(date_group) == 1 else 0.6
        )
        fig_date.update_layout(
            margin=dict(t=30, b=30, l=20, r=20),
            yaxis=dict(title="Amount (Rs.)", showgrid=True, gridcolor="#f1f5f9"),
            xaxis=dict(title="", type="category"),
            bargap=0.4
        )
        st.plotly_chart(fig_date, width="stretch")
