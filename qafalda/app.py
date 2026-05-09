import random
from typing import Optional

from .knowledge import KNOWLEDGE, find_best_knowledge, normalize_text

GREETINGS = [
    "Olá QA! Que bom te ver aqui! Qual tema vamos explorar hoje?",
    "Oi QA! 😊 Estou animada para conversar sobre qualidade de software. O que você quer saber?",
    "E aí QA! Vamos mergulhar juntos no mundo dos testes? Me diga o que te interessa!",
]

THANK_YOU = [
    "Fico tão feliz em poder ajudar, QA! Continue testando com dedicação.",
    "Que bom que consegui esclarecer suas dúvidas, QA. Estou sempre aqui!",
    "Foi um prazer ajudar, QA! Você está no caminho certo para se tornar um excelente QA.",
]

GOODBYES = [
    "Até mais, QA! Teste tudo com muito carinho e qualidade.",
    "Tchau QA! Volte sempre que precisar de dicas sobre testes.",
    "Foi ótimo conversar com você, QA! Até a próxima!",
]

FALLBACKS = [
    "Estou aqui para te ajudar com QA de forma bem prática e objetiva. Que tal perguntar sobre testes funcionais, não funcionais ou gestão de qualidade?",
    "Posso explicar conceitos de QA, técnicas de teste, planejamento de testes ou boas práticas. O que mais te interessa?",
    "Vamos conversar sobre qualidade de software! Pergunte sobre casos de teste, cobertura, métricas ou automação de testes.",
]

PERSONALITY_PREFIXES = [
    "Com muito carinho, QA: ",
    "Aqui vai uma explicação clara, QA: ",
    "Vou te explicar de forma simples, QA: ",
]

ENCOURAGEMENTS = [
    "Quer que eu dê um exemplo prático sobre isso?",
    "Continue perguntando, QA! Estou adorando nossa conversa sobre testes.",
    "Você está evoluindo muito bem como QA! Que tal explorar mais esse tema?",
]

class QAfalda:
    def __init__(self):
        self.name = "QAfalda"
        self.style = """
QAfalda: inteligente, curiosa e acolhedora. Ela lembra a Mafalda, mas fala sobre qualidade de teste.
"""

    def respond(self, question: str) -> str:
        text = question.strip()
        if not text:
            return "Escreva sua dúvida sobre qualidade de teste, QA, que eu respondo com carinho."

        normalized = normalize_text(text)

        if any(word in normalized for word in ["olá", "oi", "bom", "boa", "hello", "eai"]):
            return random.choice(GREETINGS)

        if any(word in normalized for word in ["obrigado", "valeu", "brigado", "thanks"]):
            return random.choice(THANK_YOU)

        if any(word in normalized for word in ["tchau", "até", "adeus", "bye", "see"]):
            return random.choice(GOODBYES)

        if any(word in normalized for word in ["lista", "tópico", "topico", "sintese", "resuma", "temas", "conteudo"]):
            topics = sorted({item["topic"] for item in KNOWLEDGE})
            return "Aqui vão alguns temas que posso explicar, QA:\n- " + "\n- ".join(topics)

        if any(word in normalized for word in ["mafalda", "qafalda", "persona", "personagem"]):
            return (
                "Eu sou a QAfalda, uma persona inspirada na Mafalda. "
                "Meu papel é tirar dúvidas sobre qualidade de teste e incentivar quem estuda QA."
            )

        best = find_best_knowledge(text)
        score = self._estimate_relevance(text, best)
        if score > 0.30:
            prefix = random.choice(PERSONALITY_PREFIXES)
            suffix = random.choice(ENCOURAGEMENTS)
            suggestions = self._get_topic_suggestions(best["topic"])
            response = f"{prefix}{best['answer']} {suffix}"
            if suggestions:
                response += f"\n\n💡 Que tal explorar também: {', '.join(suggestions)}?"
            return response

        return self._friendly_fallback(text)

    def _estimate_relevance(self, question: str, item: dict) -> float:
        from .knowledge import score_match

        return (
            score_match(question, item["question"]) * 0.6 +
            score_match(question, item["answer"]) * 0.3 +
            score_match(question, item["topic"]) * 0.1
        )

    def _friendly_fallback(self, question: str) -> str:
        normalized = normalize_text(question)
        if any(word in normalized for word in ["por", "que", "porque", "pq"]):
            return (
                "Às vezes a melhor resposta é um exemplo. "
                "Tente me perguntar sobre um tipo específico de teste ou um caso prático de QA."
            )
        return random.choice(FALLBACKS)

    def suggest_topics(self, question: str) -> list[str]:
        normalized = normalize_text(question)
        if any(word in normalized for word in ["teste", "qa", "qualidade", "automação", "plano", "defeito"]):
            best = find_best_knowledge(question)
            return self._get_topic_suggestions(best["topic"])

        return random.sample(
            ["Teste de Caixa Preta", "Planejamento de Testes", "Automação de Testes", "Gestão de Defeitos", "Métricas de Qualidade"],
            2,
        )

    def _get_topic_suggestions(self, current_topic: str) -> list[str]:
        """Retorna sugestões de assuntos relacionados ao tópico atual."""
        topic_suggestions = {
            "Fundamentos de Teste": ["Casos de Teste", "Cenários de Teste", "Planejamento de Testes"],
            "Técnicas de Teste": ["Teste de Caixa Preta", "Teste de Caixa Branca", "Teste de Integração"],
            "Gestão de Testes": ["Métricas de Teste", "Relatórios de Teste", "Gestão de Defeitos"],
            "Ferramentas de Teste": ["Automação de Testes", "Ferramentas de Gerenciamento", "Teste de Performance"],
            "Qualidade de Software": ["Processos de QA", "Padrões de Qualidade", "Certificações"],
        }

        # Retorna sugestões relacionadas ou uma seleção aleatória se não encontrar
        if current_topic in topic_suggestions:
            return random.sample(topic_suggestions[current_topic], min(2, len(topic_suggestions[current_topic])))

        # Fallback: retorna alguns tópicos gerais
        all_topics = ["Fundamentos de Teste", "Técnicas de Teste", "Gestão de Testes", "Ferramentas de Teste"]
        return random.sample(all_topics, 2)