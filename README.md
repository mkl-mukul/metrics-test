# metrics-test
## install django 
### install django-prometheus or [check here](https://github.com/korfuri/django-prometheus)
```bash
pip install django-prometheus
```
### download prometheus (https://prometheus.io/download/)

### add this in prometheus.yml file 
```bash
global:
  scrape_interval: 15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets:
          # - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: "prometheus"

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
      - targets: ["localhost:9090"]
  
  - job_name: django
    scrape_interval: 10s
    static_configs:
      - targets:
        - localhost:8000
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

## start grafana and download django prometheus dashboard 
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
