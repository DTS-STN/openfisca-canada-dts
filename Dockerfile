FROM python:3-stretch
COPY . /openfisca
WORKDIR /openfisca

#Temporarily manual install of openfisca-core 34.8.0 until dts changes are merged and released
RUN pip install git+https://github.com/DTS-STN/openfisca-core

RUN pip install --upgrade pip && \
    pip install -e . && \
    pip install -r requirements.txt

EXPOSE 5000

CMD [ "/usr/local/bin/openfisca", "serve", "-b", "0.0.0.0:5000" ]
