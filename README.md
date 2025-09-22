# Traffic Accident Analysis Dashboard

This project implements an interactive dashboard for analyzing traffic accident data using **Streamlit**, **XGBoost**, and **LLM Llama 3.1** integration via **Ollama**.

---

## 🚀 Features

### Interactive Dashboard
- **Year Selection:** Choose a year (2020-2025) to view accident data.
- **Accident Heatmap** by state (UF) and type.
- **Hourly Risk Prediction** with line charts.
- **Main Cause Analysis** using horizontal bar charts.
- **Interactive Charts** for accidents by day of the week and weather conditions.
- **Accident Risk Density Map:** A visual representation of accident density based on predicted risk.
- **Top 10 Critical Road Sections:** A table showing the 10 road segments with the highest accident risk.

### LLM Integration
- **Llama 3.1 via Ollama** for contextual data analysis.
- **Chat Interface** to ask questions about the data.
- **Responses based** on the context of the loaded data.

## 📋 Prerequisites

### Python and Dependencies
Install the required libraries with pip:
```bash
pip install streamlit pandas plotly xgboost scikit-learn requests ollama numpy matplotlib seaborn tqdm jupyter IPython pathlib bcrypt python-dotenv uvicorn starlette itsdangerous authlib

### Ollama (para LLM)
```bash
# Install Ollama
curl -fsSL [https://ollama.ai/install.sh](https://ollama.ai/install.sh) | sh

# Start the service
ollama serve

# Download the Llama 3.1 model
ollama pull llama3.1
```

## 🗂️ Data Structure

The dashboard expects CSV files with specific naming conventions and columns.

- **Accident Files:** `acidentesYYYY_todas_causas_tipos.csv` (where YYYY is the year)
- **ataTran Files:** `datatranYYYY.csv` (where YYYY is the year)

**Expected columns:**
- `data_inversa`: Accident date
- `horario`: Accident time
- `uf`: Federal Unit (State)
- `km`: Road kilometer
- `causa_acidente`: Accident cause
- `tipo_acidente`: Accident type
- `classificacao_acidente`: Classification (with/without victims)
- `condicao_metereologica`: Weather conditions
- `tipo_pista`: Road type
- `dia_semana`: Day of the week
- `latitude`: Accident latitude (comma or dot format)
- `longitude`: Accident longitude (comma or dot format)

### 🚀 How to Run (Windows)

### 1. Organize the Data
Create a folder named `upload` in the same directory as `app_optimized.py` and place all the provided CSV files inside it.

### 2. Install Dependencies
Open Command Prompt (CMD) or PowerShell in the project directory and execute:
```cmd
pip install -r requirements.txt
```

### 3. Run the Dashboard
In the same Command Prompt (CMD) or PowerShell, execute:
```cmd
streamlit run app_optimized.py 
```

### 4. Access in Browser
Open your browser and navigate to:
```
http://localhost:8501
```

## 📊 Dashboard Features

### 1. Main Visualizations
- **Heatmap:** Distribution of accidents by state (UF) and type
- **Line Chart:** Accident risk by time of day
- **Bar Chart:** Top 10 accident causes
- **Pie Chart:** Distribution by day of the week
- **Bar Chart:** Accidents by weather condition

### 2. Chat with LLM
- **Text Interface** for questions
- **Data Context** provided automatically
- **Responses based** on the analyzed data



## 🔧 Configurations

### Data Files
The CSV files must be in the `upload` folder within the same directory as `app_optimized.py`.

## 📈 Metrics and KPIs

- **Total Records:** Number of accidents analyzed
- **AUC-ROC Score:** Classifier model performance
- **Accuracy:** Prediction precision
- **Feature Importance:** Which variables most influence risk

### Problem: Data Not Loading
**Solution:** Check if the CSV files are in the `upload` folder and if the encoding is correct (`encoding=\'latin1\'`)
