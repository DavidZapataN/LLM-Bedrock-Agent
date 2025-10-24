# 🧠 LLM-Bedrock-Agent – SageMaker Assistant

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)
![AWS](https://img.shields.io/badge/AWS-Bedrock-orange?logo=amazonaws)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)

Asistente conversacional especializado en **Amazon SageMaker**, desarrollado como ejercicio práctico de **Agentic AI** con Amazon Bedrock.

La aplicación permite interactuar con un **agente inteligente** que responde sobre servicios de SageMaker como **JumpStart**, **Model Cards**, **Ground Truth**, **Pipelines**, **Endpoints**, entre otros, mediante una interfaz desarrollada con **Streamlit** y desplegada en **Docker**.

---

## 🚀 Tecnologías utilizadas

- 🧠 **Amazon Bedrock** → modelo fundacional y agente inteligente
- 💬 **Streamlit** → interfaz conversacional tipo chat
- 🐍 **Boto3 (AWS SDK)** → integración con los servicios de AWS
- 🐳 **Docker** → contenedorización y despliegue local
- ⚙️ **Python 3.11+**

---

## 🔧 Variables de entorno

Crea un archivo **`.env`** en la raíz del proyecto (usa `.env.example` como guía):
```env
AWS_REGION=us-east-1
AGENT_ID=agnt-xxxxxxxxxxxxxxxx
AGENT_ALIAS_ID=xxxxxxxx
AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_HERE
AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY_HERE
AWS_SESSION_TOKEN=YOUR_SESSION_TOKEN_IF_NEEDED
```

> ⚠️ **Importante:** No subas este archivo al repositorio.  
> El `.gitignore` ya lo excluye automáticamente por seguridad.

---

## 🧩 Ejecución local (sin Docker)

**1️⃣ Activa tu entorno virtual:**
```bash
source .venv/bin/activate
```

**2️⃣ Ejecuta la aplicación con Streamlit:**
```bash
streamlit run app.py
```
> ⚠️ **Importante:** Antes de hacer esto exporta las variables a tu terminal.  


Abre en tu navegador:  
👉 [http://localhost:8501](http://localhost:8501)

---

## 🐳 Ejecución con Docker

### 🔹 1. Construir la imagen
```bash
docker build -t sagemaker-assistant:latest .
```

### 🔹 2. Ejecutar el contenedor
```bash
docker run --rm -p 8501:8501 --env-file "$(pwd)/.env" sagemaker-assistant:latest
```

💡 **Si el puerto 8501 está ocupado, usa otro:**
```bash
docker run --rm -p 8502:8501 --env-file "$(pwd)/.env" sagemaker-assistant:latest
```

Abre la aplicación en tu navegador:  
👉 [http://localhost:8501](http://localhost:8501)

---

## 🧠 Ejemplo de uso

**Usuario:**  
> ¿Qué es Amazon SageMaker JumpStart?

**Asistente:**  
> SageMaker JumpStart es una colección de soluciones preconstruidas y modelos preentrenados que permiten iniciar rápidamente proyectos de aprendizaje automático en Amazon SageMaker.

---

## 🧹 Limpieza de Docker (opcional)

Para limpiar contenedores e imágenes temporales:
```bash
docker ps -a
docker stop <container_id>
docker system prune -f
```

---

## 👤 Autor

**David Zapata**

