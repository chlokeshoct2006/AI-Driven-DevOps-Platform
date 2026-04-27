FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install pandas scikit-learn flask joblib

CMD ["python", "app.py"]