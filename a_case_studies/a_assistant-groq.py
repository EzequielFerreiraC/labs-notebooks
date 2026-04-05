import os
import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="Assistente de Python com Groq", 
    page_icon="🤖", 
    layout="centered",
    initial_sidebar_state="expanded"
)

CUSTOM_PROMPT = """
Você é o "DSA Coder", um assistente de IA especialista em programação, com foco principal em Python. Sua missão é ajudar desenvolvedores iniciantes com dúvidas de programação de forma clara, precisa e útil.

REGRAS DE OPERAÇÃO:
1.  **Foco em Programação**: Responda apenas a perguntas relacionadas a programação, algoritmos, estruturas de dados, bibliotecas e frameworks. Se o usuário perguntar sobre outro assunto, responda educadamente que seu foco é exclusivamente em auxiliar com código.
2.  **Estrutura da Resposta**: Sempre formate suas respostas da seguinte maneira:
    * **Explicação Clara**: Comece com uma explicação conceitual sobre o tópico perguntado. Seja direto e didático.
    * **Exemplo de Código**: Forneça um ou mais blocos de código em Python com a sintaxe correta. O código deve ser bem comentado para explicar as partes importantes.
    * **Detalhes do Código**: Após o bloco de código, descreva em detalhes o que cada parte do código faz, explicando a lógica e as funções utilizadas.
    * **Documentação de Referência**: Ao final, inclua uma seção chamada "📚 Documentação de Referência" com um link direto e relevante para a documentação oficial da Linguagem Python (docs.python.org) ou da biblioteca em questão.
3.  **Clareza e Precisão**: Use uma linguagem clara. Evite jargões desnecessários. Suas respostas devem ser tecnicamente precisas.
"""

with st.sidebar:
    st.title("DSA IA Coder")

    st.markdown("Um assistente de IA focado em programação py")

    groq_api_key = st.text_input(
        "Insira sua API Key Groq",
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar")


st.title("Data Science Academy - Dsa Coder")

st.title("Assistente pessoal de Programção Python")

st.caption("Faça sua pergunta sobre a Linguagem Python")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

client = None

if groq_api_key:
    try:
        client = Groq(api_key = groq_api_key)

    except Exception as e:
        st.sidebar.error(f"Erro ao incializar o Groq {e}")
        st.stop()

elif st.session_state.messages:
    st.warning("Por favor, insira sua API Ket da Groq na barra lateral")


if prompt := st.chat_input("Qual sua dúvida sobre Python?"):

    if not client:
        st.warning("Por favor, insira sua API key")
        st.stop

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
        messages_for_api.append(msg)

    with st.chat_message("assistant"):
        with st.spinner("Analisando sua pergunta..."):
            try:
                chat_completion = client.chat.completions.create(
                    messages = messages_for_api,
                    model = "openai/gpt-oss-120b",
                    temperature = 0.7,
                    max_tokens = 2048,
                )

                dsa_ai_resposta = chat_completion.choices[0].message.content

                st.markdown(dsa_ai_resposta)
                st.session_state.messages.append({"role": "assistant", "content:": dsa_ai_resposta})

            except Exception as e:
                st.error(f"Ocorreu um erro ao se comuniar com a API do Groq: {e}")


st.markdown(
    """
        <div style="background-color: #black; padding: 20px; border-radius: 10px; text-align: center; color: white;">
            <h3>DSA IA Coder</h3>
            <p>Um assistente de IA focado em programação Python</p>
        </div>
    """,
    unsafe_allow_html=True

)