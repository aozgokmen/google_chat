
FROM python:3.9.6
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Uygulamanın geri kalanını kopyalayın
COPY . .
CMD [ "python", "./nobet_bot.py" ]
