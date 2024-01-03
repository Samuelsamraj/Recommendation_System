#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install neattext


# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import neattext.functions as nfx
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[3]:


warnings.filterwarnings('ignore')


# In[4]:


data = pd.read_csv("udemy_courses.csv")


# In[5]:


data.head()


# In[6]:


data.tail()


# In[7]:


print('total number of rows in my data : ', data.shape[0])
print('total number of columns in my data : ', data.shape[1])


# In[8]:


data.info()


# In[9]:


data.isnull().sum()


# In[10]:


data.isnull().sum().sum()


# In[11]:


data.duplicated().any()


# In[12]:


data[data.duplicated()]


# In[13]:


data = data.drop_duplicates()


# In[14]:


data.duplicated().any()


# In[15]:


data.columns


# *Popularity Based Recommendation System*

# In[16]:


def popularity_based_recommendation(df,top_n=5):
    # Calculate popularity score for each course
    data['popularity_score'] = 0.6 * data['num_subscribers'] + 0.4 * data['num_reviews']

    # Sort courses by popularity score in descending order
    df_sorted = data.sort_values(by='popularity_score', ascending=False)

    # Return the recommended courses (course titles and popularity scores)
    recommended_courses = df_sorted[['course_title', 'popularity_score']].head(top_n)

    return recommended_courses


# In[17]:


data


# In[18]:


popularity_based_recommendation(data)


# **Content-Based Recommendation System**

# In[19]:


data['course_title'] = data['course_title'].apply(nfx.remove_stopwords)
data['course_title']  =data['course_title'].apply(nfx.remove_special_characters)


# In[20]:


data.sample(5)


# In[21]:


data['title_subject']  =data['course_title'] +' '+data['subject']


# In[22]:


cv = CountVectorizer(max_features=3000)
vectors = cv.fit_transform(data['title_subject']).toarray()
vectors[0]


# In[25]:


len(cv.get_feature_names_out())


# In[27]:


from sklearn.metrics.pairwise import cosine_similarity


# In[28]:


similarity = cosine_similarity(vectors)


# In[30]:


sorted(list(enumerate(similarity[0])),reverse=True,key=lambda x:x[1])[1:6]



# In[31]:


def recommend(course):
    # let's featch the index
    course_index = data[data['course_title']==course].index[0]
    distances = similarity[course_index]
    courses_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    for i in courses_list:
        print(data.iloc[i[0]]['course_title'])


# In[32]:


#recommend("know HTML Learn HTML Basics")
recommend("know HTML Learn HTML Basics")


# In[33]:


data.iloc[39]['course_title']


# In[34]:


#sorted(similarity[0],reverse=True)
import pickle


# In[35]:


#pickle.dump(data.to_dict(),open('course_dict.pkl','wb'))
pickle.dump(data,open('course_dict.pkl','wb'))


# In[36]:


pickle.dump(similarity,open('similarity.pkl','wb'))


# In[38]:


import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# Assume 'data', 'similarity' are defined elsewhere

# Define the popularity-based recommendation function
def popularity_based_recommendation(df, top_n=5):
    df['popularity_score'] = 0.6 * df['num_subscribers'] + 0.4 * df['num_reviews']
    df_sorted = df.sort_values(by='popularity_score', ascending=False)
    recommended_courses = df_sorted[['course_title', 'popularity_score']].head(top_n)
    return recommended_courses

# Define the recommend function
def recommend(course):
    try:
        course_index = data[data['course_title'] == course].index[0]
        distances = similarity[course_index]
        courses_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommended_courses = [data.iloc[i[0]]['course_title'] for i in courses_list]
        return recommended_courses
    except IndexError:
        messagebox.showerror("Error", f"Course '{course}' not found.")

# Event handler for the "Recommend" button
def recommend_button_click():
    course_title = course_var.get()
    recommended_courses = recommend(course_title)
    if recommended_courses:
        popularity_label.pack_forget()
        result_label.config(text="Recommended Courses:\n" + '\n'.join(recommended_courses))

# Create the main application window
root = tk.Tk()
root.title("Course Recommender")
root.geometry("400x300")

# Change font and color
font_style = ("Arial", 12)
label_color = "blue"
heading_color="red"
button_color = "green"
result_label_color = "black"

# Create and place GUI elements
label = tk.Label(root, text="Select Course:", font=font_style, fg=label_color)
label.pack(pady=10)

course_titles = data['course_title'].tolist()
course_var = tk.StringVar(value=course_titles[0])
course_dropdown = ttk.Combobox(root, textvariable=course_var, values=course_titles, width=40, font=font_style)
course_dropdown.pack(pady=5)

popularity_recommendations = popularity_based_recommendation(data, top_n=5)
popularity_label = tk.Label(root, text="Popularity-based Recommendations:\n" + popularity_recommendations.to_string(index=False),
                             font=font_style, fg=label_color)
popularity_label.pack()

recommend_button = tk.Button(root, text="Recommend", command=recommend_button_click, width=20, font=font_style, fg=button_color)
recommend_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=350, font=font_style, fg=result_label_color)
result_label.pack()

root.mainloop()

