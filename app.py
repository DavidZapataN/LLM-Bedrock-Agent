import os
import uuid
import streamlit as st
import boto3

# Configuración básica de la app
st.set_page_config(page_title="SageMaker Assistant", page_icon="🧠", layout="centered")
st.title("🧠 SageMaker Assistant (Bedrock Agent)")

# Cargar variables desde el entorno del sistema
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AGENT_ID = os.getenv("AGENT_ID", "")
AGENT_ALIAS_ID = os.getenv("AGENT_ALIAS_ID", "")

# Verificar configuración
if not AGENT_ID or not AGENT_ALIAS_ID:
    st.error("❌ Faltan AGENT_ID o AGENT_ALIAS_ID en las variables de entorno.")
    st.stop()

# Cliente Bedrock Agent Runtime
bedrock_rt = boto3.client("bedrock-agent-runtime", region_name=AWS_REGION)

# Estado de la sesión
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Entrada del usuario
user_input = st.chat_input("💬 Escribe una pregunta sobre Amazon SageMaker...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Llamada al agente
    with st.chat_message("assistant"):
        placeholder = st.empty()
        chunks = []
        try:
            response = bedrock_rt.invoke_agent(
                agentId=AGENT_ID,
                agentAliasId=AGENT_ALIAS_ID,
                sessionId=st.session_state.session_id,
                inputText=user_input,
                enableTrace=False,  # Cambia a True para depurar
                endSession=False,
            )

            # Leer la respuesta (viene en stream de eventos)
            for event in response.get("completion", []):
                if "chunk" in event:
                    text = event["chunk"]["bytes"].decode("utf-8", errors="ignore")
                    chunks.append(text)
                    placeholder.markdown("".join(chunks))

            final_text = "".join(chunks).strip() or "_(sin contenido)_"
        except Exception as e:
            final_text = f"⚠️ Error al invocar el agente:\n\n`{e}`"

        placeholder.markdown(final_text)
        st.session_state.messages.append({"role": "assistant", "content": final_text})

# Separador y botón para limpiar
st.divider()
col1, col2 = st.columns(2)
with col1:
    if st.button("🧹 Limpiar chat"):
        st.session_state.messages = []
        st.session_state.session_id = str(uuid.uuid4())
        st.rerun()
with col2:
    st.caption(f"Session ID: `{st.session_state.session_id}`")
