conf文件夹使用规则：
    1.local_config.ini作为模版
    2.自己使用local_config.ini时候，复制local_config.ini文件然后重命名为local_config加下划线'_'延伸命名，以防文件冲突
  例如：我的为local_config_lby.ini
    3.如果根据base_page进行调用必须走local_config.ini时候，自行修改自己的代码，对local_config.ini只能进行添加操作，其他操作由管理员操作
  例如：原有user中的帐号密码是：
      [user]
        user_name = admin
        password  = Yizudedipan123456
     变更为：
      [user]
        user_name = admin
        password  = Yizudedipan123456
        user_name_liu = liuboyan1
        password_liu = *****
     通过在原有的命名基础上加'_'进行延伸命名