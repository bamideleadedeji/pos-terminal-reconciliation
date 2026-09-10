import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="POS Agency Banking Reconciliation Suite",
    page_icon=" ",
    layout="wide",
)

st.title(" POS Agency Banking Daily Reconciliation Suite")
st.caption(
    "Interactive Web Engine | Built for POS Terminal Operators & Agency Banking"
    " Agents"
)

# Sidebar - Sales & Monetization CTA
st.sidebar.header(" Get the Full Master Template")
st.sidebar.info(
    "Want the offline Excel & Google Sheets master file with auto-calculating"
    " formulas?"
)
st.sidebar.markdown(
    "[👉 Buy Master Template on"
    " Gumroad](https://bamidele38.gumroad.com/l/sme-daily-tracker)"
)

# Session State for POS Log
if "df_pos" not in st.session_state:
  st.session_state.df_pos = pd.DataFrame({
      "Txn ID": ["POS-101", "POS-102", "POS-103", "POS-104"],
      "Time": ["08:30 AM", "09:15 AM", "10:00 AM", "11:20 AM"],
      "Txn Type": [
          "Cash Withdrawal",
          "Direct Deposit",
          "Cash Withdrawal",
          "Utility Bill Pay",
      ],
      "Amount (₦)": [10000.0, 25000.0, 50000.0, 15000.0],
      "Customer Fee (₦)": [200.0, 300.0, 500.0, 250.0],
      "Provider Cost (₦)": [50.0, 100.0, 150.0, 70.0],
  })

# 1. Interactive Transaction Ledger
st.subheader("1. Daily POS Transaction Log")
st.write("Edit transactions below to test live float & commission balancing:")

edited_df = st.data_editor(
    st.session_state.df_pos, num_rows="dynamic", use_container_width=True
)

# Calculate Commission
edited_df["Net Commission (₦)"] = (
    edited_df["Customer Fee (₦)"] - edited_df["Provider Cost (₦)"]
)

# 2. Float & Cash Till Reconciliation
st.markdown("---")
st.subheader("2. Cash Float & Till Reconciliation Engine")

col1, col2 = st.columns(2)

with col1:
  starting_float = st.number_input(
      "Starting Morning Cash Float (₦)", value=100000.0, step=5000.0
  )

withdrawals = edited_df[edited_df["Txn Type"] == "Cash Withdrawal"][
    "Amount (₦)"
].sum()
deposits = edited_df[edited_df["Txn Type"] == "Direct Deposit"][
    "Amount (₦)"
].sum()
fees_collected = edited_df["Customer Fee (₦)"].sum()

expected_evening_cash = starting_float - withdrawals + deposits + fees_collected

with col2:
  actual_evening_cash = st.number_input(
      "Actual Evening Physical Cash Counted (₦)",
      value=float(expected_evening_cash),
      step=1000.0,
  )

variance = actual_evening_cash - expected_evening_cash

# Summary Metrics
m1, m2, m3 = st.columns(3)
m1.metric("Expected Cash Balance", f"₦{expected_evening_cash:,.2f}")
m2.metric(
    "Total Net Commission Earned",
    f"₦{edited_df['Net Commission (₦)'].sum():,.2f}",
)

with m3:
  if variance == 0:
    st.success(" TILL BALANCED")
  elif variance < 0:
    st.error(f" FLOAT SHORTAGE: ₦{abs(variance):,.2f}")
  else:
    st.warning(f" SURPLUS: ₦{variance:,.2f}")

# 3. Chart Breakdown
st.markdown("---")
st.subheader("3. Transaction Type Volume Breakdown")
fig = px.pie(
    edited_df,
    values="Amount (₦)",
    names="Txn Type",
    hole=0.4,
    title="Volume by Transaction Category",
)
st.plotly_chart(fig, use_container_width=True)
