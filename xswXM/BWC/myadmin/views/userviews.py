from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
# Create your views here.
from .. models import Users
import os
from django.contrib.auth.decorators import permission_required

#显示添加页面 也就是表单 
@permission_required('myadmin.insert_users',raise_exception = True)
def add(request):

	if request.method == 'GET':
		#则显示添加页面
		return render(request,'myadmin/user/add.html')
	elif request.method == 'POST':
		#则执行数据添加
		try:
			#接受表单用POST提交过来的数据
			data = request.POST.copy().dict()

			#删除掉csrf验证的字段数据
			del data['csrfmiddlewaretoken']

			#进行密码加密

			from django.contrib.auth.hashers import make_password, check_password

			# 进行用户头像上传

			if request.FILES.get('pic',None):
				data['pic'] = uploads(request)
				if data['pic'] == 1:

					return HttpResponse('<script>alert("上传的类型不符");location.href="'+reverse('myadmin_user_add')+'"</script>')
			else:
				del data['pic']

			ob = Users.objects.create(**data)

			return HttpResponse('<script>alert("添加成功");location.href="'+reverse('myadmin_user_list')+'"</script>')
		except:

			return HttpResponse('<script>alert("添加失败");location.href="'+reverse('myadmin_user_add')+'"</script>')


#列表
@permission_required('myadmin.show_users',raise_exception = True)
def list(request):

	#获取搜索条件
	types = request.GET.get('type',None)
	keywords = request.GET.get('keywords',None)


	if types:
        # 有搜索条件
		if types == 'all':
            # 全条件搜索
            
			from django.db.models import Q
			userlist = Users.objects.filter(
                Q(username__contains=keywords)|
                Q(age__contains=keywords)|
                Q(email__contains=keywords)|
                Q(phone__contains=keywords)|
                Q(sex__contains=keywords)
            )
		elif types == 'username':
            # 按照用户名搜索
			userlist = Users.objects.filter(username__contains=keywords)
        
		elif types == 'age':
            # 按照年龄搜索
			userlist = Users.objects.filter(age__contains=keywords)

		elif types == 'email':
            # 按照 email 搜索
			userlist = Users.objects.filter(email__contains=keywords)

		elif types == 'phone':
            # 按照 phone 搜索
			userlist = Users.objects.filter(phone__contains=keywords)

		elif types == 'sex':
            # 按照 sex 搜索
			userlist = Users.objects.filter(sex__contains=keywords)


	else:
        # 获取所有的用户数据
		userlist = Users.objects.filter()

	#导份分页类
	from  django.core.paginator import Paginator

	#实力话对象 参数1 是数据集合 参数2是每页显示的条数

	paginator = Paginator(userlist,10)
	#获取当前的页码书
	p = request.GET.get('p',1)

	#获取当前的页码数据
	ulist = paginator.page(p)

	#获取当前的页码range

	
	#分配数据
	context = {'userlist':ulist,}
	#加载模板

	return render(request,'myadmin/user/list.html',context)

# 会员删除
@permission_required('myadmin.del_users',raise_exception = True)

def delete(request):
	try:
		uid = request.GET.get('uid',None)
		ob = Users.objects.get(id=uid)

		# 判断当前用户是否有头想，如果有删除
		if ob.pic:
			os.remove('.'+ob.pic)
		ob.delete()

		data = {'msg':'删除成功'}
	except:
		data = {'msg':'删除失败'}
	return JsonResponse(data)
@permission_required('myadmin.edit_users',raise_exception = True)

def edit(request):
	#接受参数
	uid = request.GET.get('uid',None)
	if not uid:
		return HttpResponse('<script>alert("没有用户数据");location.href="'+reverse('myadmin_user_list')+'"</script>')

	# 获取对像

	ob = Users.objects.get(id=uid)

	if request.method == 'GET':

		#分配数据
		context = {'uinfo':ob}

		#显示编辑页面
		return render(request,'myadmin/user/edit.html',context)

	elif request.method == 'POST':

		try:
			# 判断是否上传啦新的图片
			if request.FILES.get('pic',None):

				#判断是否用了默认图
				if ob.pic:

					#如果使用的不是默认图，泽删除之前的头像
					os.remove('.'+ob.pic)

				#执行上穿
				ob.pic = uploads(request)


			ob.username = request.POST['username']
			ob.email = request.POST['email']
			ob.age = request.POST['age']
			ob.sex = request.POST['sex']
			ob.phone = request.POST['phone']
			ob.save()
			
	
			
			return HttpResponse('<script>alert("更新成功");location.href="'+reverse('myadmin_user_list')+'"</script>')
		except:	
			return HttpResponse('<script>alert("更新成功");location.href="'+reverse('myadmin_user_edit')+'"</script>')
# 执行文件头像的上传 封装函数
def uploads(request):

	# 获取请求中的文件 File

	myfile = request.FILES.get('pic',None)

	# 获取上传文件的后缀名 
	p = myfile.name.split('.').pop()

	arr = ['jpg','png','jpeg','gif']

	if p not in arr:
		return 1 

	import time,random

	# 生成新的文件名

	filename = str(time.time())+str(random.randint(1,99999))+'.'+p

	# 打开文件

	destin = open("./static/pics"+filename,"wb+")

	# 分块写入文件
	for chunk in myfile.chunks():      
	   destin.write(chunk)

	#关闭文件
	destin.close()

	return '/static/pics'+filename