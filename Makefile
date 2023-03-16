env:
	sudo apt install python3-pip
	pip3 install virtualenv
	python3 -m venv env

install: requirements.txt 
	pip3 install -r requirements.txt 

migrate:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py makemigrations core
	python manage.py migrate core
	python manage.py makemigrations twbot
	python manage.py migrate twbot


create:
ifdef n
	python manage.py create --n=$(n)
else
	python manage.py create
endif

signup:
	python manage.py views 

git:
	git stash
	git pull
