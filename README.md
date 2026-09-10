#  POS Agency Banking Daily Reconciliation Suite

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An automated financial ledger, live reconciliation engine, and interactive dashboard built specifically for Point-of-Sale (POS) operators, mobile money merchants, and agency banking outlets. 

This repository houses both the **Python-driven Streamlit web application** for real-time browser-based testing and the source code generator for the **offline Microsoft Excel (`.xlsx`) & Google Sheets master templates**.

---

##  Key Features & Business Value

- ** Instant Till & Float Reconciliation:** Automatically balances starting morning cash floats against daily withdrawals (Cash Out), deposits (Cash In), and utility bill payments to flag cash shortages or surpluses instantly.
- ** Commission & Fee Calculator:** Computes net commissions by subtracting provider transaction costs (OPay, Moniepoint, Palmpay, Quickteller) from customer service charges in real time.
- ** Mobile & Cloud Compatible:** Works seamlessly across smartphones, tablets, and desktops via Google Sheets or native Microsoft Excel.
- **🛡️ Audit & Discrepancy Tracking:** Provides clean, structured data logging to eliminate daily cash leakages, operator theft, and unrecorded customer transfers.

---

##  Repository Structure

```text
pos-terminal-reconciliation/
│
├── .streamlit/
│   └── config.toml             # Streamlit app layout & visual theme configuration
├── data/
│   └── POS_Terminal_Daily_Reconciliation_Master.xlsx  # Excel master workbook
├── app.py                      # Interactive Streamlit Web Application
├── generator.ipynb             # Jupyter Notebook containing Python openpyxl engine
├── requirements.txt            # Environment dependencies
└── README.md                   # Project documentation & distribution portal

 Live Demo & Web Application
Test the live interactive reconciliation model directly in your browser:
👉 Launch Streamlit Interactive Web App https://pos-terminal-reconciliation-bvwvvhc3vjfabmmvexvqzf.streamlit.app/

🛍️ Get the Full Master Template (Excel & Google Sheets)
For offline use, daily commercial operations, or deployment across multiple agency outlets:
👉 Buy Master Template on Gumroad

Local Installation & Development Setup
To run this project locally on your machine:

Clone the repository:

Bash
git clone [https://github.com/bamideleadedeji/pos-terminal-reconciliation.git](https://github.com/bamideleadedeji/pos-terminal-reconciliation.git)
cd pos-terminal-reconciliation
Create and activate a virtual environment:

Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install required dependencies:

Bash
pip install -r requirements.txt
Launch the Streamlit app:

Bash
streamlit run app.py
🛠️ Built With
Python 3.10+

Streamlit - Interactive Web UI framework

Pandas - Data manipulation and transaction aggregation

OpenPyXL - Programmatic Excel workbook formatting and dynamic formula generation

Plotly - Data visualization and payment category analytics

👨‍💻 Author & Contact
Bamidele Adedeji

Founder & Principal Consultant, Dejifolakemi Enterprises

GitHub: @bamideleadedeji

Gumroad Store: Dejifolakemi Enterprises

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.


***

### Next Action Step
You can create a `README.md` file in your project folder, paste this text inside, and commit it to GitHub using:

```bash
git add README.md
git commit -m "Add production-ready README documentation"
git push origin main
