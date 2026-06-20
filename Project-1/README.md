# 🤖 DecodeBot – Rule-Based AI Chatbot

**Project 1 | DecodeLabs AI Internship – Batch 2026**

## 📌 Overview

DecodeBot is a simple **rule-based chatbot** built in Python as the foundational project of the DecodeLabs AI Internship. The goal of this project is to demonstrate core programming concepts — control flow, decision-making logic, and basic AI principles — before moving on to more advanced, generative AI systems.

Unlike modern AI chatbots that use machine learning, DecodeBot relies entirely on **predefined rules and pattern matching**, making it fully transparent, predictable, and easy to debug — a true "white box" system.

## ✨ Features

- **Continuous Conversation Loop** – Runs indefinitely until the user chooses to exit.
- **Input Sanitization** – Handles different cases and extra spaces (e.g., "HELLO ", "hello", " Hello" all work the same).
- **Dictionary-Based Knowledge Base** – Stores 10+ predefined intents and responses for fast (O(1)) lookups.
- **Fallback Response** – Politely informs the user when it doesn't understand an input.
- **Nested Conditional Logic**:
  - Detects the word **"time"** anywhere in the input and replies with the current time.
  - Detects **"my name is..."** and personalizes its response using the user's name.
  - Detects AI-related questions even with extra wording (e.g., "what is AI can you tell me").
- **Help Command** – Typing `help` shows the user a list of things they can ask.
- **Multiple Exit Commands** – Accepts `exit`, `quit`, or `bye` to end the chat gracefully.

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries Used:** `datetime` (built-in)
- **Core Concepts:** Loops, conditionals, dictionaries, string methods

## 🚀 How to Run

1. Make sure Python 3 is installed on your system.
2. Download or clone this project folder.
3. Open a terminal in the project directory.
4. Run the following command:

   ```bash
   python rule_based_chatbot.py
   ```

5. Start chatting! Type `help` to see example commands, or `exit` / `quit` / `bye` to end the conversation.

## 💬 Example Conversation

```
Bot: Hello! I am DecodeBot 🤖
Bot: I'm a rule-based assistant created at DecodeLabs.
Bot: Type 'exit', 'quit', or 'bye' anytime to end the chat.
==================================================
You: hello
Bot: Hi there! How can I help you today?
You: my name is Faraz
Bot: Nice to meet you, Faraz! How can I help you?
You: what is the time
Bot: The current time is 01:30 PM.
You: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!
You: bye
Bot: Goodbye! Have a great day. 👋
```

## 📂 Project Structure

```
Project-1/
│
├── rule_based_chatbot.py   # Main chatbot program
└── README.md               # Project documentation
```

## 🧠 Key Learnings

This project reinforced the importance of:

- **Control flow and decision-making logic** as the foundation of any intelligent system.
- **Dictionaries over if-elif ladders** for scalable, efficient lookups.
- The concept of **deterministic "guardrails"** — the same principles used in real-world production AI systems to keep generative models safe and reliable.

## 🔮 Future Improvements

- Expand the knowledge base with more intents.
- Add support for synonyms (e.g., "hiya", "good morning" → greeting).
- Integrate this rule-based layer as a guardrail in front of a generative AI model (Project 2+).

---

**Author:** Faraz
**Internship:** DecodeLabs AI Internship – Batch 2026
**Project:** 1 of N – Rule-Based AI Chatbot
