FROM python:3.12
RUN pip install scikit-learn
RUN pip install requests
RUN pip install pytest
RUN pip install flask
RUN pip install pandas
RUN pip install numpy
RUN pip install scipy
COPY . .
CMD ["python3","index.py"]