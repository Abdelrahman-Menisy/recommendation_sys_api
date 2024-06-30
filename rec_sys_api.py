from fastapi import FastAPI, HTTPException
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import random
import os

# Load models and data
with open('app/svd_model.pkl', 'rb') as f:
    algo = pickle.load(f)

with open('app/tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('app/recipe_matrix.pkl', 'rb') as f:
    recipe_matrix = pickle.load(f)

recipes = pd.read_pickle('app/recipes.pkl')

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Welcome to the food recommendation API"}

@app.get('/recommend/')
def recommend(Favorite_cuisines: str, Favorite_ingredients: str, Favorite_dishes: str, top_n: int = 10):
    try:
        # Combine user preferences into a single string
        user_pref = Favorite_cuisines + ' ' + Favorite_ingredients + ' ' + Favorite_dishes
        user_pref_vector = vectorizer.transform([user_pref])
        
        # Compute cosine similarity
        cosine_sim = cosine_similarity(user_pref_vector, recipe_matrix)
        recommendations = cosine_sim.argsort()[0][-top_n*2:][::-1]  # Get more recommendations than needed
        
        # Shuffle filtered recommendations and select top_n random recipes
        random.shuffle(recommendations)
        selected_recommendations = recommendations[:top_n]
        
        # Get recommended recipes
        recommended_recipes = recipes.iloc[selected_recommendations][['name']].to_dict(orient='records')
        
        return recommended_recipes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
