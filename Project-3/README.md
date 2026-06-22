# Tech Stack Recommender
> An AI-powered career recommendation engine built with Content-Based Filtering

---

## Overview

Finding the right career path in tech can be overwhelming. This project solves that by building a personalized recommendation system that maps a user's skills to the most relevant job roles — using the same algorithmic logic that powers platforms like Netflix and Amazon.

Given a set of user skills as input, the system computes similarity scores against a curated dataset of tech job profiles and returns the top 3 best-fit career recommendations ranked by relevance.

---

## Demo

```
Input:  python, machine learning, sql

Output:
  #1  Data Scientist      ████████████░░░░░░░░  57.1%
  #2  ML Engineer         ██████████░░░░░░░░░░  51.3%
  #3  Data Analyst        ████░░░░░░░░░░░░░░░░  20.1%
```

---

## How It Works

The system follows a clean 4-step pipeline:

**1. Ingestion** — Accepts a minimum of 3 user skills as comma-separated input.

**2. Vectorization** — Converts all skills (both user input and job role datasets) into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency). This ensures rare, specific skills carry more weight than common ones.

**3. Scoring** — Calculates Cosine Similarity between the user vector and each job role vector. Cosine similarity measures the angular alignment between two vectors, making it scale-invariant — perfect for comparing skill profiles of different sizes.

**4. Ranking & Filtering** — Sorts all roles by similarity score in descending order and returns the Top-3 matches to prevent information overload.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Core language |
| scikit-learn | TF-IDF Vectorization + Cosine Similarity |

---

## Project Structure

```
Project-3/
├── tech_stack_recommender.py   # Core recommendation engine
└── README.md                   # Project documentation
```

---

## Setup & Usage

**Install dependency:**
```bash
pip install scikit-learn
```

**Run the program:**
```bash
python tech_stack_recommender.py
```

**Enter your skills when prompted:**
```
Tumhari skills (comma se alag karo): python, docker, aws
```

---

## Supported Job Roles

The dataset currently includes 8 tech career profiles:

- Data Scientist
- ML Engineer
- Data Analyst
- Backend Developer
- DevOps Engineer
- Cloud Architect
- Cybersecurity Analyst
- Frontend Developer

---

## Key Concepts

**Content-Based Filtering** — Recommendations are driven purely by item attributes (skill tags), with no dependency on other users' data. This eliminates the cold-start problem for new items.

**TF-IDF Weighting** — Penalizes generic, high-frequency terms and rewards specific, descriptive skills. A skill like "neural networks" carries more signal than "software."

**Cosine Similarity** — Measures orientation between vectors rather than magnitude, making it the industry standard for text-based similarity matching.

---

## Author

**Faraz Ul Zaman**
AI Engineering Intern — DecodeLabs
Batch 2026 | Project 3: AI Recommendation Logic
