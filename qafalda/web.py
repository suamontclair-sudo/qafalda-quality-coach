import os
import random
from flask import Flask, render_template, request, session

from .app import QAfalda
from .knowledge import KNOWLEDGE

CTFL_SUGGESTIONS = [
    "Fundamentos de Teste",
    "Técnicas de Teste",
    "Gestão de Testes",
    "Ferramentas de Teste",
    "Automação de Testes",
    "Qualidade de Software",
]

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "templates"),
    static_folder=os.path.join(os.path.dirname(__file__), "static"),
)
app.secret_key = 'qafalda-secret-key-2024'
bot = QAfalda()


@app.route("/", methods=["GET", "POST"])
def index():
    if 'messages' not in session:
        session['messages'] = []
    if 'suggestions' not in session:
        session['suggestions'] = []

    if request.method == "POST":
        user_text = request.form.get("question", "").strip()
        if user_text:
            session['messages'].append({'role': 'user', 'content': user_text})
            answer = bot.respond(user_text)
            session['messages'].append({'role': 'assistant', 'content': answer})
            session['messages'] = session['messages'][-20:]
            session.modified = True

    return render_template(
        "index.html",
        messages=session.get('messages', []),
        suggestions=CTFL_SUGGESTIONS,
    )


@app.route("/temas")
def temas():
    return render_template("temas.html", knowledge=KNOWLEDGE)


@app.route("/dicas")
def dicas():
    dica = random.choice(KNOWLEDGE)
    return render_template("dicas.html", dica=dica)


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        selected = request.form.get("answer")
        correct = request.form.get("correct")
        question = request.form.get("question")
        feedback = "Correto! Parabéns." if selected == correct else f"Incorreto. A resposta certa é: {correct}"
        return render_template("quiz.html", feedback=feedback, question=question)

    # Generate quiz question
    item = random.choice(KNOWLEDGE)
    question = item["question"]
    correct_answer = item["answer"]
    options = [correct_answer]

    # Add 3 wrong options from other items
    other_answers = [k["answer"] for k in KNOWLEDGE if k != item]
    options.extend(random.sample(other_answers, min(3, len(other_answers))))
    random.shuffle(options)

    return render_template("quiz.html", question=question, options=options, correct=correct_answer)


def run_web() -> None:
    app.run(host="0.0.0.0", port=5000)
