# Generated by Django 4.1.4 on 2022-12-12 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BorTransaction',
            fields=[
                ('bornumber', models.IntegerField(db_column='BorNumber', primary_key=True, serialize=False)),
                ('bordate', models.DateField(blank=True, db_column='BorDate', null=True)),
                ('retdate', models.DateField(blank=True, db_column='RetDate', null=True)),
                ('duedate', models.DateField(blank=True, db_column='DueDate', null=True)),
                ('fineamount', models.TextField(blank=True, db_column='FineAmount', null=True)),
            ],
            options={
                'db_table': 'Bor_Transaction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('bid', models.IntegerField(db_column='Bid', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('location', models.CharField(blank=True, db_column='Location', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Branch',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Copy',
            fields=[
                ('copyno', models.IntegerField(db_column='CopyNo', primary_key=True, serialize=False)),
                ('position', models.CharField(blank=True, db_column='Position', max_length=255, null=True)),
                ('bid', models.IntegerField(blank=True, db_column='Bid', null=True)),
            ],
            options={
                'db_table': 'Copy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('docid', models.IntegerField(db_column='DocID', primary_key=True, serialize=False)),
                ('title', models.TextField(db_column='Title')),
                ('pdate', models.DateField(blank=True, db_column='Pdate', null=True)),
                ('numberofcopies', models.IntegerField(blank=True, db_column='NumberOfCopies', null=True)),
                ('doctype', models.TextField(blank=True, db_column='DocType', null=True)),
            ],
            options={
                'db_table': 'Document',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('pid', models.IntegerField(db_column='Pid', primary_key=True, serialize=False)),
                ('pname', models.CharField(blank=True, db_column='PName', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proceedings',
            fields=[
                ('docid', models.IntegerField(db_column='DocID', primary_key=True, serialize=False)),
                ('cdate', models.DateField(blank=True, db_column='CDate', null=True)),
                ('clocation', models.CharField(blank=True, db_column='CLocation', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Proceedings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('publisherid', models.IntegerField(db_column='PublisherID', primary_key=True, serialize=False)),
                ('pubname', models.CharField(db_column='PubName', max_length=255)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Publisher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('readerid', models.IntegerField(db_column='ReaderID', primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=255, null=True)),
                ('readname', models.CharField(blank=True, db_column='ReadName', max_length=255, null=True)),
                ('phoneno', models.BigIntegerField(blank=True, db_column='PhoneNo', null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
                ('numborbooks', models.IntegerField(blank=True, db_column='NumBorBooks', null=True)),
                ('numresbooks', models.IntegerField(blank=True, db_column='NumResBooks', null=True)),
            ],
            options={
                'db_table': 'Reader',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('resnumber', models.IntegerField(db_column='ResNumber', primary_key=True, serialize=False)),
                ('resdate', models.DateField(blank=True, db_column='ResDate', null=True)),
                ('resstatus', models.BooleanField(blank=True, db_column='ResStatus', null=True)),
            ],
            options={
                'db_table': 'Reservation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('docid', models.OneToOneField(db_column='DocID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='lib_app.document')),
            ],
            options={
                'db_table': 'Authors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(blank=True, db_column='ISBN', max_length=255, null=True)),
                ('docid', models.OneToOneField(db_column='DocID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='lib_app.document')),
            ],
            options={
                'db_table': 'Book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Borrows',
            fields=[
                ('bornumber', models.OneToOneField(db_column='BorNumber', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='lib_app.bortransaction')),
            ],
            options={
                'db_table': 'Borrows',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chairs',
            fields=[
                ('docid', models.OneToOneField(db_column='DocID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='lib_app.document')),
            ],
            options={
                'db_table': 'Chairs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GuestEditors',
            fields=[
                ('docid', models.OneToOneField(db_column='DocID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='lib_app.document')),
            ],
            options={
                'db_table': 'Guest_editors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Has',
            fields=[
                ('docid', models.OneToOneField(db_column='DocID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='lib_app.document')),
            ],
            options={
                'db_table': 'Has',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JournalIssues',
            fields=[
                ('issueno', models.IntegerField(db_column='IssueNo')),
                ('docid', models.OneToOneField(db_column='DocID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='lib_app.document')),
            ],
            options={
                'db_table': 'Journal_issues',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JournalVolume',
            fields=[
                ('volumeno', models.IntegerField(blank=True, db_column='VolumeNo', null=True)),
                ('docid', models.OneToOneField(db_column='DocID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='lib_app.document')),
            ],
            options={
                'db_table': 'Journal_volume',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reserves',
            fields=[
                ('resnumber', models.OneToOneField(db_column='ResNumber', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='lib_app.reservation')),
            ],
            options={
                'db_table': 'Reserves',
                'managed': False,
            },
        ),
    ]
