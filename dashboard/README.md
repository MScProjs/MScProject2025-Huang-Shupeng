# Student Dropout Risk Dashboard

This folder contains the Streamlit dashboard developed as part of the MSc Data Science dissertation project.  
The dashboard provides interactive exploration of student dropout probabilities and SHAP-based feature explanations.

---

## Files
- `app.py` : Streamlit application  
- `requirements.txt` : Python dependencies  
- `data/df_dashboard_final_with_shap_direction.csv` : Input dataset used by the app  

---

## How to Run Locally

1. Clone the repository and enter the `dashboard` folder:
   ```bash
   git clone https://github.com/MScProjs/MScProject2025-Huang-Shupeng.git
   cd MScProject2025-Huang-Shupeng/dashboard
2. (Optional) Create a virtual environment:
    python -m venv .venv
    source .venv/bin/activate   # On Windows: .venv\Scripts\activate

3.  Install dependencies:
   pip install -r requirements.txt

4. Run the dashboard:
   streamlit run app.py
Alternatively, you can run with full path, e.g.:
streamlit run path/to/dashboard/app.py


