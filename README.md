

# 🌟 Aplicativo Web de Predicción con Django y ML 🌟
---
Este proyecto implementa un **aplicativo web en Django** que permite cargar un modelo de **Machine Learning** preentrenado (Iris) para realizar predicciones basadas en datos proporcionados a través de un archivo Excel. ¡Todo esto con una interfaz sencilla y fácil de usar que despliega los resultados directamente en la web!

Aplicación **desplegada** aquí: 
  - [Link Aplicación](https://web-production-cfa5.up.railway.app/predictions/)
  - [Archivo Excel de prueba](https://docs.google.com/spreadsheets/d/1PF2AIta3LV15Mq5JrIwq8mpXNEzuwXLS/edit?usp=sharing&ouid=100339178753591638653&rtpof=true&sd=true)
----

## 🛠️ Características Principales

- 🚀 **Carga de modelo preentrenado:** Integra el modelo Iris de ML listo para predecir con datos cargados dinámicamente.
- 📊 **Predicción desde Excel:** Sube un archivo Excel con datos, y obtén predicciones procesadas en tiempo real.
- 🖥️ **Resultados en HTML:** Los resultados se presentan en una tabla fácil de interpretar.
- 🐳 **Listo para producción:** Configuración optimizada con Docker y despliegue automatizado en Railway.
- 🔄 **CI/CD Integrado:** Flujo automatizado con GitHub Actions para asegurar la calidad en cada cambio.
- 🚧 **Unit tests:** Se hace una covertura total de todos los servicios utilizados por el aplicativo.
---

## 🔧 Tecnologías Utilizadas

- **Framework Backend:** Django 
- **Interfaz web:** Estructura HTML semántico y estilizado con CSS.
- **Machine Learning:** Modelo preentrenado basado en el dataset `iris` para predicción de clases de flores.
- **DevOps:** 
  - `Docker` para contenedorización.
  - `Railway` como plataforma de despliegue.
  - `GitHub Actions` para CI/CD automatizado.

---
## 📂 Estructura del Proyecto

La estructura del proyecto está organizada de la siguiente manera:
  ```
  ├── .github/workflows        # Pipelines de CI/CD con GitHub Actions
  ├── predictions              # Archivos relacionados con predicciones (modelo, etc.)
  ├── scripts                  # Scripts auxiliares para datos o manejo del modelo
  ├── prueba_tecnica_talentoB  # Código principal de Django
  ├── Dockerfile               # Configuración para contenedor Docker
  ├── docker-compose.yml       # Orquestación de contenedores
  ├── requirements.txt         # Dependencias del proyecto
  ```
---

## 🛠️ Desarrollo y Pipeline
- **CI/CD Pipeline:** Automatización del flujo de integración y despliegue continuo con GitHub Actions.
  - Validación y construcción del entorno.
  - Despliegue automatizado en Railway.
- **Railway:** Servicio utilizado para ejecutar la aplicación web en la nube, asegurando alta disponibilidad.

---


## 🚀 Instalación y Uso Local

Sigue los pasos a continuación para ejecutar el proyecto en tu entorno local:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/FerneyMontoya1/prueba-tecnica-talentoB.git
   cd prueba-tecnica-talentoB
2. Construye y ejecuta los contenedores usando Docker:
   ```bash
   docker-compose up --build
3. Accede al aplicativo desde tu navegador en: http://localhost:8000.
4. Sube un archivo Excel para predecir resultados utilizando el modelo preentrenado. 🎉

## 📊 Ejemplo de Uso
1. Carga del archivo Excel:
   - Subir un archivo con datos similares al formato del dataset iris. [Archivo Excel de prueba](https://docs.google.com/spreadsheets/d/1PF2AIta3LV15Mq5JrIwq8mpXNEzuwXLS/edit?usp=sharing&ouid=100339178753591638653&rtpof=true&sd=true)
2. Procesamiento:
   - El modelo realiza la predicción y los resultados se procesan en tiempo real.
3. Visualización:
   - Los resultados se muestran directamente en una tabla HTML en la misma página web.

## ✨ Créditos
Desarrollado por Ferney Montoya para la prueba técnica de Talento b. 💻


