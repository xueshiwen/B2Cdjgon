from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
# Create your views here.
from .. models import Types

def add(request):

	if request.method == 'GET':

		#获取当前数据库中所有分类
		tlist = paixu()
		context = {'tlist':tlist}
		#返回一个添加的页面
		return render(request,'myadmin/types/add.html',context)
	
	elif request.method == 'POST':

		ob=Types()

		ob.name = request.POST['name']

		ob.pid = request.POST['pid']
		if ob.pid == '0':
			ob.path = '0,'
		else:
			#根据获取父级的id来获取path,在添加父级id

			t = Types.objects.get(id=ob.pid)
			ob.path = t.path + str(ob.pid)+','
		ob.save()
	
		return HttpResponse('<script>alert("添加成功");location.href="'+reverse('myadmin_types_list')+'"</script>')


def list(request):

	#获取搜索条件
	types = request.GET.get('type',None)
	keywords = request.GET.get('keywords',None)

	if types:
		#有搜索条件
		if types == 'all':

			#全条件搜索
			from django.db.models import Q
			typeslist = Types.objects.filter(name__contains=keywords)
			# typeslist = paixu()

		elif types == 'name':
			typeslist = Types.objects.filter(name__contains=keywords)
			# typeslist = paixu()

	else:
		#获取所有用户数据
		
		typeslist = Types.objects.extra(select = {'paths':'concat(path,id)'}).order_by('paths')
		
	for x in typeslist:
		if x.pid == 0:
			x.pname = '顶级分类'
		else:
			t = Types.objects.get(id=x.pid)
			x.pname = t.name
			num  = x.path.count(',')-1
			x.name = (num*'|----')+x.name
	#导分分页累
	from  django.core.paginator import Paginator

	#实例化对象 参数1 是数据集合 参数2是每页显示的条数
	paginator = Paginator(typeslist,3)
	#获取当前页码数
	p = request.GET.get('p',1)

	#获取当前页码的数据
	ylist = paginator.page(p)
	#调用paixu函数
	# tlist = paixu(request)
	#分配数据
	context = {'tylist':ylist}

	return render(request,'myadmin/types/list.html',context,)

def delete(request):
	tid = request.GET.get('uid',None)
	#判断是否是子类
	num = Types.objects.filter(pid=tid).count()

	if num != 0:
		data = {'msg':'当前有子类，不能删除','code':1}
	else:
		ob = Types.objects.get(id=tid)
		ob.delete()
		data = {'msg':'删除成功','code':0}

	return JsonResponse(data)
def edit(request):
	#接受参数
	uid = request.GET.get('uid',None)
	if not uid:
		return HttpResponse('<script>alert("没有用户数据");location.href="'+reverse('myadmin_types_list')+'"</script>')

	#获取对象
	ob = Types.objects.get(id=uid)

	
	if request.method == 'GET':
		tlist = paixu()
		#分配数据
		context = {'uinfo':ob,'tlist':tlist}

		#显示编辑页面
		return render(request,'myadmin/types/edit.html',context)
	elif request.method == 'POST':

		try:
			ob.name = request.POST['name']
			ob.path = request.POST['path']
			ob.save()
			return HttpResponse('<script>alert("更新成功");location.href="'+reverse('myadmin_types_list')+'"</script>')
		except:
			return HttpResponse('<script>alert("更新失败");location.href="'+reverse('myadmin_types_list')+'"</script>')
			

#定义分配函数
def paixu():

	tlist = Types.objects.extra(select = {'paths':'concat(path,id)'}).order_by('paths')
		

	for x in tlist:
		if x.pid == 0:
			x.pname = '顶级分类'
		else:
			t = Types.objects.get(id=x.pid)
			x.pname = t.name
			num  = x.path.count(',')-1
			x.name = (num*'|----')+x.name


	return tlist