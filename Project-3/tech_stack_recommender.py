# ============================================================
#  Project 3: AI Recommendation System
#  DecodeLabs Industrial Training - Batch 2026
#  Tech Stack Recommender (Content-Based Filtering)
# ============================================================

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


job_roles = {
    "Data Scientist": [
        "python", "machine learning", "sql", "statistics",
        "data analysis", "tensorflow", "pandas", "numpy"
    ],
    "ML Engineer": [
        "python", "machine learning", "tensorflow", "pytorch",
        "deep learning", "algorithms", "model deployment", "docker"
    ],
    "Data Analyst": [
        "sql", "excel", "data analysis", "python", "tableau",
        "statistics", "reporting", "power bi"
    ],
    "Backend Developer": [
        "python", "java", "sql", "apis", "databases",
        "docker", "git", "rest api", "node js"
    ],
    "DevOps Engineer": [
        "docker", "kubernetes", "aws", "linux", "git",
        "ci cd", "automation", "cloud computing", "terraform"
    ],
    "Cloud Architect": [
        "aws", "azure", "cloud computing", "networking",
        "docker", "kubernetes", "automation", "security"
    ],
    "Cybersecurity Analyst": [
        "networking", "linux", "python", "security",
        "ethical hacking", "firewalls", "encryption", "risk analysis"
    ],
    "Frontend Developer": [
        "javascript", "html", "css", "react", "vue",
        "ui ux", "typescript", "responsive design"
    ]
}


def build_skill_vectors(job_roles):
    role_names = list(job_roles.keys())
    role_texts = [" ".join(skills) for skills in job_roles.values()]
    
    vectorizer = TfidfVectorizer()
    
    role_matrix = vectorizer.fit_transform(role_texts)
    
    return vectorizer, role_matrix, role_names


def get_similarity_scores(user_skills, vectorizer, role_matrix):
    user_text = " ".join(user_skills)
    
    user_vector = vectorizer.transform([user_text])
    
    scores = cosine_similarity(user_vector, role_matrix)[0]
    
    return scores


def recommend_jobs(user_skills, job_roles, top_n=3):
    vectorizer, role_matrix, role_names = build_skill_vectors(job_roles)
    
    scores = get_similarity_scores(user_skills, vectorizer, role_matrix)
    
    scored_roles = list(zip(role_names, scores))
    
    scored_roles.sort(key=lambda x: x[1], reverse=True)
    
    top_results = scored_roles[:top_n]
    
    return top_results


def main():
    print("=" * 55)
    print("   DecodeLabs - Tech Stack Recommender")
    print("   Project 3: AI Recommendation Logic")
    print("=" * 55)
    print()
    
    # ---- USER INPUT ----
    print("Apni skills batao (minimum 3 skills):")
    print("Example: python, machine learning, sql")
    print()

    skill_input = input("Tumhari skills (comma se alag karo): ")
    user_skills = [skill.strip().lower() for skill in skill_input.split(",")]
    
    if len(user_skills) < 3:
        print("\nError: Kam se kam 3 skills zaroor batao!")
        return
    
    print(f"\nTumhari skills: {user_skills}")
    print("\nRecommendations dhundh raha hun...")
    print("-" * 55)
    
    # ---- RECOMMENDATION ----
    results = recommend_jobs(user_skills, job_roles, top_n=3)
    
    # ---- OUTPUT ----
    print("\nTumhare liye Top 3 Career Recommendations:\n")
    
    for rank, (job, score) in enumerate(results, 1):
        percentage = round(score * 100, 1)
        
        bar_length = int(score * 20)
        bar = "█" * bar_length + "░" * (20 - bar_length)
        
        print(f"  #{rank}  {job}")
        print(f"       Match: [{bar}] {percentage}%")
        print()
    
    print("=" * 55)
    print("Tip: Zyada skills add karo for better results!")

if __name__ == "__main__":
    main()
