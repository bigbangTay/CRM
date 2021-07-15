# Solar
# handsome
import unittest
from CRM_Page_Object.Base.caozuo import *
from selenium.webdriver.common.by import By
from time import sleep
import random
from selenium.webdriver.support.select import Select
from CRM_Page_Object.Data.data import *
from selenium import webdriver

class MyTestCase (FangFa) :

    ran = [chr (i) for i in range (65, 91)] + [chr (i) for i in range (97, 123)] + [str (i) for i in range (10)]

    def test_1addyuangong (self) :

        # 点击管理员且点击添加员工，然后切换到工作台
        self.frame (self.driver.find_elements_by_tag_name ('frame')[1])
        self.find (By.XPATH,'/html/body/table/tbody/tr[2]/td/table'
                            '/tbody/tr[4]/td/table/tbody/tr[1]/td/table/tbody').click ()
        self.find (By.LINK_TEXT,'添加员工').click ()
        self.driver.switch_to.default_content ()
        self.frame (self.driver.find_elements_by_tag_name ('frame')[2])

        name = 'Solar' + str (random.randint(1001,2000))
        self.find (By.NAME,'userName').send_keys (name)

        age = random.randint (1,100)
        self.find (By.NAME,'userAge').send_keys (age)

        # 先获取性别的下拉框，再随机选值
        sex = self.find (By.NAME,'userSex')
        sex.click ()
        sleep (1)
        values = random.randint (0,1)
        Select (sex).select_by_index (values)
        sex.click ()

        # 学历同理
        userDiploma = self.find (By.NAME,'userDiploma')
        userDiploma.click ()
        sleep (1)
        values1 = random.randint (0,4)
        Select (userDiploma).select_by_index (values1)
        userDiploma.click ()

        # 部门同理
        departmentId = self.find (By.NAME,'departmentId')
        departmentId.click ()
        sleep(1)
        values2 = random.randint (0,2)
        Select (departmentId).select_by_index (values2)
        departmentId.click ()

        # 座机
        zuoji = '028-' + str (random.randint (10000000, 99999999))
        self.find (By.CSS_SELECTOR,'[valid = "isPhone"]').send_keys (zuoji)

        # 工资卡号
        kahao = '622280' + str (random.randint (1000000000000, 9999999999999))
        self.find (By.CSS_SELECTOR,'[valid = "isNumber"]').send_keys (kahao)

        # 身份证
        year = str (random.randint (1930,2021))
        month = str (random.randint (1,9))
        day = str (random.randint (10,28))
        three = str (random.randint (100,999))
        cho = [str (i) for i in range (10)] + ['X']
        last = str (random.choice (cho))
        shenfen = '511011' + year + '0' + month + day + three + last
        self.find (By.CSS_SELECTOR,'[valid = "isIdCard"]').send_keys (shenfen)

        # 添加人
        self.driver.implicitly_wait (3)
        self.driver.switch_to.default_content()
        self.frame (self.driver.find_elements_by_tag_name ('frame')[0])
        person = self.find (By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table'
                                     '/tbody/tr/td[1]/table/tbody/tr/td[2]/div').text
        person1 = person.split ('：')
        self.driver.switch_to.default_content ()
        self.frame (self.driver.find_elements_by_tag_name ('frame')[2])
        self.find (By.NAME,'userAddman').send_keys (person1 [1])

        # 账号
        us = (random.choice (self.ran) for i in range (10))
        us1 = ''
        for i in us :
            us1 += i
        self.find (By.NAME,'userNum').send_keys (us1)

        # 密码
        pw = (random.choice (self.ran) for i in range (6))
        pw1 = ''
        for i in pw :
            pw1 += i
        self.find (By.NAME,'userPw').send_keys (pw1)

        # 民族
        minzu = ['维吾尔族', '汉族', '壮族', '傣族', '藏族', '水族']
        minzu1 = random.choice (minzu)
        self.find (By.NAME,'userNation').send_keys (minzu1)

        # 婚姻
        isMarried = self.find (By.NAME,'isMarried')
        isMarried.click ()
        sleep (1)
        values3 = random.randint (0,2)
        Select (isMarried).select_by_index (values3)
        isMarried.click ()

        # 角色
        roleId = self.find (By.NAME,'roleId')
        roleId.click ()
        sleep (1)
        values4 = random.randint (0,2)
        Select (roleId).select_by_index (values4)
        roleId.click ()

        # 爱好
        hobby = ['打篮球', '乒乓球', '羽毛球', '游泳', '健身', '滑雪', 'lol']
        hobby1 = random.choice (hobby)
        self.find (By.NAME,'userIntest').send_keys (hobby1)

        # 手机
        last1 = (random.randint (0,9) for i in range (8))
        phone = '183'
        for i in last1:
            phone += str (i)
        self.find (By.CSS_SELECTOR,'[valid = "regexp"]').send_keys (phone)

        # 地址
        address = ['四川省成都市', '首都北京市', '广东省深圳市', '广东省广州市', '上海市']
        address1 = random.choice (address)
        self.find (By.NAME,'userAddress').send_keys (address1)

        # E_mail
        qq1 = random.randint (1,9)
        qq2 = (random.randint (0,9) for i in range (8))
        qq3 = ''
        for i in qq2:
            qq3 += str (i)
        email = ['@qq.com','@163.com']
        email1 = str (qq1) + qq3 + random.choice (email)
        self.find (By.NAME,'userEmail').send_keys (email1)

        # 添加按钮
        self.find (By.NAME,'submit').click ()

        # 获取提示框的文本
        sleep (2)
        notice = self.driver.switch_to.alert.text
        sleep (2)
        self.driver.switch_to.alert.accept ()

        # 断言文本
        self.assertEqual ('员工添加成功',notice,'添加失败')

        # 数据库断言
        sleep (2)
        chaxun = Selects ('localhost', 'root', '123456', 'crm')
        result = chaxun.can (f'SELECT user_name from user_info where user_name = "{name}"')
        if result == name :
            print (f'数据库查询结果：添加成功\n员工姓名为：{name}')
        else:
            print (f'数据库查询结果：添加失败\n员工姓名为：{name}')

if __name__ == '__main__' :
    unittest.main ()