
# GPT Chatbot in Python 🤖

A simple chatbot built with **Python** and **Flask**, using the **OpenAI GPT-3.5 API** to generate smart responses. The system is scalable, customizable by context (company, product, audience) and allows contextual and natural responses via AI. Fully integrated via REST API, with the possibility of training with company documents or FAQs.

![Chatbot Demo](./assets/demo.png)

---

## 🚀 Project Goal

This project shows how to:

- Connect the OpenAI GPT-3.5 API to a backend.
- Create a Flask API for chatting with the bot.
- Build a simple and clean chatbot backend that can be expanded later.

---

## ⚙️ Technologies

- Python 3.10+
- Flask
- OpenAI API (GPT-3.5)

---

## 📁 Project Structure

```
gpt-chatbot-python/
│
├── app.py               
├── chatbot.py           
├── .env                 
├── requirements.txt     
├── README.md
└── assets/
```

---

## 🛠️ How to Use

> ⚠️ This project is still in development.

1. Clone the repository:

```
git clone https://github.com/yourusername/gpt-chatbot-python.git
cd gpt-chatbot-python
```

2. (Optional) Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Install the requirements:

```
pip install -r requirements.txt
```

4. Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=sk-your-api-key-here
```

5. Run the Flask app:

```
python app.py
```

6. Go to `http://localhost:5000` and send a POST request to `/chat` with a message.

---

## 💬 Example 

POST to `/chat` with:

```json
{
  "message": "What is the capital of France?"
}
```

Response:

```json
{
  "response": "The capital of France is Paris."
}
```

---

## 📌 Roadmap

- [x] Initial project structure
- [x] Flask API setup
- [x] GPT-3.5 integration
- [ ] Add Dockerfile
- [ ] Public demo 

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Made by **Codenaia**  
• [GitHub](https://github.com/CodeNaIa)

---

> This is a personal portfolio project. Feel free to clone, suggest ideas, or use it as a base for your own chatbot.
