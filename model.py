from typing import List
from surprise import Dataset, Reader
from surprise import SVD 
from surprise.model_selection import train_test_split
import pandas as pd
import numpy as np

def create_model() -> SVD:
    ratings_data = pd.read_csv("ratings.csv")

    min_rating = ratings_data.rating.min()
    max_rating = ratings_data.rating.max()
    
    reader = Reader(rating_scale=(min_rating, max_rating))
    data = Dataset.load_from_df(ratings_data[['userId', 'movieId', 'rating']], reader)

    trainset, testset = train_test_split(data, test_size=.20)
    
    svd = SVD(n_factors=50, n_epochs=20)
    
    svd.fit(trainset)
    return svd

def generate_recommendation(model: SVD, user_id: int, n_items: int = 10) -> List:
   ratings_data = pd.read_csv("ratings.csv")
   movies_data = pd.read_csv("movies.csv")
   movie_ids = ratings_data["movieId"].unique()
 
   movie_ids_user = ratings_data.loc[ratings_data["userId"] == user_id, "movieId"]
   movie_ids_to_pred = np.setdiff1d(movie_ids, movie_ids_user)
 
   test_set = [[user_id, movie_id, 4] for movie_id in movie_ids_to_pred]
 
   predictions = model.test(test_set)
   pred_ratings = np.array([pred.est for pred in predictions])
   print("Top {0} item recommendations for user {1}:".format(n_items, user_id))
   index_max = (-pred_ratings).argsort()[:n_items]
   print(index_max)
   print(movie_ids_to_pred)
   res = []
   for i in index_max:
       movie_id = movie_ids_to_pred[i]
       res.append(str(movies_data[movies_data["movieId"]==movie_id]["title"].values[0]) + " " + str(pred_ratings[i]))
   return res

model = create_model()
res = generate_recommendation(model, 23)
print(res)
