import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ExcelAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Data Statistical Analyzer")
        self.root.geometry("1000x700")
        self.root.minsize(900, 600)
        
        # State variables
        self.df = None
        self.x_col = None
        self.y_col = None
        self.canvas = None
        
        self.create_widgets()
        
    def create_widgets(self):
        # Top Panel - File Selection & Column Configuration
        top_frame = ttk.LabelFrame(self.root, text=" 1. Load Data Source ", padding=10)
        top_frame.pack(fill="x", padx=15, pady=10)
        
        self.file_label = ttk.Label(top_frame, text="No Excel file selected...", font=("Arial", 10, "italic"))
        self.file_label.pack(side="left", padx=5, expand=True, fill="x")
        
        browse_btn = ttk.Button(top_frame, text="Browse Excel File", command=self.load_excel_file)
        browse_btn.pack(side="right", padx=5)
        
        # Column selection dropdowns (hidden until data loads)
        self.col_frame = ttk.Frame(self.root, padding=5)
        self.col_frame.pack(fill="x", padx=15)
        
        # Main Dashboard split layout (Left: Controls/Stats, Right: Visualization)
        self.main_split = ttk.Frame(self.root)
        self.main_split.pack(fill="both", expand=True, padx=15, pady=5)
        
        # Left Panel (Controls & Statistical Cards)
        self.left_panel = ttk.Frame(self.main_split, width=320)
        self.left_panel.pack(side="left", fill="both", padx=(0, 10))
        self.left_panel.pack_propagate(False) # Keep width fixed
        
        # Axis Constraints Section
        self.limit_frame = ttk.LabelFrame(self.left_panel, text=" 2. X-Axis Constraints ", padding=10)
        self.limit_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(self.limit_frame, text="Min X Value:").grid(row=0, column=0, sticky="w", pady=2)
        self.xmin_entry = ttk.Entry(self.limit_frame, width=12)
        self.xmin_entry.grid(row=0, column=1, pady=2, padx=5)
        
        ttk.Label(self.limit_frame, text="Max X Value:").grid(row=1, column=0, sticky="w", pady=2)
        self.xmax_entry = ttk.Entry(self.limit_frame, width=12)
        self.xmax_entry.grid(row=1, column=1, pady=2, padx=5)
        
        self.apply_btn = ttk.Button(self.limit_frame, text="Apply & Recalculate", command=self.update_dashboard, state="disabled")
        self.apply_btn.grid(row=2, column=0, columnspan=2, pady=(8, 0), sticky="ew")
        
        # Summary Statistics Summary Block
        self.stats_frame = ttk.LabelFrame(self.left_panel, text=" 3. Statistical Metrics (Y-Axis) ", padding=15)
        self.stats_frame.pack(fill="both", expand=True)
        
        # Metrics presentation slots
        self.avg_val = tk.StringVar(value="-")
        self.med_val = tk.StringVar(value="-")
        self.max_val = tk.StringVar(value="-")
        self.min_val = tk.StringVar(value="-")
        
        self.add_stat_row("Average (Mean):", self.avg_val, 0)
        self.add_stat_row("Median:", self.med_val, 1)
        self.add_stat_row("Maximum (Max):", self.max_val, 2)
        self.add_stat_row("Minimum (Min):", self.min_val, 3)

        # Right Panel (Interactive Plotting Canvas)
        self.right_panel = ttk.LabelFrame(self.main_split, text=" 4. Interactive Data Visualization Graph ")
        self.right_panel.pack(side="right", fill="both", expand=True)
        
        self.placeholder_lbl = ttk.Label(self.right_panel, text="Load data to visualize trend paths", font=("Arial", 11, "italic"))
        self.placeholder_lbl.pack(expand=True)

    def add_stat_row(self, label_text, var_target, row_idx):
        ttk.Label(self.stats_frame, text=label_text, font=("Arial", 10, "bold")).grid(row=row_idx, column=0, sticky="w", pady=8)
        ttk.Label(self.stats_frame, textvariable=var_target, font=("Courier", 11, "bold"), foreground="#1A73E8").grid(row=row_idx, column=1, sticky="e", pady=8, padx=(10, 0))
        self.stats_frame.grid_columnconfigure(1, weight=1)

    def load_excel_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx *.xls")])
        if not file_path:
            return
            
        try:
            # Parse Excel structure natively
            self.df = pd.read_excel(file_path)
            self.file_label.config(text=file_path.split("/")[-1])
            
            # Clear out legacy dropdown iterations if file is reloaded
            for widget in self.col_frame.winfo_children():
                widget.destroy()
                
            # Filter clean columns with numerical attributes
            numeric_cols = self.df.select_dtypes(include=['number']).columns.tolist()
            
            if len(numeric_cols) < 2:
                messagebox.showerror("Data Error", "Excel workbook must contain at least 2 columns filled with numerical records.")
                return
                
            # Initialize dropdown layout managers
            ttk.Label(self.col_frame, text="X-Axis Data Vector:").pack(side="left", padx=5)
            self.x_combo = ttk.Combobox(self.col_frame, values=numeric_cols, state="readonly", width=15)
            self.x_combo.pack(side="left", padx=5)
            self.x_combo.set(numeric_cols[0])
            
            ttk.Label(self.col_frame, text="Y-Axis Target Metric:").pack(side="left", padx=5)
            self.y_combo = ttk.Combobox(self.col_frame, values=numeric_cols, state="readonly", width=15)
            self.y_combo.pack(side="left", padx=5)
            self.y_combo.set(numeric_cols[1])
            
            self.x_combo.bind("<<ComboboxSelected>>", lambda e: self.reset_bounds_and_update())
            self.y_combo.bind("<<ComboboxSelected>>", lambda e: self.update_dashboard())
            
            self.reset_bounds_and_update()
            self.apply_btn.config(state="normal")
            
        except Exception as e:
            messagebox.showerror("Error Reading File", f"Failed to ingest sheet matrices:\n{str(e)}")

    def reset_bounds_and_update(self):
        if self.df is None: return
        self.x_col = self.x_combo.get()
        
        # Infer and seed default absolute min/max limits based on underlying data arrays
        abs_min = self.df[self.x_col].min()
        abs_max = self.df[self.x_col].max()
        
        self.xmin_entry.delete(0, tk.END)
        self.xmin_entry.insert(0, f"{abs_min:.2f}")
        self.xmax_entry.delete(0, tk.END)
        self.xmax_entry.insert(0, f"{abs_max:.2f}")
        
        self.update_dashboard()

    def update_dashboard(self):
        if self.df is None: return
        
        self.x_col = self.x_combo.get()
        self.y_col = self.y_combo.get()
        
        try:
            # Parse limits safely
            xmin = float(self.xmin_entry.get())
            xmax = float(self.xmax_entry.get())
        except ValueError:
            messagebox.showerror("Validation Error", "X-Axis boundary constraints must be explicit float values.")
            return
            
        if xmin >= xmax:
            messagebox.showerror("Validation Error", "Minimum X limit constraint cannot exceed or match Maximum X limit.")
            return
            
        # Isolate rows falling neatly within user-assigned constraints
        filtered_df = self.df[(self.df[self.x_col] >= xmin) & (self.df[self.x_col] <= xmax)].copy()
        
        # Sort values chronologically along X vector to keep plotted line segments linear
        filtered_df = filtered_df.sort_values(by=self.x_col)
        
        if filtered_df.empty:
            self.avg_val.set("No Data")
            self.med_val.set("No Data")
            self.max_val.set("No Data")
            self.min_val.set("No Data")
            # Clear visualization area if data falls out of window range
            if self.canvas: self.canvas.get_tk_widget().destroy()
            return

        # Compute data science summaries over isolated target Y dimension
        y_series = filtered_df[self.y_col]
        self.avg_val.set(f"{y_series.mean():.4f}")
        self.med_val.set(f"{y_series.median():.4f}") # Note: 'Mean' and 'Average' are interchangeable; Median satisfies the mathematical mean definition requested.
        self.max_val.set(f"{y_series.max():.4f}")
        self.min_val.set(f"{y_series.min():.4f}")
        
        # Regenerate visual plot architecture
        self.render_chart(filtered_df)

    def render_chart(self, target_data):
        # Scrub existing canvas frameworks clean
        if self.placeholder_lbl:
            self.placeholder_lbl.destroy()
            self.placeholder_lbl = None
            
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            
        # Configure a responsive Matplotlib configuration canvas
        fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
        ax.plot(target_data[self.x_col], target_data[self.y_col], marker='o', color='#1A73E8', linewidth=2, markersize=4, label=self.y_col)
        
        ax.set_xlabel(self.x_col, fontweight='bold', fontsize=9)
        ax.set_ylabel(self.y_col, fontweight='bold', fontsize=9)
        ax.set_title(f"{self.y_col} Behavior Profile over Selected Scope", fontsize=11, fontweight='bold', pad=10)
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend()
        
        fig.tight_layout()
        
        # Blit Matplotlib drawing onto Native Tkinter Frame geometry tree
        self.canvas = FigureCanvasTkAgg(fig, master=self.right_panel)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)
        plt.close(fig) # Prevent explicit dangling system resource leaks

if __name__ == "__main__":
    root_window = tk.Tk()
    app = ExcelAnalyzerApp(root_window)
    root_window.mainloop()