from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from django.contrib.auth.models import User,Permission,Group
from django.contrib.auth import authenticate, login,logout



#管理元用户添加
def useradd(request):

	if request.method == 'GET':

		#获取所有组
		glist = Group.objects.all()

		context = {'glist':glist}
		#显示添加页面
		return render(request,'auth/user/add.html',context)

	elif request.method == 'POST':
		#执行管理员添加

		#判断是否是超级用户还是普通用户
		if request.POST['is_superuser'] == '1':

			ob = User.objects.create_superuser(request.POST['username'],request.POST['email'],request.POST['password'],)
		else:
			ob = User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'],)
		#进行添加
		ob.save()

		#判断是否为用户分配组
		gs = request.POST.getlist('gs',None)
		if gs:
			#给当前用户分组
			ob.groups.set(gs)
			ob.save()
		return HttpResponse('<script>location.href="/myadmin/auth/user/list"</script>')

#管理员用户列表
def userlist(request):

	#获取所有的管理员
	data = User.objects.all()

	context = {'ulist':data}
	return	render(request,'auth/user/list.html',context)




#管理组添加
def groupadd(request):

	if request.method == 'GET':

		#获取所有权限
		# perm = Permission.objects.all()
		# 读取所有权限信息,并排除以Can开头的系统默认生成权限
		perms = Permission.objects.exclude(name__istartswith='Can')
		context = {'perm':perms}
		return render(request,'auth/group/add.html',context)
	elif request.method == 'POST':

		#创建组
		g = Group(name=request.POST['name'])
		g.save()

		#获取组的所有权限
		prms = request.POST.getlist('prms',None)
		#判断是否给组分配权限
		if prms:

				#给组分配权限
			g.permissions.set(prms)
			g.save()
		return HttpResponse('<script>location.href="/myadmin/auth/group/list"</script>')




#管理组列表
def grouplist(request):
	#获取所有组
	data = Group.objects.all()

	context = {'glist':data}
	return render(request,'auth/group/list.html',context)



#编辑组

def groupedit(request,gid):

	#获取当钱组的信息
	ginfo = Group.objects.get(id=gid)

	if request.method == 'GET':
	
	 # 读取所有权限信息,并排除已经有的权限
		perms = Permission.objects.exclude(group=ginfo).exclude(name__istartswith='Can')
		#分配数据
		context = {'ginfo':ginfo,'perms':perms}

		return render(request,'auth/group/edit.html',context)
	elif request.method == 'POST':

		#修改组名

		ginfo.name = request.POST['name']

		#判断是否有权限
		prms = request.POST.getlist('prms',None)

		#全部删除，在添加
		g.permissions.clear()
		if prms:

			# 添加权限

			ginfo.permissions.set(prms)

		ginfo.save()
		
		return HttpResponse('<script>location.href="/myadmin/auth/group/list"</script>')


# 管理员删除
def userdel(request,uid):

    ob = User.objects.get(id=uid)
    ob.delete()
    return HttpResponse('<script>location.href="/myadmin/auth/user/list"</script>')
    



	
#后台登录
def mylogin(request):
	 # 如果访问当前页面的请求方式为GET ,则返回一个登录页面
    if request.method == 'GET':
        return render(request,'myadmin/login.html')

    elif request.method == 'POST':

        # 执行登录
        # 判断验证码是否正确
        if request.POST['vcode'].lower() != request.session['verifycode'].lower():
            return HttpResponse('<script>alert("验证码错误");location.href="/myadmin/login/"</script>')
        
        # 使用django提供的后台用户验证方法
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            #登录
            login(request,user)
            return HttpResponse('<script>location.href="/myadmin/user/list"</script>')

        return HttpResponse('<script>alert("用户名或密码不存在");location.href="/myadmin/login/"</script>')


def myloginout(request):
    # 退出登录
	logout(request)
	return HttpResponse('<script>alert("退出登录成功");location.href="/myadmin/login/"</script>')
