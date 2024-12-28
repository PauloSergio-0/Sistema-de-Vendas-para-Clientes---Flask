#imagem base python
FROM python:3.10-slim

# pasta de trabalho
WORKDIR /app

# dependencias
COPY requirements.txt .

# instalando depêndencias
RUN pip install --no-cache-dir -r requirements.txt

# copiando todos os arquivos
COPY . .

# executar na porta 5000
EXPOSE 5000

# iniciando serviço
CMD [ "python", "app/run.py" ]