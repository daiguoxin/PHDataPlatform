
def get_audit_item_name(item_id):
    item_name = ''
    if item_id == '1-1':
        item_name = '适应证'
    elif item_id == '1-2':
        item_name = '人群禁忌'
    elif item_id == '1-3':
        item_name = '禁忌症'
    elif item_id == '1-4':
        item_name = '过敏禁忌'
    elif item_id == '1-5':
        item_name = '用法用量'
    elif item_id == '1-6':
        item_name = '相互作用'
    elif item_id == '1-7':
        item_name = '重复用药'
    elif item_id == '1-8':
        item_name = '配伍禁忌'
    elif item_id == '1-9':
        item_name = '溶媒适宜性'
    elif item_id == '1-10':
        item_name = '疗程'
    elif item_id == '1-11':
        item_name = '全静脉营养液（TPN）'
    elif item_id == '1-12':
        item_name = '连续用药天数'
    elif item_id == '1-13':
        item_name = '遴选人群'
    elif item_id == '1-14':
        item_name = '限制药品不可掰服'
    elif item_id == '1-15':
        item_name = '首剂负荷用量'
    elif item_id == '1-16':
        item_name = '治疗方案'
    elif item_id == '1-17':
        item_name = '皮试用药'

    elif item_id == '2-1':
        item_name = '门七急三'
    elif item_id == '2-2':
        item_name = '发药量'
    elif item_id == '2-3':
        item_name = '毒麻精放开药量'
    elif item_id == '2-4':
        item_name = '抗菌药物天数'
    elif item_id == '2-5':
        item_name = '药品使用权限'
    elif item_id == '2-6':
        item_name = '医生月度开药量限制'
    elif item_id == '2-7':
        item_name = '医生月度开药金额限制'
    elif item_id == '2-8':
        item_name = '科室月度开药量限制'
    elif item_id == '2-9':
        item_name = '科室月度开药金额限制'
    elif item_id == '2-10':
        item_name = '处方药品数量限制'
    elif item_id == '2-11':
        item_name = '抗菌药物分级管理'
    elif item_id == '2-12':
        item_name = '毒麻精放使用权限'

    elif item_id == '3-1':
        item_name = '累计用量提醒'
    elif item_id == '3-2':
        item_name = '超说明书用药'
    elif item_id == '3-3':
        item_name = '过敏提醒'
    elif item_id == '3-4':
        item_name = '医保限适应症'
    elif item_id == '3-5':
        item_name = '过敏风险提醒'

    return item_name
