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

#### start grafana and download django prometheus dashboard
##### django dashboard here(https://grafana.com/grafana/dashboards/7996)
