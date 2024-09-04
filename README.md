# How to use

1. install requirments.txt

```bash
cd src
pip install -r requirments.txt
```

2. run migrations

```bash
alembic upgrade head
```

3. run docker-compose

```bash
cd .. # to root folder
docker-compose up -d
```

4. see API endpoints

```
http://localhost:8000/docs
```