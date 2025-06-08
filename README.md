# 📊 Data Cleaning and Preprocessing – Elevate Labs Internship Task 1

This project is part of the Elevate Labs Data Analyst Internship Task 1. The goal is to clean and preprocess a medical appointment dataset for further analysis and visualization.

---

## 📁 Dataset

- **Filename**: `appointments.csv`
- **Source**: Provided for internship assessment.
- **Columns include**:
  - `PatientId`, `AppointmentID`, `Gender`, `ScheduledDay`, `AppointmentDay`
  - `Age`, `Neighbourhood`, `Scholarship`, `Hipertension`, `Diabetes`
  - `Alcoholism`, `Handcap`, `SMS_received`, `No-show`

---

## 🛠️ Steps Performed

1. **Loaded the dataset** using `pandas`.
2. **Checked for missing values** and applied forward fill (`ffill`) to handle them.
3. **Identified and removed duplicates** using `.duplicated()` and `.drop_duplicates()`.
4. **Standardized categorical columns** like `Gender` (converted to lowercase and stripped whitespace).
5. **Converted date columns** (`ScheduledDay`, `AppointmentDay`) to proper datetime format.
6. **Renamed column headers** to lowercase and replaced spaces with underscores for consistency.
7. **Converted the Age column** to integer type (handling non-numeric errors).
8. **Saved cleaned dataset** as `cleaned_dataset.csv`.

---

## ✅ Output

- **Cleaned File**: `cleaned_dataset.csv`
- **Location**: Same folder as the source dataset.

---

## 🐍 Technologies Used

- Python 3.11+
- `pandas` library

---

## 📦 How to Run

1. Make sure Python and `pandas` are installed:
   ```bash
   pip install pandas
2. Run the script:
  python demo.py
3. Check the output file:

cleaned_dataset.csv will be created in the same directory.
