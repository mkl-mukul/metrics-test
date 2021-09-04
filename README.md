# metrics-test
## install django 
### install django-prometheus or [check here](https://github.com/korfuri/django-prometheus)
```bash
pip install django-prometheus
```

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
##### import this dashboard code 7996 or check here (https://grafana.com/grafana/dashboards/7996) and add prometheus datasource

#### change some query in grafana dashboard
##### request panel
```bash
10*(sum(irate(django_http_requests_total_by_view_transport_method_total{service=~"^$service$",view!~"prometheus-django-metrics|healthcheck"}[30s])) by(method, view))
```
##### response panel
```bash
10*(sum(irate(django_http_responses_before_middlewares_total{service=~"^$service$", view!~"prometheus-django-metrics|healthcheck"}[30s])) by(job))
```
##### add new panel and add this query for duration seconds
``` bash
rate(django_db_query_duration_seconds_bucket[30s])
```
##### total 200 responses 
```bash
django_http_responses_total_by_status_total{status=~"2.+",service=~"^$service$"}
```
