from django.db import models

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class OneObjectRule(models.Model):
    oneobjectruleid = models.BigIntegerField(db_column='OneObjectRuleID', primary_key=True)  # Field name made lowercase.
    module = models.CharField(db_column='Module', max_length=255, blank=True, null=True)  # Field name made lowercase.
    objecttype = models.CharField(db_column='ObjectType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    objectlogic = models.IntegerField(db_column='ObjectLogic', blank=True, null=True)  # Field name made lowercase.
    objectvalue = models.CharField(db_column='ObjectValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conditiondesc = models.CharField(db_column='ConditionDesc', max_length=500, blank=True, null=True)  # Field name made lowercase.
    judgedesc = models.CharField(db_column='JudgeDesc', max_length=500, blank=True, null=True)  # Field name made lowercase.
    conclusiondesc = models.CharField(db_column='ConclusionDesc', max_length=500, blank=True, null=True)  # Field name made lowercase.
    conditioncontent = models.TextField(db_column='ConditionContent', blank=True, null=True)  # Field name made lowercase.
    judgecontent = models.CharField(db_column='JudgeContent', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    conclusioncontent = models.CharField(db_column='ConclusionContent', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    rulesourcetypeid = models.CharField(db_column='RuleSourceTypeID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    datasourceid = models.CharField(db_column='DataSourceID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ruletype = models.IntegerField(db_column='RuleType', blank=True, null=True)  # Field name made lowercase.
    rulelevel = models.IntegerField(db_column='RuleLevel', blank=True, null=True)  # Field name made lowercase.
    rulepriority = models.IntegerField(db_column='RulePriority', blank=True, null=True)  # Field name made lowercase.
    ruletips = models.CharField(db_column='RuleTips', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ruledesc = models.CharField(db_column='RuleDESC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isenable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='LastUpdateTime', blank=True, null=True)  # Field name made lowercase.
    lastupdateuser = models.CharField(db_column='LastUpdateUser', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'one_object_rule'