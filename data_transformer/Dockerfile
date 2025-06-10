FROM python:3.11-slim

RUN pip install pandas
COPY exec.py .
COPY joint_list.json .

CMD ["python", "exec.py"]