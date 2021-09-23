FROM python:3.9.7-alpine

RUN adduser -D jfrogcleaner
USER jfrogcleaner
WORKDIR /home/jfrogcleaner

COPY --chown=jfrogcleaner:jfrogcleaner jfrogclean.py jfrogclean.py
RUN pip install --user requests --no-warn-script-location

ENV PATH="/home/jfrogcleaner/.local/bin:${PATH}"

COPY --chown=jfrogcleaner:jfrogcleaner jfrogclean.py .

CMD ["python", "jfrogclean.py"]
