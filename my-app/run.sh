export OPENAI_API_KEY=
PYTHONPATH=app uvicorn app.server:app --host 0.0.0.0 --port 8000 --reload
