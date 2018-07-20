from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
# Create your views here.
from .. models import Goods,Types,Orders,Address,OrderInfo
from . typesviews import paixu
from . userviews import uploads
import os
def list(request):
# 获取搜索条件
	# goods = request.GET.get('type',None)
	# keywords = request.GET.get('keywords',None)

	# if goods:
	# 	#有搜索条件
	# 	if goods == 'all':
	# 		#全条件搜索

	# 		from django.db.models import Q

	# 		orderlist = Orders.objects.filter(
 #                Q(id__contains=keywords)|
 #                Q(title__contains=keywords)|
 #                Q(price__contains=keywords)|
 #                Q(clicknum__contains=keywords)|
 #                Q(num__contains=keywords)
 #            )
     
	# 	elif goods == 'id':
	# 		goodslist = Goods.objects.filter(id__contains=keywords)
	# 	elif goods == 'title':
	# 		goodslist = Goods.objects.filter(title__contains=keywords)
	# 	elif goods == 'price':
	# 		goodslist = Goods.objects.filter(price__contains=keywords)

	# 	elif goods == 'clicknum':
	# 		goodslist = Goods.objects.filter(clicknum__contains=keywords)
	# 	elif goods == 'num':
	# 		goodslist = Goods.objects.filter(num__contains=keywords)
	# 	elif goods == 'typeid':
	# 		goodslist = Goods.objects.filter(typeid__name__contains=keywords)
	# else:
	# 	#获取所有数据
	goodslist = Orders.objects.filter()
	# 	# print(goodslist.pid)
	# 	# print(goodslist)
	# # for x in goodslist:
	# # 	if x.pid == 0:
	# # 		x.pname = '顶级分类'
	# # 	else:
	# # 		t = Types.objects.get(id=x.pid)
	# # 		x.pname = t.name
	# # 		num  = x.path.count(',')-1
	# # 		x.name = (num*'|----')+x.name


	# #导分页类
	from  django.core.paginator import Paginator

	#实例化对象 参数1是数据集和 参数2是每页显示的条数
	paginator = Paginator(goodslist,2)
	#获取当前的页码数
	p = request.GET.get('p',1)

	# 获取当前页码的数据
	gllist = paginator.page(p)
	#分配数据
	context = {'glist':gllist}

	# return HttpResponse('aaaa')
	return render(request,'myadmin/order/order.html',context)


def info(request):

	oid = request.GET.get('oid')

	print(oid)

	data = OrderInfo.objects.filter(orderid = oid)
	print(data)
	context = {'data':data,'uid':oid}

	return render(request,'myadmin/order/info.html',context)


# def edit(request):

# 	if request.method == 'GET':

# 		uid = request.GET.get('uid')
# 		data = Orders.objects.get(id=uid)

# 		context = {'data':data}

# 		return render(request,'myadmin/order/edit.html',context)


# 	elif request.method == 'POST':
# 		