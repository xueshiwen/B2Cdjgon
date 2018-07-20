from django.shortcuts import render
from django.http import HttpResponse
import re


class Middleware:
	def __init__(self, get_response):
		self.get_response = get_response
# One-time configuration and initialization.

	def __call__(self, request):

#获取当前用户的路径
		urllis = ['/myadmin/login/','/myadmin/vcode/']

        # 判断是否要进入后台
		if re.match('/myadmin/',request.path) and request.path not in urllis:

            # 判断是否登录
			if not request.session.get('_auth_user_id',None):
                # 如果没有登录,则跳转到登录页面
				return HttpResponse('<script>alert("请先登录");location.href="/myadmin/login/"</script>')

				

	#定义url登录请求
		ullist = ['/ordercheck/','/addressedit/','/addressadd/','/ordercreate/','/buy/','/mycenter/']
	#判断前台是否登录
	#判断当前的请求需不需要登录

		 # 判断是否进入
		if request.path in ullist:

            # 判断是否登录
			if not request.session.get('VipUser',None):
                # 如果没有登录,则跳转到登录页面
				return HttpResponse('<script>alert("请先登录");location.href="/login/"</script>')



		response = self.get_response(request)

		return response