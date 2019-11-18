## Getting started

Start project with three celery workers
```sh
bash docker-compose.bash up --build --scale celery=3
```

### Trigger tasks

```sh
http --json :8000/timeseries 'database_code=WIKI' 'dataset_code=FB'
```

```sh
http :8000/timeseries
```