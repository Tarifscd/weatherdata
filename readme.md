install celery and redis
First active venv and install from requirements.txt .

run - 'celery -A mywebscrapy worker -l INFO' - for running background worker
For scrapping data download from website, run in python shell -
from srcap.tasks import scrapping r = scrapping()