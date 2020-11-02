FROM ubuntu 				# Image de base Ubuntu
WORKDIR /workspace			# Espace de travail
COPY . .

# Installer les packages python, pip3, vim et git
RUN apt-get install -r -y requirementPackage.txt	
# Installer les librairies de python
RUN pip3 install -r requirementLibPython.txt 

# credential git
RUN git --global user.name allanCouderette \				
&& git config --global user.email allan.couderette@free.fr \
&& git clone https://github.com/allanCouderette/noSql


EXPOSE 8000 # exposition du port 8000
CMD ["jupyter", "notebook","--no-browser"]