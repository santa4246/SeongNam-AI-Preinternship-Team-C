from django.db import models as rdbms
from django_prometheus.models import ExportModelOperationsMixin


# from djangotoolbox.fields import SetField


# Create your models here.


class user_col(ExportModelOperationsMixin('user'), rdbms.Model):
    user_Id = rdbms.AutoField(primary_key=True)
    name = rdbms.CharField(max_length=64, default='신규 회원', blank=True)
    major = rdbms.CharField(max_length=128, blank=True)
    degree = rdbms.CharField(max_length=16, blank=True)
    contact_email = rdbms.CharField(max_length=32, blank=True)
    belong = rdbms.CharField(max_length=64, blank=True)
    career = rdbms.CharField(max_length=128, blank=True)
    img_link = rdbms.SlugField(max_length=128, blank=True)


class thesis_plan_col(ExportModelOperationsMixin('plan'), rdbms.Model):
    thesis_plan_Id = rdbms.AutoField(primary_key=True)
    subject = rdbms.CharField(max_length=128)
    schedule = rdbms.IntegerField()
    on_domestic = rdbms.BooleanField()  # true : on domestic
    journal_tier = rdbms.BooleanField()  # true : top tier
    purpose = rdbms.CharField(max_length=32)
    user_Id = rdbms.ForeignKey("user_col", related_name="TP_user_Id", on_delete=rdbms.CASCADE, db_column="user_Id")


class mentor_answer_col(ExportModelOperationsMixin('answer'), rdbms.Model):
    mentor_answer_Id = rdbms.AutoField(primary_key=True)
    mentor_answer = rdbms.TextField()
    mentee_question_Id = rdbms.IntegerField()
    date = rdbms.DateTimeField(auto_now_add=True)
    title = rdbms.TextField()
    user_Id = rdbms.ForeignKey("user_col", related_name="MA_user_Id", on_delete=rdbms.CASCADE, db_column="user_Id")


class mentee_question_col(ExportModelOperationsMixin('question'), rdbms.Model):
    mentee_question_Id = rdbms.AutoField(primary_key=True)
    thesis_plan_Id = rdbms.ForeignKey("thesis_plan_col", related_name="MQ_plan_Id",
    on_delete=rdbms.CASCADE, db_column="thesis_plan_Id")
    date = rdbms.DateTimeField(auto_now_add=True)
    title = rdbms.TextField()
    mentee_question = rdbms.TextField()
    user_Id = rdbms.ForeignKey("user_col", related_name="MQ_user_Id", on_delete=rdbms.CASCADE, db_column="user_Id")
