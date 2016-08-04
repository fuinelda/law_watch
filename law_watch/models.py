# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField

class LawSummary(models.Model):
	law_no = models.CharField(primary_key=True, max_length=20)
	law_json = JSONField()  # This field type is a guess.

	class Meta:
		managed = True
		db_table = 'law_summary'

class BillInfoList(models.Model):
	bill_id = models.CharField(primary_key=True, max_length=100)
	bill_json = JSONField()  # This field type is a guess.
	bill_member_json = JSONField()

	class Meta:
		managed = False
		db_table = 'bill_info_list'
