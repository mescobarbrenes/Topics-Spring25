# Topics-Spring25
Repository for **Topics In Computer Science: Web Application Development With Python** for Spring 2025.

# **Homework 3: MongoDB**

## **Query 1**
Problem 1: The first task assigned was to write a query to find all movies with runtime greater than 200 minutes in year 1983. The result should include a list of objects sorted by runtime increasing, and each object only has three fields: runtime, title, year.

Explanation of Problem 1 Query: First, we query the movies collection in the sample_mflix database. Then, we filter the movies to only include movies that came out in 1983, and with a runtime that is greater than 200 minutes. We make sure to include the runtime, title, and year fields, and to exclude the id field from the result. Finally, the results are sorted in increasing order of runtime.

![Query 1 Result](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_hw3/problem1_image_result.png?raw=true)

## **Query 2**
Problem 2: The second task assigned was to find all movies after the year 2014 with imdb rating greater than 9.

Explanation of Problem 2 Query: We query the movies collection in the sample_mflix database. Then, we filter to only include movies that came out after the year 2014. We make sure to include the runtime, title, and imdb rating, and to exclude the id field. Finally, it wasn't specified in the prompt, but to match the example result, I sorted the imdb ratings in descending order, so that the movie result with a rating of 9.4 appears over the movie result with a rating of 9.3.

![Query 2 Result](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_hw3/problem2_image_result.png?raw=true)