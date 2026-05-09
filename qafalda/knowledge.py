import re
from typing import List, Dict

KNOWLEDGE: List[Dict[str, str]] = [
    {
        "topic": "Fundamentos do teste",
        "question": "O que é teste de software e qual é seu objetivo?",
        "answer": (
            "Teste de software é a atividade que busca encontrar problemas antes que o produto chegue ao usuário. "
            "Seu objetivo é verificar se o software atende aos requisitos, reduzir riscos e aumentar a confiança na qualidade."
        ),
    },
    {
        "topic": "Princípios do teste",
        "question": "Quais são os princípios básicos do teste?",
        "answer": (
            "Os princípios incluem: todo teste mostra a presença de defeitos, testes exaustivos são impossíveis, "
            "os testes devem começar cedo, defeitos se agrupam, necessidade de contexto e a importância da avaliação de risco."
        ),
    },
    {
        "topic": "Plano de teste",
        "question": "Como fazer o planejamento de teste?",
        "answer": (
            "Planejamento de teste define o que será testado, como será testado, quais recursos são necessários e quais riscos devem ser mitigados. "
            "Inclui escopo, cronograma, critérios de entrada e saída, e controle de mudanças."
        ),
    },
    {
        "topic": "Estratégia de teste",
        "question": "Qual é a diferença entre estratégia e plano de teste?",
        "answer": (
            "A estratégia de teste é o desenho de alto nível das abordagens usadas para validar o produto. "
            "O plano é o documento que organiza atividades concretas, cronograma, recursos e responsáveis."
        ),
    },
    {
        "topic": "Casos de teste",
        "question": "O que são casos de teste?",
        "answer": (
            "Casos de teste descrevem entradas, ações e resultados esperados para validar um requisito. "
            "Eles ajudam a garantir que os testes sejam repetíveis, claros, rastreáveis e fáceis de executar."
        ),
    },
    {
        "topic": "Técnicas de caixa preta",
        "question": "Quais são as técnicas de teste de caixa preta?",
        "answer": (
            "Técnicas de caixa preta examinam o comportamento do sistema sem olhar o código. "
            "Exemplos incluem partição de equivalência, análise de valor limite, tabelas de decisão e teste exploratório."
        ),
    },
    {
        "topic": "Técnicas de caixa branca",
        "question": "Como funciona o teste de caixa branca?",
        "answer": (
            "Teste de caixa branca verifica a lógica interna, estruturas de controle e caminhos de código. "
            "É usado para medir cobertura, validar fluxos de decisão e checar condições internas."
        ),
    },
    {
        "topic": "Teste exploratório",
        "question": "O que é teste exploratório?",
        "answer": (
            "Teste exploratório é uma abordagem onde o testador investiga o produto em tempo real, usando conhecimento e intuição. "
            "É muito útil para descobrir problemas inesperados e validar a experiência do usuário."
        ),
    },
    {
        "topic": "Teste de regressão",
        "question": "Quando devo usar teste de regressão?",
        "answer": (
            "Teste de regressão é usado sempre que o software sofre mudanças ou correções. "
            "O objetivo é garantir que funcionalidades existentes continuem funcionando após novas alterações."
        ),
    },
    {
        "topic": "Cobertura de teste",
        "question": "O que significa cobertura de teste?",
        "answer": (
            "Cobertura de teste mede quanto do sistema, dos requisitos ou do código foi validado pelos testes. "
            "Ela ajuda a identificar lacunas e a melhorar a confiança na qualidade do produto."
        ),
    },
    {
        "topic": "Critérios de aceitação",
        "question": "O que são critérios de aceitação?",
        "answer": (
            "Critérios de aceitação descrevem as condições que uma funcionalidade deve cumprir para ser considerada pronta. "
            "Eles orientam o desenvolvimento e os testes para que todos tenham a mesma expectativa."
        ),
    },
    {
        "topic": "Ambiente de teste",
        "question": "Por que ambiente de teste é importante?",
        "answer": (
            "Um ambiente de teste confiável reproduz condições semelhantes às do uso real do sistema. "
            "Sem um bom ambiente, os testes podem falhar por causa de fatores externos e não do software em si."
        ),
    },
    {
        "topic": "Testes não funcionais",
        "question": "Quais são exemplos de testes não funcionais?",
        "answer": (
            "Testes não funcionais verificam aspectos como performance, segurança, usabilidade, compatibilidade e confiabilidade. "
            "Eles são essenciais para medir experiência e robustez, além de funcionalidade."
        ),
    },
    {
        "topic": "Revisão e inspeção",
        "question": "Qual a importância de revisão de teste?",
        "answer": (
            "Revisão e inspeção ajudam a encontrar problemas cedo, antes do esforço de execução. "
            "Elas melhoram a qualidade dos casos de teste, dos requisitos e da documentação."
        ),
    },
    {
        "topic": "Avaliação de risco",
        "question": "Como faço avaliação de risco em testes?",
        "answer": (
            "Avaliação de risco identifica as áreas que têm maior chance de falha e maior impacto. "
            "Com isso, os testes são planejados de forma mais eficiente e a equipe foca no que mais importa."
        ),
    },
    {
        "topic": "Teste de usabilidade",
        "question": "O que é teste de usabilidade?",
        "answer": (
            "Teste de usabilidade verifica se o usuário consegue utilizar o sistema com facilidade e satisfação. "
            "Ele analisa clareza, fluxo de interação e barreiras que podem prejudicar a experiência."
        ),
    },
    {
        "topic": "Teste de integração",
        "question": "Como funciona o teste de integração?",
        "answer": (
            "Teste de integração valida a comunicação entre componentes ou sistemas. "
            "Ele busca problemas de interface, dados e dependências entre partes do software."
        ),
    },
    {
        "topic": "Teste de sistema",
        "question": "O que é teste de sistema?",
        "answer": (
            "Teste de sistema valida o produto como um todo, considerando todas as suas partes integradas. "
            "Ele confirma que o comportamento final atende ao requisito do usuário e às expectativas do negócio."
        ),
    },
    {
        "topic": "Teste de aceitação",
        "question": "O que é teste de aceitação?",
        "answer": (
            "Teste de aceitação verifica se o software cumpre os requisitos do cliente e está pronto para uso. "
            "Normalmente envolve validação pelos usuários ou pelo time de produto."
        ),
    },
    {
        "topic": "Métricas de teste",
        "question": "Quais métricas são úteis em testes?",
        "answer": (
            "Métricas úteis incluem taxa de defeitos, progresso dos testes, cobertura de requisitos, execução de casos e densidade de defeitos. "
            "Elas ajudam a avaliar qualidade, progresso e necessidade de ajustes."
        ),
    },
    {
        "topic": "Gestão de defeitos",
        "question": "Como gerenciar defeitos?",
        "answer": (
            "O ciclo de vida do defeito inclui identificação, registro, classificação, correção, verificação e fechamento. "
            "Uma boa gestão usa triagem, priorização e comunicação clara entre teste e desenvolvimento."
        ),
    },
    {
        "topic": "Automação de testes",
        "question": "Quando usar automação de testes?",
        "answer": (
            "Automação é indicada para testes repetitivos, regressão e validação rápida de funcionalidades estáveis. "
            "Não substitui testes exploratórios, mas acelera entregas e melhora a consistência."
        ),
    },
    {
        "topic": "Teste de unidade",
        "question": "O que é teste de unidade?",
        "answer": (
            "Teste de unidade valida componentes individuais do software, como funções ou métodos. "
            "É executado pelos desenvolvedores e ajuda a identificar problemas logo no início do desenvolvimento."
        ),
    },
    {
        "topic": "Teste de performance",
        "question": "Como funciona o teste de performance?",
        "answer": (
            "Teste de performance avalia o comportamento do sistema sob carga, medindo velocidade, estabilidade e uso de recursos. "
            "Inclui testes de carga, estresse e volume para garantir que o sistema suporte o uso esperado."
        ),
    },
    {
        "topic": "Teste de segurança",
        "question": "O que é teste de segurança?",
        "answer": (
            "Teste de segurança identifica vulnerabilidades e garante que o sistema proteja dados e usuários contra ameaças. "
            "Inclui verificação de autenticação, autorização, criptografia e conformidade com padrões de segurança."
        ),
    },
    {
        "topic": "Teste de compatibilidade",
        "question": "Por que fazer teste de compatibilidade?",
        "answer": (
            "Teste de compatibilidade verifica se o software funciona corretamente em diferentes ambientes, como sistemas operacionais, navegadores ou dispositivos. "
            "Garante que os usuários tenham uma experiência consistente independente da plataforma."
        ),
    },
    {
        "topic": "Ferramentas de teste",
        "question": "Quais ferramentas são usadas em testes?",
        "answer": (
            "Ferramentas de teste incluem gerenciadores de casos de teste, ferramentas de automação como Selenium, ferramentas de cobertura de código, "
            "ferramentas de gerenciamento de defeitos como Jira, e ferramentas de performance como JMeter."
        ),
    },
    {
        "topic": "Ciclo de vida de desenvolvimento",
        "question": "Como o teste se integra ao ciclo de desenvolvimento?",
        "answer": (
            "O teste deve ser integrado desde o início do desenvolvimento, seguindo abordagens como TDD, BDD ou testes contínuos. "
            "Isso inclui testes em cada fase: planejamento, desenvolvimento, integração, sistema e aceitação."
        ),
    },
    {
        "topic": "Análise estática",
        "question": "O que é análise estática?",
        "answer": (
            "Análise estática examina o código ou documentação sem executar o software. "
            "Inclui revisões de código, inspeções e uso de ferramentas para detectar problemas potenciais antes da execução."
        ),
    },
    {
        "topic": "Teste baseado em experiência",
        "question": "O que é teste baseado em experiência?",
        "answer": (
            "Teste baseado em experiência usa o conhecimento e intuição do testador para explorar o sistema. "
            "Inclui teste exploratório, testes de ataque e uso de heurísticas para descobrir defeitos não óbvios."
        ),
    },
    {
        "topic": "Qualidade de processo",
        "question": "O que é garantia da qualidade?",
        "answer": (
            "Garantia da qualidade foca no processo usado para criar o produto, não apenas em encontrar defeitos. "
            "Inclui revisão de processos, auditorias e melhoria contínua para que o resultado seja confiável."
        ),
    },
]


def normalize_text(text: str) -> List[str]:
    cleaned = re.sub(r"[^a-z0-9\s]", " ", text.lower())
    return [word for word in cleaned.split() if word]


def score_match(query: str, text: str) -> float:
    query_tokens = set(normalize_text(query))
    text_tokens = set(normalize_text(text))
    if not query_tokens or not text_tokens:
        return 0.0
    overlap = query_tokens & text_tokens
    return len(overlap) / max(len(text_tokens), 1)


def find_best_knowledge(query: str) -> Dict[str, str]:
    best_item = None
    best_score = 0.0
    for item in KNOWLEDGE:
        score = (
            score_match(query, item["question"]) +
            score_match(query, item["answer"]) +
            score_match(query, item["topic"])
        )
        if score > best_score:
            best_score = score
            best_item = item
    return best_item if best_item else KNOWLEDGE[0]
