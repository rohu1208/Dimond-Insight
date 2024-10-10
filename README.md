# ** 💎 Diamond Insight 💎 - Diamond Price Prediction**

**Diamond Insight** is a machine learning project to predict diamond prices based on key features such as carat, cut, color, and clarity. This predictive model improves price estimation accuracy, supporting businesses in making data-driven decisions.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Setup](#project-setup)
- [Usage](#usage)
- [Data](#data)
- [Model Evaluation](#model-evaluation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Predicts diamond prices with improved accuracy.
- Utilizes a range of features including:
  - Carat
  - Cut
  - Color
  - Clarity
  - Depth
  - Table
  - X, Y, Z dimensions
- Machine learning model trained with real-world data.
## Architecture

The architecture of the Diamond Insight project consists of the following components:

1. **Data Ingestion**: 
   - Collect and clean the diamond dataset for analysis.

2. **Data Preprocessing**: 
   - Handle missing values, encode categorical features, and normalize numerical features.

3. **Model Training**: 
   - Train a machine learning model using various algorithms (e.g., Linear Regression, Decision Trees) on the processed data.

4. **Model Evaluation**: 
   - Assess model performance using metrics such as Mean Absolute Error (MAE) and R-squared.

5. **Prediction**: 
   - Use the trained model to make price predictions on new data.

6. **Visualization**: 
   - Visualize data and model performance using libraries like Matplotlib.
## Tech Stack

- **Programming Language**: Python
- **Machine Learning Libraries**: Scikit-learn,
- **Data Manipulation**: Pandas, NumPy
- **Data Visualization**: Matplotlib, Seaborn
- **Development Environment**: Jupyter Notebook  
   
## **Project Setup**

Follow these steps to set up and run the project on your local machine.

### Step 1: Clone the Repository
Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/rohu1208/Dimond-Insight
cd Dimond-Insight
```

### Step 2: Create and Activate a Virtual Environment 
Create a virtual environment to manage project dependencies. Run the following command:

```bash

python -m venv new_venv
```
Next, activate the virtual environment:
   On Windows:
   
   ```bash
   
   new_venv\Scripts\activate
   ```
   On macOS/Linux:
   
   ```bash
   
   source new_venv/bin/activate
   ```

### Step 3: Install Dependencies
With the virtual environment activated, install the required dependencies from the ``` requirements.txt``` file 

```
pip install -r requirements.txt
```

### Step 4 : Start the Application
```
python app2.py
```

### Step 5: Access the Web Application
```
http://127.0.0.1:5000/predict
```
# Model Evaluation
To evaluate the model's performance, you can use various metrics. Here’s how to calculate Mean -------Absolute Error (MAE) and R-squared:
Interpretation of Results
- Mean Absolute Error (MAE): This metric measures the average magnitude of the errors in a set of predictions, without considering their direction. A lower MAE indicates better model performance.

- R-squared: This value indicates how well the independent variables explain the variability of the dependent variable. An R-squared value closer to 1 indicates a better fit of the model to the data.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Contact
For any inquiries, please reach out to:

- author - Rohan Kaitake
-mail_id - rohan0070k@gmail.com
- GitHub: https://github.com/rohu1208
