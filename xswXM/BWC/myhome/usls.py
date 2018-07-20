from django.conf.urls import url
from . import views

urlpatterns = [

	#首页
	url(r'^$',views.index,name="myhome_index"),
	#列表
	url(r'^list/(?P<tid>[0-9]+)/$',views.list,name="myhome_list"),
	#详情
	url(r'^info/(?P<sid>[0-9]+)/$',views.info,name="myhome_info"),
	#登录
	url(r'^login/$',views.login,name="myhome_login"),
	#退出登录
	url(r'^logout/$',views.logout,name="myhome_logout"),
	#注册
	url(r'^register/$',views.register,name="myhome_register"),
	#验证吗
	url(r'^vcode/$',views.vcode,name="myhome_vcode"),
	#搜索
	url(r'^search/$',views.search,name="myhome_search"),

	#购物车
	#加入商品到购物车
	url(r'^addcart/$',views.addcart,name="myhome_addcart"),
	#购物车列表
	url(r'^cartlist/$',views.cartlist,name="myhome_cartlist"),
	#删除购物车一个商品
	url(r'^delcart/$',views.delcart,name="myhome_delcart"),
	#清空购物车
	url(r'^cartclear/$',views.cartclear,name="myhome_cartclear"),
	#修改购物车数量
	url(r'^editcart/$',views.editcart,name="myhome_editcart"),

	# 订单
    #  订单确认页面
    url(r'^ordercheck/$', views.ordercheck,name='myhome_ordercheck'),
    url(r'^addressedit/$', views.addressedit,name='myhome_addressedit'),
    url(r'^addressadd/$', views.addressadd,name='myhome_addressadd'),
    #  订单生成
    url(r'^ordercreate/$', views.ordercreate,name='myhome_ordercreate'),

    #  支付
    url(r'^buy/$', views.buy,name='myhome_buy'),

    #  支付成功


    # 个人中心
    url(r'^mycenter/$', views.mycenter,name='myhome_mycenter'),
    # 我的订单
    url(r'^myorders/$', views.myorders,name='myhome_myorders'),
    #个人信息
    url(r'^mygrxx/$', views.mygrxx,name='myhome_mygrxx'),
    #安全设置
    url(r'^mysafety/$', views.mysafety,name='myhome_mysafety'),
    #安全设置修改密码
    url(r'^mypassword/$', views.mypassword,name='myhome_mypassword'),
    #地址管理
    url(r'^myaddress/$', views.myaddress,name='myhome_myaddress'),
]
