from django.http import JsonResponse


def many_obj_condi_conclu(request):
    audit_item_id = request.GET['audit_item_id']
    curr_manage_index = request.GET['curr_manage_index']

    data_list = []
    if audit_item_id == '抗菌药物分级管理':
        if curr_manage_index == '按抗菌药物分级管理':
            data_list = [{"依据": "说明书", "项目": "特殊级抗菌药物", "触发条件": "", "审核结果": "<span style='color:green;'>适宜</span>"
                             , "备注": "123123123", "状态": "<span style='color:green;'>启用</span>"
                             , "级别": "<span style='color:blue;'>提示</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "规则结论": "【开药天数】3天"}
                , {"依据": "说明书", "项目": "特殊级抗菌药物", "触发条件": "", "审核结果": "<span style='color:green;'>适宜</span>",
                   "备注": "123123123", "状态": "<span style='color:green;'>启用</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "级别": "<span style='color:red;'>强制</span>"
                             , "规则结论": "【开药天数】3天"}
                , {"依据": "说明书", "项目": "限制级抗菌药物", "触发条件": "", "审核结果": "<span style='color:green;'>适宜</span>",
                   "备注": "123123123", "状态": "<span style='color:green;'>启用</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "级别": "<span style='color:red;'>强制</span>"
                             , "规则结论": "【开药天数】3天"}
                , {"依据": "说明书", "项目": "限制级抗菌药物", "触发条件": "", "审核结果": "<span style='color:red;'>不适宜</span>",
                   "备注": "123123123", "状态": "<span style='color:#c8c8c8;'>停用</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "级别": "<span style='color:red;'>强制</span>"
                             , "规则结论": "【开药天数】3天"}]
        elif curr_manage_index == '本院药品通用名':
            data_list = [{"依据": "说明书", "项目": "阿司匹林肠溶片", "触发条件": "", "审核结果": "<span style='color:green;'>适宜</span>"
                             , "备注": "123123123", "状态": "<span style='color:green;'>启用</span>"
                             , "级别": "<span style='color:blue;'>提示</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "规则结论": "【开药天数】3天"}
                , {"依据": "说明书", "项目": "阿莫西林分散片", "触发条件": "", "审核结果": "<span style='color:green;'>适宜</span>",
                   "备注": "123123123", "状态": "<span style='color:green;'>启用</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "级别": "<span style='color:red;'>强制</span>"
                             , "规则结论": "【开药天数】3天"}
                , {"依据": "说明书", "项目": "万古霉素注射液", "触发条件": "", "审核结果": "<span style='color:green;'>适宜</span>",
                   "备注": "123123123", "状态": "<span style='color:green;'>启用</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "级别": "<span style='color:red;'>强制</span>"
                             , "规则结论": "【开药天数】3天"}
                , {"依据": "说明书", "项目": "注射用庆大霉素", "触发条件": "", "审核结果": "<span style='color:red;'>不适宜</span>",
                   "备注": "123123123", "状态": "<span style='color:#c8c8c8;'>停用</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "级别": "<span style='color:red;'>强制</span>"
                             , "规则结论": "【开药天数】3天"}]
        elif curr_manage_index == '本院药品通用名规格':
            data_list = [{"依据": "说明书", "项目": "阿司匹林肠溶片20mg", "触发条件": "", "审核结果": "<span style='color:green;'>适宜</span>"
                             , "备注": "123123123", "状态": "<span style='color:green;'>启用</span>"
                             , "级别": "<span style='color:blue;'>提示</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "规则结论": "【开药天数】3天"}
                , {"依据": "说明书", "项目": "阿莫西林分散片10mg", "触发条件": "", "审核结果": "<span style='color:green;'>适宜</span>",
                   "备注": "123123123", "状态": "<span style='color:green;'>启用</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "级别": "<span style='color:red;'>强制</span>"
                             , "规则结论": "【开药天数】3天"}
                , {"依据": "说明书", "项目": "万古霉素注射液5mg", "触发条件": "", "审核结果": "<span style='color:green;'>适宜</span>",
                   "备注": "123123123", "状态": "<span style='color:green;'>启用</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "级别": "<span style='color:red;'>强制</span>"
                             , "规则结论": "【开药天数】3天"}
                , {"依据": "说明书", "项目": "注射用庆大霉素3mg", "触发条件": "", "审核结果": "<span style='color:red;'>不适宜</span>",
                   "备注": "123123123", "状态": "<span style='color:#c8c8c8;'>停用</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "级别": "<span style='color:red;'>强制</span>"
                             , "规则结论": "【开药天数】3天"}]
        elif curr_manage_index == '本院药品通用名规格厂家':
            data_list = [{"依据": "说明书", "项目": "阿司匹林肠溶片20mg", "触发条件": "", "审核结果": "<span style='color:green;'>适宜</span>"
                             , "备注": "123123123", "状态": "<span style='color:green;'>启用</span>"
                             , "级别": "<span style='color:blue;'>提示</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "规则结论": "【开药天数】3天"}
                , {"依据": "说明书", "项目": "阿莫西林分散片10mg", "触发条件": "", "审核结果": "<span style='color:green;'>适宜</span>",
                   "备注": "123123123", "状态": "<span style='color:green;'>启用</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "级别": "<span style='color:red;'>强制</span>"
                             , "规则结论": "【开药天数】3天"}
                , {"依据": "说明书", "项目": "万古霉素注射液5mg", "触发条件": "", "审核结果": "<span style='color:green;'>适宜</span>",
                   "备注": "123123123", "状态": "<span style='color:green;'>启用</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "级别": "<span style='color:red;'>强制</span>"
                             , "规则结论": "【开药天数】3天"}
                , {"依据": "说明书", "项目": "注射用庆大霉素3mg", "触发条件": "", "审核结果": "<span style='color:red;'>不适宜</span>",
                   "备注": "123123123", "状态": "<span style='color:#c8c8c8;'>停用</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "级别": "<span style='color:red;'>强制</span>"
                             , "规则结论": "【开药天数】3天"}]
        elif curr_manage_index == '本院药品编码':
            data_list = [{"依据": "说明书", "项目": "阿司匹林肠溶片20mg", "触发条件": "", "审核结果": "<span style='color:green;'>适宜</span>"
                             , "备注": "123123123", "状态": "<span style='color:green;'>启用</span>"
                             , "级别": "<span style='color:blue;'>提示</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "规则结论": "【开药天数】3天"}
                , {"依据": "说明书", "项目": "阿莫西林分散片10mg", "触发条件": "", "审核结果": "<span style='color:green;'>适宜</span>",
                   "备注": "123123123", "状态": "<span style='color:green;'>启用</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "级别": "<span style='color:red;'>强制</span>"
                             , "规则结论": "【开药天数】3天"}
                , {"依据": "说明书", "项目": "万古霉素注射液5mg", "触发条件": "", "审核结果": "<span style='color:green;'>适宜</span>",
                   "备注": "123123123", "状态": "<span style='color:green;'>启用</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "级别": "<span style='color:red;'>强制</span>"
                             , "规则结论": "【开药天数】3天"}
                , {"依据": "说明书", "项目": "注射用庆大霉素3mg", "触发条件": "", "审核结果": "<span style='color:red;'>不适宜</span>",
                   "备注": "123123123", "状态": "<span style='color:#c8c8c8;'>停用</span>"
                             , "最后操作时间": "2020-02-01", "最后操作人": "张三"
                             , "级别": "<span style='color:red;'>强制</span>"
                             , "规则结论": "【开药天数】3天"}]

    return JsonResponse({"code": 0, "msg": "", "count": 66, "data": data_list})
