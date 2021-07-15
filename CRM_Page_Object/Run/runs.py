# Solar
# handsome
from HTMLTestRunner import HTMLTestRunner
import os
import time
import unittest
from time import sleep
from CRM_Page_Object.Case.addyuangong import MyTestCase

# 获取当前文件的路径
lujing = os.getcwd ()

# 把最后的文件劈分掉
lujing1 = os.path.split (lujing)

# 劈分的结果第一个元素和要存放的html目录进行拼接
# lujing2 = os.path.join (lujing1 [0],'HTMLshengcheng')
lujing2 = 'D:/pythonbao/CRM_Page_Object/HTMLshengcheng/'

# 格式化时间
t = time.strftime ('%Y-%m-%d-%H-%M-%S')

# 拼接html后缀
t1 = t + '_result.html'

# 把存放的html文件路径和生成的文件名拼接起来
lujing3 = 'D:/pythonbao/CRM_Page_Object/HTMLshengcheng/' + t1

# 设定要跑什么模块
su = unittest.TestSuite ()
su.addTest (MyTestCase ('test_1addyuangong'))

# 打开这个文件写入内容
file = open (lujing3,'wb')

# 跑脚本
runner = HTMLTestRunner (stream = file, verbosity = 2, title = 'CRM新增员工', description = '详情如下：')
runner.run (su)

# 跑完关闭
sleep (2)
file.close ()