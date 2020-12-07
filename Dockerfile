FROM 3.9.0-alpine3.12
COPY main.py /main.py
RUN pip install pathlib
CMD python main.py