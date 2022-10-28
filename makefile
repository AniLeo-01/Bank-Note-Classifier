run-db:
	sudo docker run --name banknotes-classifier -p 5432:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_DB=banknotes_db -v ${PWD}/database:/var/lib/postgresql/data -d postgres

start-server:
	uvicorn src.main:app --reload

run-streamlit:
	streamlit run 1_🏠_Home.py