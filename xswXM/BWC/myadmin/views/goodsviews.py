from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
# Create your views here.
from .. models import Goods,Types
from . typesviews import paixu
from . userviews import uploads
import os
def add(request):
	
	if request.method == 'GET':
		tlist = paixu()
		context = {'tlist':tlist}
		return render(request,'myadmin/goods/add.html',context)
	elif request.method == 'POST':
		#判断是否上传了图片
		if not request.FILES.get('pic',None):
			return HttpResponse('<script>alert("必须上传一张图片");location.href="'+reverse('myadmin_goods_add')+'"</script>')
		pic = uploads(request)
		if pic == 1:
			return HttpResponse('<script>alert("图片上传类型错误");location.href="'+reverse('myadmin_goods_add')+'"</script>')

		#执行添加 接受挑担提交的数据
		data = request.POST.copy().dict()
		#删除点 cref验证的字段数据
	
		del data['csrfmiddlewaretoken']
		#添加pics 
		
		data['pics'] = pic
		print(data)
		data['typeid'] = Types.objects.get(id = data['typeid'])
	
		#执行用户的创建
		ob = Goods.objects.create(**data)

		return HttpResponse('<script>alert("添加成功");location.href="'+reverse('myadmin_goods_list')+'"</script>')
		
def list(request):
	
	# 获取搜索条件
	goods = request.GET.get('type',None)
	keywords = request.GET.get('keywords',None)

	if goods:
		#有搜索条件
		if goods == 'all':
			#全条件搜索

			from django.db.models import Q

			goodslist = Goods.objects.filter(
                Q(id__contains=keywords)|
                Q(title__contains=keywords)|
                Q(price__contains=keywords)|
                Q(clicknum__contains=keywords)|
                Q(num__contains=keywords)
            )
     
		elif goods == 'id':
			goodslist = Goods.objects.filter(id__contains=keywords)
		elif goods == 'title':
			goodslist = Goods.objects.filter(title__contains=keywords)
		elif goods == 'price':
			goodslist = Goods.objects.filter(price__contains=keywords)

		elif goods == 'clicknum':
			goodslist = Goods.objects.filter(clicknum__contains=keywords)
		elif goods == 'num':
			goodslist = Goods.objects.filter(num__contains=keywords)
		elif goods == 'typeid':
			goodslist = Goods.objects.filter(typeid__name__contains=keywords)
	else:
		#获取所有数据
		goodslist = Goods.objects.filter()
		# print(goodslist.pid)
		# print(goodslist)
	# for x in goodslist:
	# 	if x.pid == 0:
	# 		x.pname = '顶级分类'
	# 	else:
	# 		t = Types.objects.get(id=x.pid)
	# 		x.pname = t.name
	# 		num  = x.path.count(',')-1
	# 		x.name = (num*'|----')+x.name


	#导分页类
	from  django.core.paginator import Paginator

	#实例化对象 参数1是数据集和 参数2是每页显示的条数
	paginator = Paginator(goodslist,2)
	#获取当前的页码数
	p = request.GET.get('p',1)

	# 获取当前页码的数据
	gllist = paginator.page(p)
	#分配数据
	context = {'glist':gllist}


	return render(request,'myadmin/goods/list.html',context)





def delete(request):
	
	try:
		tid = request.GET.get('uid',None)
		print(tid)
		ob = Goods.objects.get(id=tid)

		#判断当前用户是否头像，如果有则删除
		if ob.pics:
			os.remove('.'+ob.pics)
			ob.delete()

		data = {'msg':'删除成功','code':0}
	except:
		data = {'msg':'删除失败','code':1}

	return JsonResponse(data)
#修改
def edit(request):
	
	#接受参数

	uid = request.GET.get('uid',None)
	
	#获取对象

	ob = Goods.objects.get(id=uid)


	

	if request.method == 'GET':

		#分配数据
		tlist = paixu()

		context = {'tlist':tlist,'uinfo':ob}

		#显示编辑页面

		return render(request,'myadmin/goods/edit.html',context)

	elif  request.method == 'POST':

			
		# try: 
	 #判断是否上传了新的图片
		if request.FILES.get('pic',None):
            # 判断是否使用的默认图
			if ob.pics:
                # 如果使用的不是默认图,则删除之前上传的头像
				os.remove('.'+ob.pics)

            # 执行上传
			ob.pics = uploads(request)
		ob.typeid =Types.objects.get(id=request.POST['typeid'])
		ob.title = request.POST['title']
		ob.descr = request.POST['descr']

		ob.price = request.POST['price']

		ob.store = request.POST['store']
		ob.info = request.POST['info']

		ob.save()

		return HttpResponse('<script>alert("更新成功");location.href="'+reverse('myadmin_goods_list')+'"</script>')

		# except:
		# 	return HttpResponse('<script>alert("更新失败");location.href="'+reverse('myadmin_goods_list')+'"</script>')





