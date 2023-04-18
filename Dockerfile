FROM python:3.10
RUN pip install flask
RUN pip install pandas
RUN pip install numpy
RUN pip install scikit-learn==0.24.2
RUN pip install sklearn
RUN pip install scipy
RUN pip install requests
RUN pip install pytest
COPY . .
CMD ["python3","app.py"]