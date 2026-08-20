# Basic Coding

## dataAnalizer

To build a Tkinter application that processes Excel data, calculates statistics, and allows filtering of the X-axis range, you must import pandas for data aggregation, openpyxl to handle Excel spreadsheets, matplotlib to embed an interactive graph, and use standard Tkinter widgets to accept numerical boundary inputs.

```python
# Save this code as a script (e.g., excel_analyzer_gui.py) and run it with Python 3.
# Ensure you have dependencies installed: pip install pandas openpyxl matplotlib
```

### 🏛️ Functional Overview of the Architecture

*   **Excel Data Consumption Pipeline**: Uses `pandas.read_excel()` to scan uploaded data. The application dynamically loops through column vectors, strips non-numeric arrays, and registers available dimensions directly into your UI dropdown boxes.
*   **Dynamic Matrix Slicing**: When you change your coordinate entries, Pandas evaluates the dataframe via boolean masking (`df[(df[X] >= min) & (df[X] <= max)]`). This filters out data outside your boundaries before computing metrics.
*   **Decoupled Multi-Metric Core**: The left dashboard frame isolates operations into precise summary cards, capturing:
    *   **Average**: Mathematical arithmetic mean.
    *   **Mean (Median)**: The exact structural midpoint value of the numerical matrix.
    *   **Max / Min**: Peak boundaries visible inside your slice parameters.
*   **Embedded Plot Lifecycle Control**: `FigureCanvasTkAgg` opens a pipeline showing an interactive charting layout alongside UI tools without launching external graphic popups. Old charts are destroyed before redrawing to keep memory usage low.

### 🧪 Creating a Test File
To verify the application quickly without real business sheets, generate a dummy layout called `test_data.xlsx` via this Python snippet:
```python
import pandas as pd
import numpy as np

# Generates 100 row units of clean coordinates
test_df = pd.DataFrame({
    'Time_Seconds': np.arange(1, 101),
    'Voltage_Output': np.sin(np.linspace(0, 10, 100)) * 50 + np.random.normal(0, 2, 100)
})
test_df.to_excel('test_data.xlsx', index=False)
```
