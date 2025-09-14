# Usa uma imagem oficial do Python como base
FROM python:3.10-slim

# Define um diretório dentro do container para rodar a aplicação
WORKDIR /app

# Copia o arquivo da aplicação para dentro do container
COPY geometria.py .

# Comando que será executado quando o container iniciar
CMD ["python", "geometria.py"]
