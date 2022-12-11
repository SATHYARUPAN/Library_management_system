# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authors(models.Model):
    docid = models.OneToOneField('Document', models.DO_NOTHING, db_column='DocID', primary_key=True)  # Field name made lowercase.
    pid = models.ForeignKey('Person', models.DO_NOTHING, db_column='Pid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Authors'
        unique_together = (('docid', 'pid'),)


class Book(models.Model):
    isbn = models.CharField(db_column='ISBN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docid = models.OneToOneField('Document', models.DO_NOTHING, db_column='DocID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Book'


class BorTransaction(models.Model):
    bornumber = models.IntegerField(db_column='BorNumber', primary_key=True)  # Field name made lowercase.
    bordate = models.DateField(db_column='BorDate', blank=True, null=True)  # Field name made lowercase.
    retdate = models.DateField(db_column='RetDate', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    fineamount = models.TextField(db_column='FineAmount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readerid = models.ForeignKey('Reader', models.DO_NOTHING, db_column='ReaderID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bor_Transaction'


class Borrows(models.Model):
    bornumber = models.OneToOneField(BorTransaction, models.DO_NOTHING, db_column='BorNumber', primary_key=True)  # Field name made lowercase.
    copyno = models.ForeignKey('Copy', models.DO_NOTHING, db_column='CopyNo')  # Field name made lowercase.
    resnumber = models.ForeignKey('Reservation', models.DO_NOTHING, db_column='ResNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Borrows'
        unique_together = (('bornumber', 'copyno', 'resnumber'),)


class Branch(models.Model):
    bid = models.IntegerField(db_column='Bid', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Branch'


class Chairs(models.Model):
    docid = models.OneToOneField('Document', models.DO_NOTHING, db_column='DocID', primary_key=True)  # Field name made lowercase.
    pid = models.ForeignKey('Person', models.DO_NOTHING, db_column='Pid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Chairs'
        unique_together = (('docid', 'pid'),)


class Copy(models.Model):
    copyno = models.IntegerField(db_column='CopyNo', primary_key=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bid = models.IntegerField(db_column='Bid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Copy'


class Document(models.Model):
    docid = models.IntegerField(db_column='DocID', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title')  # Field name made lowercase. This field type is a guess.
    pdate = models.DateField(db_column='Pdate', blank=True, null=True)  # Field name made lowercase.
    numberofcopies = models.IntegerField(db_column='NumberOfCopies', blank=True, null=True)  # Field name made lowercase.
    publisherid = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='PublisherID', blank=True, null=True)  # Field name made lowercase.
    bid = models.ForeignKey(Branch, models.DO_NOTHING, db_column='Bid', blank=True, null=True)  # Field name made lowercase.
    doctype = models.TextField(db_column='DocType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Document'


class GuestEditors(models.Model):
    docid = models.OneToOneField(Document, models.DO_NOTHING, db_column='DocID', primary_key=True)  # Field name made lowercase.
    pid = models.ForeignKey('Person', models.DO_NOTHING, db_column='Pid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Guest_editors'
        unique_together = (('docid', 'pid'),)


class Has(models.Model):
    docid = models.OneToOneField(Document, models.DO_NOTHING, db_column='DocID', primary_key=True)  # Field name made lowercase.
    copyno = models.ForeignKey(Copy, models.DO_NOTHING, db_column='CopyNo')  # Field name made lowercase.
    resnumber = models.ForeignKey('Reservation', models.DO_NOTHING, db_column='ResNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Has'
        unique_together = (('docid', 'copyno', 'resnumber'),)


class JournalIssues(models.Model):
    issueno = models.IntegerField(db_column='IssueNo')  # Field name made lowercase.
    docid = models.OneToOneField(Document, models.DO_NOTHING, db_column='DocID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Journal_issues'


class JournalVolume(models.Model):
    volumeno = models.IntegerField(db_column='VolumeNo', blank=True, null=True)  # Field name made lowercase.
    docid = models.OneToOneField(Document, models.DO_NOTHING, db_column='DocID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Journal_volume'


class Person(models.Model):
    pid = models.IntegerField(db_column='Pid', primary_key=True)  # Field name made lowercase.
    pname = models.CharField(db_column='PName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person'


class Proceedings(models.Model):
    docid = models.IntegerField(db_column='DocID', primary_key=True)  # Field name made lowercase.
    cdate = models.DateField(db_column='CDate', blank=True, null=True)  # Field name made lowercase.
    clocation = models.CharField(db_column='CLocation', max_length=-1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Proceedings'


class Publisher(models.Model):
    publisherid = models.IntegerField(db_column='PublisherID', primary_key=True)  # Field name made lowercase.
    pubname = models.CharField(db_column='PubName', max_length=255)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Publisher'


class Reader(models.Model):
    readerid = models.IntegerField(db_column='ReaderID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readname = models.CharField(db_column='ReadName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phoneno = models.BigIntegerField(db_column='PhoneNo', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numborbooks = models.IntegerField(db_column='NumBorBooks', blank=True, null=True)  # Field name made lowercase.
    numresbooks = models.IntegerField(db_column='NumResBooks', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reader'


class Reservation(models.Model):
    resnumber = models.IntegerField(db_column='ResNumber', primary_key=True)  # Field name made lowercase.
    resdate = models.DateField(db_column='ResDate', blank=True, null=True)  # Field name made lowercase.
    readerid = models.ForeignKey(Reader, models.DO_NOTHING, db_column='ReaderID', blank=True, null=True)  # Field name made lowercase.
    resstatus = models.BooleanField(db_column='ResStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reservation'


class Reserves(models.Model):
    resnumber = models.OneToOneField(Reservation, models.DO_NOTHING, db_column='ResNumber', primary_key=True)  # Field name made lowercase.
    copyno = models.ForeignKey(Copy, models.DO_NOTHING, db_column='CopyNo')  # Field name made lowercase.
    readerid = models.ForeignKey(Reader, models.DO_NOTHING, db_column='ReaderID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reserves'
        unique_together = (('resnumber', 'copyno', 'readerid'),)
