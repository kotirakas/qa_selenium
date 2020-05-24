FROM python:3.7

WORKDIR /app

COPY . .

RUN apt-get update
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN apt-get install -y wget xvfb unzip
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo deb http://dl.google.com/linux/chrome/deb/ stable main >> /etc/apt/sources.list.d/google.list
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable
RUN wget https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/bin/chromedriver
RUN chown root:root /usr/bin/chromedriver
RUN chmod +x /usr/bin/chromedriver
ENV PATH /chromedriver:$PATH

CMD ["pytest", "--alluredir", "allure-report"]