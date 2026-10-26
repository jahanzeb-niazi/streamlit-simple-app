# Task 1: Streamlit-Based Exploratory Data Analysis Interface

## Objective

Develop and deploy an interactive GUI system for exploratory data analysis (EDA) using Streamlit. The system should facilitate dataset ingestion, metadata inspection, and primary visual pattern recognition, providing end-users with a structured interface for initial data exploration.

## Implementation Requirements

### 1. Dataset Ingestion & Metadata Inspection

- **File Upload Interface:** Implement a secure file upload module supporting CSV format. Validate that the uploaded file is correctly formatted.
- **Dataset Overview Panel:** Display key metadata, including:
  - Number of rows and columns.
  - Column-wise data types.
  - Count of missing values per attribute.
  - Basic statistical summary for numerical attributes (mean, median, min, max).

**Note:** Test your implementation using the `titanic.csv` dataset.

### 2. Attribute Selection & Classification

- **Dynamic Feature Selector:** Provide a dropdown to select a single column for analysis.
- **Automated Attribute Typing:** Detect whether the selected column is numerical or categorical, and update the visualization module accordingly.

### 3. Visualization Module

#### Conditional Rendering

- **Numerical Attributes:** Generate a histogram depicting the value distribution. Include axis labels and a descriptive title.
- **Categorical Attributes:** Generate a bar chart representing frequency counts of unique values. Include axis labels and percentage display (optional).
- Ensure that visualizations are updated dynamically upon attribute selection.

### 4. Interface Layout & Organization

- **Sidebar Panel:** Include all interactive controls, including file upload and column selection.

- **Main Content Area:**
  - **Top Section:** Dataset preview (first 5 rows) and metadata display.
  - **Bottom Section:** Conditional visualization canvas.