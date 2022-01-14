import pymysql

from PHHCDataPro.settings import DATABASES
from cus_rule.models import OneObjectRule
from cus_rule.service.IdWorker import IdWorker


def add_kjywsj_general_name():
    # 读取数据库，获取个性化规则数据。
    # 转换为规则数据
    # 保存数据库

    # # 连接数据库
    dbconfig = 'default'
    db = pymysql.connect(DATABASES.get(dbconfig).get('HOST'), DATABASES.get(dbconfig).get('USER'),
                         DATABASES.get(dbconfig).get('PASSWORD'),
                         DATABASES.get(dbconfig).get('NAME'), int(DATABASES.get(dbconfig).get('PORT')))

    # 使用cursor()方法创建一个游标对象
    cursor = db.cursor()

    # 使用execute()方法执行SQL语句
    cursor.execute("SELECT * FROM 药物送检提醒_本院药品通用名")

    # 使用fetall()获取全部数据
    data = cursor.fetchall()

    # 打印获取到的数据
    for data_item in data:

        print(data_item[0])
        drug_name_list = data_item[0].split('||', -1)
        for drug_name in drug_name_list:
            本院药品通用名 = drug_name
            病原学送检_元素判断逻辑 = data_item[1]
            病原学送检_项目名称 = data_item[2]
            病原学送检_集合判断逻辑 = data_item[3]
            结果 = data_item[4]
            依据 = data_item[5]
            提示信息 = data_item[6]

            oneObjectRule = OneObjectRule()
            oneObjectRule.OneObjectRuleID = IdWorker(1, 2, 0).get_id()
            oneObjectRule.Module = 'AntiDrugEtiologyExam'
            oneObjectRule.ObjectType = 'drugGeneralName'
            oneObjectRule.ObjectLogic = 1
            oneObjectRule.ObjectValue = 本院药品通用名

            oneObjectRule.ConditionDesc = ''
            oneObjectRule.JudgeDesc = '【病原学送检】' + '（除外）' + '[' + 病原学送检_元素判断逻辑 + ']' + 病原学送检_项目名称
            oneObjectRule.ConclusionDesc = ''

            oneObjectRule.ConditionContent = ''
            oneObjectRule.JudgeContent = ''
            ruleDataType

            oneObjectRule.ConclusionContent = ''

            oneObjectRule.RuleSourceTypeID = 1
            oneObjectRule.DataSourceID = 1
            oneObjectRule.RuleType = 1
            oneObjectRule.RuleLevel = 1

            oneObjectRule.RulePriority = 1
            oneObjectRule.RuleTips = 1
            oneObjectRule.RuleDESC = 1
            oneObjectRule.Remark = 1
            oneObjectRule.IsEnable = 1
            oneObjectRule.CreateTime = 1
            oneObjectRule.CreateUser = 1

    # 关闭游标和数据库的连接
    cursor.close()
    db.close()

    return 1


add_kjywsj_general_name()
