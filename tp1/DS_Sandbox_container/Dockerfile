FROM ubuntu
WORKDIR /workspace
COPY . .

RUN apt-get update

RUN apt-get install -y python3.8 python3-pip vim git	
RUN pip3 install -r requirement.txt 

RUN git config --global user.name allanCouderette \				
&& git config --global user.email al@google.fr \
&& git clone https://github.com/allanCouderette/noSql.git


EXPOSE 8000
CMD jupyter notebook --no-browser --allow-root --ip 0.0.0.0 --port 8000 