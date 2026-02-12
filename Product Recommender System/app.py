from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import uvicorn
import json
import os
import pandas as pd
import random

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Load products
def load_products():
    with open('products.json', 'r') as f:
        return json.load(f)

# Load Rules
rules = {}
try:
    # Read CSV
    df_rules = pd.read_csv('rules.csv')
    
    # Clean column names logic (removing spaces if any)
    # The file has header: ,Left Hand Side,Right Hand Side,Support,Confidence,Lift
    # Pandas might read the first empty column as Unnamed: 0 if not specified.
    
    # Let's inspect columns dynamically to be safe
    lhs_col = None
    rhs_col = None
    
    for col in df_rules.columns:
        if "Left Hand Side" in col:
            lhs_col = col
        if "Right Hand Side" in col:
            rhs_col = col
            
    if lhs_col and rhs_col:
        for _, row in df_rules.iterrows():
            lhs = str(row[lhs_col]).strip().lower()
            rhs = str(row[rhs_col]).strip().lower()
            
            if lhs not in rules:
                rules[lhs] = []
            # Avoid duplicates
            if rhs not in rules[lhs]:
                rules[lhs].append(rhs)
    else:
        print("Could not find LHS/RHS columns in rules.csv")
        
except Exception as e:
    print(f"Error loading rules.csv: {e}")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/product/{product_id}", response_class=HTMLResponse)
async def product_detail(request: Request, product_id: int):
    products = load_products()
    product = next((p for p in products if p['id'] == product_id), None)
    
    if not product:
        return RedirectResponse("/")

    # Recommendation Logic
    recommendations = []
    prod_name_lower = product['name'].strip().lower()
    
    # 1. Check rules for this product (LHS -> RHS)
    # We look for rules where current product is LHS
    rule_recommendations_names = rules.get(prod_name_lower, [])
    
    # Find these recommended products in our product list
    for rec_name in rule_recommendations_names:
        # Try to find product with this name (case insensitive)
        rec_product = next((p for p in products if p['name'].strip().lower() == rec_name), None)
        if rec_product:
            # Create a copy to not mutate the original cached list if we were caching, 
            # though here we load fresh every time so it's fine.
            # But better safe to copy if modifying.
            rec_p_copy = rec_product.copy()
            rec_p_copy['is_recommended'] = True  # Flag for UI highlight
            recommendations.append(rec_p_copy)
    
    # 2. Fill remaining slots with random products
    needed = 4 - len(recommendations)
    if needed > 0:
        # Exclude current product and already recommended ones
        excluded_ids = {product['id']} | {r['id'] for r in recommendations}
        candidates = [p for p in products if p['id'] not in excluded_ids]
        
        # Shuffle and pick
        random.shuffle(candidates)
        recommendations.extend(candidates[:needed])
    
    # Trim to exactly 4 if we somehow got more (e.g. many rules)
    recommendations = recommendations[:4]

    return templates.TemplateResponse("product.html", {
        "request": request, 
        "product": product,
        "recommendations": recommendations
    })

@app.get("/api/products")
async def get_products(limit: int = None):
    products = load_products()
    if limit:
        return products[:limit]
    return products

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
