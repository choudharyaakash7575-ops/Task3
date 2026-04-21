import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
df = pd.read_csv("data.csv")
df['order_date'] = pd.to_datetime(df['order_date'])

st.title("📊 Deep-Dive Analysis Dashboard")

# =========================
# 🔹 KPI SECTION
# =========================

total_revenue = df['amount'].sum()
total_orders = df['order_id'].nunique()
total_customers = df['customer_id'].nunique()

avg_order_value = total_revenue / total_orders

st.subheader("📌 Key KPIs")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Revenue", f"₹{total_revenue}")
col2.metric("Orders", total_orders)
col3.metric("Customers", total_customers)
col4.metric("Avg Order Value", f"₹{round(avg_order_value,2)}")

# =========================
# 🔹 SALES TREND
# =========================

st.subheader("📈 Sales Trend")

sales_trend = df.groupby('order_date')['amount'].sum().reset_index()

fig = px.line(sales_trend, x='order_date', y='amount', title="Sales Over Time")
st.plotly_chart(fig)

# =========================
# 🔹 SEGMENTATION (Region)
# =========================

st.subheader("🌍 Region-wise Revenue")

region_data = df.groupby('region')['amount'].sum().reset_index()

fig2 = px.bar(region_data, x='region', y='amount', color='region')
st.plotly_chart(fig2)

# =========================
# 🔹 CUSTOMER ANALYSIS
# =========================

st.subheader("👤 Customer Analysis")

customer_data = df.groupby('customer_id')['amount'].sum().reset_index()

fig3 = px.pie(customer_data, names='customer_id', values='amount', title="Customer Contribution")
st.plotly_chart(fig3)

# =========================
# 🔹 COHORT ANALYSIS (Simple)
# =========================

st.subheader("📅 Cohort Analysis")

df['month'] = df['order_date'].dt.to_period('M')

cohort = df.groupby(['month'])['customer_id'].nunique().reset_index()

fig4 = px.bar(cohort, x='month', y='customer_id', title="Customers per Month")
st.plotly_chart(fig4)

# =========================
# 🔹 FUNNEL ANALYSIS (Simple)
# =========================

st.subheader("🔻 Funnel Analysis")

funnel_data = pd.DataFrame({
    "Stage": ["Visited", "Added to Cart", "Purchased"],
    "Users": [1000, 600, 300]
})

fig5 = px.funnel(funnel_data, x='Users', y='Stage')
st.plotly_chart(fig5)

st.success("✅ Dashboard Loaded Successfully!")