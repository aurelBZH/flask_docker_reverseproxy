FROM nginx
COPY ./flask_min /etc/nginx/sites-available/
RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/flask_min /etc/nginx/sites-enabled/flask_min