# Recommendation_System

# Udemy Course Recommender

This project implements two recommendation systems: Popularity-Based and Content-Based. The Popularity-Based system calculates a popularity score for each course, while the Content-Based system uses natural language processing techniques to recommend courses based on similarity.

# Data Preprocessing
-- Load the dataset from "udemy_courses.csv".
-- Check for null values and remove duplicates.

# Popularity-Based Recommendation System
-- Calculate popularity score for each course.
-- Sort courses by popularity score.
-- Display top recommended courses based on popularity.

# Content-Based Recommendation System
-- Clean course titles by removing stopwords and special characters.
-- Create a combined feature of course titles and subjects.
-- Use CountVectorizer to convert text data to vectors.
-- Calculate cosine similarity between course vectors.
-- Implement a function to recommend similar courses.

# GUI Application
-- Create a Tkinter-based GUI for user interaction.
-- Select a course from the dropdown menu and click the "Recommend" button.
-- Display recommended courses based on both popularity and content.

# Dependencies
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
Tkinter (for GUI)
