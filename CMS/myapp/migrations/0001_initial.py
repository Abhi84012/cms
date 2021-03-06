# Generated by Django 3.1.1 on 2020-10-09 05:52

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name_en', models.CharField(choices=[('onlinecasino', 'Online-Casino'), ('sportsbet', 'Sports-Bet'), ('slotmachine', 'Slot-Machine')], max_length=255)),
                ('category_name_de', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('country_name_en', models.CharField(choices=[('austria', 'Austria'), ('germany', 'Germany'), ('switzerland', 'Switzerland')], max_length=255)),
                ('country_name_de', models.CharField(choices=[('osterreich', 'Österreich'), ('deutschland', 'Deutschland'), ('schweiz', 'Schweiz')], max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinanceType',
            fields=[
                ('financetype_id', models.AutoField(primary_key=True, serialize=False)),
                ('financetype_name_en', models.CharField(choices=[('partfinanced', 'Part-Financed'), ('percentagefinanced', 'Percentage-Financed'), ('fullyfinanced', 'Fully-Financed')], max_length=255)),
                ('financetype_name_de', models.CharField(choices=[('teilfinanzierung', 'Teilfinanzierung'), ('prozentfinanzierung', 'Prozentfinanzierung'), ('vollfinanzierung', 'Vollfinanzierung')], max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('telephone1', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('telephone2', phone_field.models.PhoneField(blank=True, help_text='Contact phone number2', max_length=31)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('street', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=255)),
                ('postalcode', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(choices=[(1, 'New'), (2, 'Processing'), (3, 'Waiting'), (4, 'Lawsuit Filed'), (5, 'Won'), (6, 'Inactive'), (7, 'Lost')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_type', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True)),
                ('person_id', models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.person')),
            ],
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('Lawyer_id', models.AutoField(primary_key=True, serialize=False)),
                ('fees_per_hour', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fees_per_service', models.DecimalField(decimal_places=2, max_digits=6)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True)),
                ('person_id', models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.person')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True)),
                ('person_id', models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.person')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('currency_id', models.AutoField(primary_key=True, serialize=False)),
                ('currency_name', models.CharField(max_length=100)),
                ('currency_short', models.CharField(max_length=100)),
                ('currency_symbol', models.CharField(max_length=100)),
                ('country_id', models.ForeignKey(db_column='country_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.country')),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('case_id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True)),
                ('customer_amount_lost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('case_amount_claim', models.DecimalField(decimal_places=2, max_digits=10)),
                ('case_amount_won', models.DecimalField(decimal_places=2, max_digits=10)),
                ('case_amount_lost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lawyer_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('court_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('other_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('earnings_from_claim', models.DecimalField(decimal_places=2, max_digits=10)),
                ('money_earned_netto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer_loss_evidence', models.BooleanField()),
                ('customer_signed_contract', models.BooleanField()),
                ('lawyer_sent_letter_to_vendor', models.BooleanField()),
                ('fee_paid_to_lawyer', models.BooleanField()),
                ('lawyer_assigned', models.BooleanField()),
                ('Lawsuit_has_been_filed', models.BooleanField()),
                ('Lawsuit_won', models.BooleanField()),
                ('category_id', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
                ('country_id', models.ForeignKey(db_column='country_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.country')),
                ('currency_id', models.ForeignKey(db_column='currency_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.currency')),
                ('customer_id', models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
                ('financetype_id', models.ForeignKey(db_column='financetype_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.financetype')),
                ('lawyer_id', models.ForeignKey(db_column='lawyer_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.lawyer')),
                ('state_id', models.ForeignKey(db_column='state_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.state')),
            ],
        ),
    ]
