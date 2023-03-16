env:
	sudo apt install python3-pip
	pip3 install virtualenv
	python3 -m venv env

install: requirements.txt 
	pip3 install -r requirements.txt 


create:
ifdef n
	python manage.py create --n=$(n)
else
	python manage.py create
endif

signup:
	python manage.py views 
