class LogRequestMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        print(f"[Middleware] request path :{request.path}")
        response=self.get_response(request)
        
        print(f"[Middleware] response status:{response.status_code}")
        return response