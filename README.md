# 🌦️ Weather Chatbot

A Rasa-powered chatbot that provides weather updates based on user queries. This bot can respond to inputs like "What's the weather in Delhi today?" and provide real-time weather information using an integrated weather API.

---

## 🧠 Features

- Built using Rasa framework
- Integrates with a weather API
- Supports intents like:
  - Asking about weather in a city
  - Greetings and goodbyes
- Can be extended for more features like forecasts, alerts, etc.

---

## 📁 Project Structure

.
├── actions/ # Custom action code (e.g., API calls)
├── data/ # NLU training data (intents, examples)
├── models/ # Trained Rasa models
├── tests/ # Test stories for validation
├── .rasa/cache/ # Rasa internal cache (can be ignored)
├── config.yml # Rasa pipeline and policies
├── credentials.yml # Connectors (e.g., REST, Slack)
├── domain.yml # Intents, responses, entities, slots, actions
├── endpoints.yml # Endpoint configs for actions and models


---

![Chatbot Output](./SS/chatbot%20output.jpg)


---

👨‍💻 Author
Anubhav Choudhary

LinkedIn: [LinkedIn](https://www.linkedin.com/in/anubhav-choudhary-35b8ab254/) | GitHub [GitHub](https://github.com/ANUBHAV0112)
