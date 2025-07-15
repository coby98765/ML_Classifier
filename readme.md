install library
``` bash
pip install requirements.txt
```
update requirements
```bash
pip freeze > requirements.txt
```
run FastAPI server
```bash
uvicorn back.api:app --reload
```
uvicorn back.api:app --reload --port 8001
