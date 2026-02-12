# Association Rule Based Recommendation System

## Overview
This project implements a product recommendation system for an e-commerce platform ("Samazon Store") using **Association Rule Learning**. By analyzing transaction history (Market Basket Analysis), the system identifies strong relationships between products—specifically, which items are frequently bought together.

These insights are used to power a "You May Also Like" feature, suggesting relevant add-on products to users based on their current selection, thereby increasing cross-selling opportunities and average order value.

## Core Concept: Association Rule Learning
Association Rule Learning is a rule-based machine learning method for discovering interesting relations between variables in large databases. It is intended to identify strong rules discovered in databases using some measures of interestingness.

In this project, we use the **Apriori Algorithm** to mine these rules. The algorithm identifies frequent itemsets in the dataset and then generates association rules from them.

A rule implies that if a customer buys **Item A** (Left Hand Side), they are likely to buy **Item B** (Right Hand Side).

## Training Process (`train.py`)
The training pipeline consists of three main steps:

1.  **Data Preprocessing**:
    - The raw transaction dataset (`Market_Basket_Optimisation.csv`) is converted into a list of transactions (list of lists).
    - Each transaction represents a customer's basket.

2.  **Model Training (Apriori Algorithm)**:
    - The `apyori` library is used to find frequent itemsets and generate rules based on specified thresholds (support, confidence, lift).

3.  **Rule Extraction & Export**:
    - The raw output from the Apriori algorithm is parsed to extract the Antecedent (LHS), Consequent (RHS), Support, Confidence, and Lift.
    - These rules are saved to `rules.csv`, which serves as the knowledge base for the backend application.

## Hyperparameters & Business Configuration
The behavior of the recommendation engine is heavily dependent on the hyperparameters used in the Apriori algorithm. These can be tuned in `train.py` to align with business requirements.

### Key Parameters:

*   **`min_support`** (Default: `0.003`):
    - **Definition**: The frequency of the itemset appearing in the database.
    - **Calculation**: (Transactions containing Item A & B) / (Total Transactions).
    - **Business Impact**: Lowering this value includes less popular items in the analysis (finding niche rules). Increasing it ensures rules are only generated for high-volume products.
    - *Example*: `0.003` means an item must appear in at least ~0.3% of transactions (approx. 3 times a day in a week of 7500 transactions).

*   **`min_confidence`** (Default: `0.2`):
    - **Definition**: The likelihood that Item B is purchased when Item A is purchased.
    - **Calculation**: (Transactions containing A & B) / (Transactions containing A).
    - **Business Impact**: This measures the reliability of the rule. A higher value (e.g., 0.8) means a very strong correlation but yields fewer rules. A lower value (e.g., 0.2) catches more potential associations but may include weaker links.

*   **`min_lift`** (Default: `3`):
    - **Definition**: The ratio of the observed support to that expected if A and B were independent.
    - **Business Impact**:
        - `Lift > 1`: Items are likely bought together (Positive correlation).
        - `Lift = 1`: No relation (Independent).
        - `Lift < 1`: Items are unlikely to be bought together (Negative correlation).
    - *Configuration*: We use a minimum lift of `3` to ensure we only recommend products with a **strong** positive correlation, filtering out coincidental purchases.

*   **`min_length` / `max_length`** (Set to `2`):
    - **Definition**: The number of items in the rule (LHS + RHS).
    - **Business Impact**: We restrict this to `2` to generate simple "Buy X, Get Y" pairs, which are easier to display and understand in a simple recommendation widget. For bundle recommendations (e.g., "Buy X & Y, Get Z"), these values can be increased.

## Backend Architecture (`app.py`)
The backend is built with **FastAPI** to serve the application and recommendation logic.

1.  **Rule Loading**:
    - On startup, the application reads `rules.csv`.
    - It builds a dictionary mapping products (LHS) to their recommended counterparts (RHS).

2.  **Product Data**:
    - Product details (Name, Price, Image, Description) are loaded from `products.json`.

3.  **Recommendation Logic**:
    - When a user visits a product page (`/product/{id}`):
        1.  The system checks if the current product has any associated rules in the loaded dictionary.
        2.  If associations exist (e.g., *Current Product* -> *Recommended Product*), the recommended products are prioritized in the "You May Also Like" section.
        3.  Remaining slots in the recommendation grid (total 4) are filled with random products to ensure the UI always looks complete.

## Setup & Usage

### Prerequisites
- Python 3.x
- Pandas, Numpy, Apyori, FastAPI, Uvicorn

### 1. Train the Model
Run the training script to generate new rules based on the dataset.
```bash
python train.py
```
This will generate/update `rules.csv`.

### 2. Run the Application
Start the FastAPI server.
```bash
python app.py
```
Access the application at `http://127.0.0.1:8000`.

## File Structure
- `train.py`: Logic for training the Apriori model and generating rules.
- `app.py`: FastAPI backend application.
- `rules.csv`: Output file containing the generated association rules.
- `products.json`: Database of product details (Mock data mapped from dataset items).
- `templates/`: HTML templates for the UI.
- `static/`: CSS and JavaScript files.

## Important Note
This project is for **educational purposes only**. The data used is a sample market basket dataset and is not intended for commercial use. The product images and descriptions are for demonstration and may not reflect real products.

## Thanks
Thank you for exploring this Association Rule Based Recommendation System! We hope it provides a clear understanding of how machine learning can drive business value in e-commerce.
