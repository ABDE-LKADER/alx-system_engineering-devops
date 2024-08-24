# 0x16. API Advanced

## Description

This project focuses on interacting with APIs, specifically the Reddit API. You'll learn how to:
- Read API documentation to find the endpoints you need
- Use APIs with pagination
- Parse JSON results from an API
- Make recursive API calls
- Sort dictionaries by value

By the end of this project, you will be able to confidently work with APIs in a variety of scenarios.

## Background Context

APIs are a common topic in technical interviews, ranging from simple endpoint queries to more complex recursive functions and data formatting tasks. The Reddit API is a great resource for practice, as it offers a wide range of endpoints and data to work with, many of which do not require authentication.

Understanding APIs is not only useful for interviews but also for practical applications in software development. 

## Resources

- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Query String](https://en.wikipedia.org/wiki/Query_string)

## Learning Objectives

At the end of this project, you should be able to:
- Read API documentation to find the endpoints you’re looking for
- Use an API with pagination
- Parse JSON results from an API
- Make recursive API calls
- Sort a dictionary by value

## Requirements

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
- Libraries imported in your Python files must be organized in alphabetical order.
- Your code should follow the PEP 8 style guide.
- All your files must be executable.
- All modules should have documentation.

## Tasks

### 0. How many subs?

Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

- **Prototype:** `def number_of_subscribers(subreddit)`
- If not a valid subreddit, return `0`.

### 1. Top Ten

Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

- **Prototype:** `def top_ten(subreddit)`
- If not a valid subreddit, print `None`.

### 2. Recurse it!

Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return `None`.

- **Prototype:** `def recurse(subreddit, hot_list=[])`
- If not a valid subreddit, return `None`.

### 3. Count it! (Advanced)

Write a recursive function that queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of given keywords (case-insensitive).

- **Prototype:** `def count_words(subreddit, word_list)`
- Results should be printed in descending order, by the count, and if the count is the same for separate keywords, they should then be sorted alphabetically (ascending, from A to Z).

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/alx-system_engineering-devops.git
   cd alx-system_engineering-devops/0x16-api_advanced
