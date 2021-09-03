
import prometheus_client
from prometheus_client import Counter, Histogram,CollectorRegistry, Gauge, push_to_gateway,Summary
from django.http import HttpResponse
from django.shortcuts import render
import time 

class SimpleMiddleware:
    def __init__(self,get_response): 
        self.start=time.time()
        self.get_response = get_response 
        self.graph={}
        self.graph['http'] = Counter('python_http_total_response','http response',['status_code','endpoint'])
        self.graph['t']= Histogram('python_response_duration_seconds','duration in second',['status_code','endpoint'])#,buckets=(0.1,0.7,1,5,10,float('inf')))
        #self.graph['s']=Summary('python_response_duration','duaration quantile')
      
        
      #  self.graph['404'] = Counter('http_404_total_response','total response of 400')
    def __call__(self, request):
        response = self.get_response(request) 
        if request.path == "/" :
            time.sleep(0.5)
            end=time.time()
            print(f'start {self.start}')
            print(f'end{end}')

            print(f'final{end-self.start}')  
            #self.graph['s'].observe(end-self.start) 
            if response.status_code == 200 :
                self.graph['t'].labels('200','/').observe(end-self.start) 
                self.graph['http'].labels(status_code=200,endpoint='/').inc() 
            elif response.status_code == 404 :
                 self.graph['t'].labels('404','/').observe(end-self.start) 
                 self.graph['http'].labels(status_code=404,endpoint='/').inc()
            elif response.status_code == 500 :
                 self.graph['t'].labels('500','/').observe(end-self.start) 
                 self.graph['http'].labels(status_code=404,endpoint='/').inc()
        return response
             
   
        

   




        