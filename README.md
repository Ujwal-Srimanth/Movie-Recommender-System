#  Movie Recommendation System
This is a simple movie recommendation system built using cosine similarity to suggest the top 5 movie recommendations based on a user's input. The app is developed using Streamlit and utilizes pickle files to store pre-processed data and models for efficient loading.

# Features
Cosine Similarity: The recommendation system uses cosine similarity to calculate the similarity between movies based on their features.
Top 5 Recommendations: For any given movie, the system recommends the top 5 most similar movies.
Streamlit Interface: The web application is built using Streamlit, providing a simple and interactive user interface.
Pre-loaded Data: Movie data and trained similarity models are stored in pickle files to allow quick access and predictions.
How it works
Data Preprocessing:

Movies are represented using feature vectors, where features can include genres, keywords, and more.
Cosine similarity is calculated between these vectors to determine how similar any two movies are.
Pickle Files:

The feature matrix and the similarity model are saved in pickle files for efficient storage and retrieval.
These files are loaded when the app starts, allowing the recommendation system to make fast predictions.
Recommendation Engine:

When a user selects or inputs a movie, the app retrieves the corresponding feature vector.
It computes the cosine similarity between this vector and the rest of the movies in the dataset.
The system then ranks the movies by similarity and returns the top 5 movies as recommendations.
