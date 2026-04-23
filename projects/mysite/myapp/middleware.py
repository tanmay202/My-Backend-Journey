class LogRequestMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        print(f"[Middleware] request path :{request.path}")
        response=self.get_response(request)
        
        print(f"[Middleware] response status:{response.status_code}")
        return response
    
import time

class TimeCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()

        response = self.get_response(request)

        duration = time.time() - start
        print(f'[Middleware] took {duration:.4f} seconds')

        return response
    
class IPBlockerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        # List of blocked IPs
        self.blocked_ips = [
            '127.0.0.1',   # IPv4 localhost
            '::1',         # IPv6 localhost
        ]

    def __call__(self, request):
        ip = self.get_client_ip(request)

        if ip in self.blocked_ips:
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("Access Denied 🚫")

        return self.get_response(request)

    def get_client_ip(self, request):
        # Handle proxy headers (important in real-world apps)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        return ip
        