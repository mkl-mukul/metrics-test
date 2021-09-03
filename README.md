# metrics-test
## install django 
## go to prometheus folder start  
```bash
./prometheus --config.file=prometheus.yml
```
## now run this django project 
``` bash
python3 manage.py runserver
```

## go to browser 
### prometheus monitoring 
``` bash
http://localhost:9090
```
### django project
``` bash
http://localhost:8000
```

#### refresh django page and check this query in prometheus 
``` bash
python_http_total_response_total
```
