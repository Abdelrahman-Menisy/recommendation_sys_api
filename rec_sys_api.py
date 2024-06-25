from fastapi import FastAPI, HTTPException
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import random  # Import random module

# Load models and data
with open('svd_model.pkl', 'rb') as f:
    algo = pickle.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('recipe_matrix.pkl', 'rb') as f:
    recipe_matrix = pickle.load(f)

recipes = pd.read_pickle('recipes.pkl')

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Welcome to the food recommendation API"}

@app.get('/recommend/')
def recommend(Favorite_cuisines: str, Favorite_ingredients: str, Favorite_dishes: str, Disliked_ingredients: str, top_n: int = 10):
    try:
        # Combine user preferences into a single string
        user_pref = Favorite_cuisines + ' ' + Favorite_ingredients + ' ' + Favorite_dishes
        user_pref_vector = vectorizer.transform([user_pref])
        
        # Compute cosine similarity
        cosine_sim = cosine_similarity(user_pref_vector, recipe_matrix)
        recommendations = cosine_sim.argsort()[0][-top_n*2:][::-1]  # Get more recommendations than needed
        
        # Convert disliked ingredients to a list
        disliked_ingredients_list = Disliked_ingredients.split()
        
        # Filter out recipes containing disliked ingredients
        filtered_recommendations = []
        for idx in recommendations:
            ingredients = recipes.iloc[idx]['ingredients'].split()
            combined_features = recipes.iloc[idx]['combined_features']
            
            # Check if any disliked ingredient is in the combined_features
            if not any(disliked in combined_features for disliked in disliked_ingredients_list):
                filtered_recommendations.append(idx)
                if len(filtered_recommendations) >= top_n:
                    break
        
        # Shuffle filtered recommendations and select top_n random recipes
        random.shuffle(filtered_recommendations)
        selected_recommendations = filtered_recommendations[:top_n]
        
        # Get recommended recipes
        recommended_recipes = recipes.iloc[selected_recommendations][['name', 'combined_features']].to_dict(orient='records')
        return recommended_recipes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("rec_sys_api:app", host='127.0.0.1', port=8000, reload=True)
