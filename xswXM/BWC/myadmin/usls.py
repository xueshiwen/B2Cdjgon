from django.conf.urls import url

from . views import views,userviews,typesviews,goodsviews,orderviews,authviews

urlpatterns = [
	
    #会员添加
    url(r'^user/add$', userviews.add,name='myadmin_user_add'),
    #会员列表
    url(r'^user/list$', userviews.list,name='myadmin_user_list'),
    #会员删除
    url(r'^user/delete$', userviews.delete,name='myadmin_user_delete'),
    #会员修改
    url(r'^user/edit$', userviews.edit,name='myadmin_user_edit'),

    #分类管理
    url(r'^types/add$', typesviews.add,name='myadmin_types_add'),
    url(r'^types/list$', typesviews.list,name='myadmin_types_list'),
    url(r'^types/delete$', typesviews.delete,name='myadmin_types_delete'),
    url(r'^types/edit$', typesviews.edit,name='myadmin_types_edit'),

    #商品管理
    url(r'^goods/add$', goodsviews.add,name='myadmin_goods_add'),
    url(r'^goods/list$', goodsviews.list,name='myadmin_goods_list'),
    url(r'^goods/delete$', goodsviews.delete,name='myadmin_goods_delete'),
    url(r'^goods/edit$', goodsviews.edit,name='myadmin_goods_edit'),
    
    #订单管理
    url(r'^order/order$', orderviews.list,name='myadmin_order_list'),
    url(r'^order/info$', orderviews.info,name='myadmin_order_info'),


    #登录页面
    url(r'^login/$', authviews.mylogin,name='myadmin_login'),
    #退出登录
    url(r'^loginout/$', authviews.myloginout,name='myadmin_loginout'),

    #后台权限管理
    #后台用户添加
    url(r'^auth/user/add$', authviews.useradd,name='auth_user_add'),
    #后台用户列表
    url(r'^auth/user/list$', authviews.userlist,name='auth_user_list'),

    #后台组添加
    url(r'^auth/group/add$', authviews.groupadd,name='auth_group_add'),
    #后台组列表
    url(r'^auth/group/list$', authviews.grouplist,name='auth_group_list'),
    #后台组编辑
    url(r'^auth/group/edit/(?P<gid>[0-9]+)$', authviews.groupedit,name='auth_group_edit'),
    #后台删除
    url(r'^auth/group/del/(?P<uid>[0-9]+)$', authviews.userdel,name='auth_user_del'),
    
    url(r'^', userviews.list),



]
