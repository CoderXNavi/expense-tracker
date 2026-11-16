# Student Expense Tracker
**Data Science Industrial Training Project**

A simple and interactive web application to track daily personal expenses, view spending habits, and analyze financial data using interactive charts.

---

## 1. What Does This App Do?
- **Add Expenses:** Enter date, category (Food, Travel, Bills, etc.), amount, and an optional note.
- **Save to CSV:** All data is saved automatically in a local file (`data/expenses.csv`).
- **Summary Cards:** Shows total money spent, total entries recorded, and average per entry.
- **Filter & Search:** Filter by category or search through notes.
- **Interactive Charts:** 
  - Ranked bar chart showing which category took the most money.
  - Pie chart showing percentage breakdown with direct rupee labels.
  - Daily spending timeline bar chart.
- **Manage Data:** Delete specific mistaken entries, undo the last entry, or reset the table columns with one click.
- **Export Data:** Download your expense history anytime as a CSV file.

---

## 2. Tools & Technologies Used
| Tool | Why It Is Used |
|---|---|
| **Python** | Main programming language |
| **Streamlit** | Web interface (no HTML/CSS required) |
| **Pandas** | Reading, writing, and filtering expense data |
| **Plotly Express** | Drawing interactive charts with clear labels |

---

## 3. Project Structure
```text
Spendee/
|-- app.py               # Main Python application
|-- requirements.txt     # List of required packages
|-- README.md            # Project documentation and guide
|-- .streamlit/
|   `-- config.toml      # Theme settings (expense colors)
|-- assets/
|   `-- banner.jpg       # Header banner image
`-- data/
    `-- expenses.csv     # File where expenses are saved
```

---

## 4. How to Run on Your Laptop

### Step 1: Install required libraries
Open your terminal (PowerShell or Command Prompt) inside this project folder and run:
```bash
pip install -r requirements.txt
```

### Step 2: Start the application
```bash
streamlit run app.py
```

### Step 3: Open in browser
Your browser should open automatically. If not, go to:
```text
http://localhost:8501
```

---

## 5. How to Open on Your Phone (Same Wi-Fi)
Great for showing a live demo to teachers or friends without hosting online:
1. Make sure your phone and laptop are connected to the **same Wi-Fi** or mobile hotspot.
2. In the terminal where you ran `streamlit run app.py`, look for the **Network URL**:
   ```text
   Network URL: http://192.168.x.x:8501
   ```
3. Type that exact URL into Chrome or Safari on your phone.

---

## 6. How to Deploy Online (Free - Streamlit Community Cloud)
Deploying online gives you a permanent link (like `https://my-expense-tracker.streamlit.app`) that anyone can open from anywhere in the world.

### Step 1: Create a GitHub Repository
1. Go to [github.com](https://github.com) and sign in (or create a free account).
2. Click **New Repository**.
3. Name it `student-expense-tracker` and choose **Public**.
4. Click **Create repository**.

### Step 2: Upload Your Project Files
You can upload either using Git or directly via the GitHub website:
- **Easy way (Web Upload):**
  1. On your new repository page, click **"uploading an existing file"**.
  2. Drag and drop all project files:
     - `app.py`
     - `requirements.txt`
     - `README.md`
     - `.streamlit/config.toml`
     - `data/expenses.csv`
  3. Click **Commit changes**.

### Step 3: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io) and click **Continue with GitHub**.
2. Click the **"New app"** button.
3. Choose:
   - **Repository:** `your-username/student-expense-tracker`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Click **Deploy!**

Wait 1–2 minutes while Streamlit sets up your app. Once finished, you will receive your live, shareable public link!
