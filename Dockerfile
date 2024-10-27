FROM python:3.12
RUN pip install scikit-learn==0.24.2
RUN pip install flask
RUN pip install pandas
RUN pip install numpy
RUN pip install sklearn
RUN pip install scipy
RUN pip install requests
COPY . .
CMD ["python3","app.py"]