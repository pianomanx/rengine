# Generated by Django 3.2.23 on 2024-05-12 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DNSRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300, unique=True)),
                ('h1_team_handle', models.CharField(blank=True, max_length=100, null=True)),
                ('ip_address_cidr', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('insert_date', models.DateTimeField(null=True)),
                ('start_scan_date', models.DateTimeField(null=True)),
                ('request_headers', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DomainRegistration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('organization', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=500, null=True)),
                ('phone', models.CharField(blank=True, max_length=150, null=True)),
                ('fax', models.CharField(blank=True, max_length=150, null=True)),
                ('id_str', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalIP',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=500)),
                ('owner', models.CharField(max_length=500)),
                ('last_seen', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='NameServer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Registrar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('phone', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=350, null=True)),
                ('url', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RelatedDomain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='WhoisStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('insert_date', models.DateTimeField()),
                ('domains', models.ManyToManyField(related_name='domains', to='targetApp.Domain')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.project')),
            ],
        ),
        migrations.CreateModel(
            name='DomainInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dnssec', models.BooleanField(default=False)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('expires', models.DateTimeField(blank=True, null=True)),
                ('geolocation_iso', models.CharField(blank=True, max_length=10, null=True)),
                ('whois_server', models.CharField(blank=True, max_length=150, null=True)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='targetApp.domainregistration')),
                ('dns_records', models.ManyToManyField(blank=True, to='targetApp.DNSRecord')),
                ('historical_ips', models.ManyToManyField(blank=True, related_name='similar_domains', to='targetApp.HistoricalIP')),
                ('name_servers', models.ManyToManyField(blank=True, to='targetApp.NameServer')),
                ('registrant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrant', to='targetApp.domainregistration')),
                ('registrar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='targetApp.registrar')),
                ('related_domains', models.ManyToManyField(blank=True, related_name='associated_domains', to='targetApp.RelatedDomain')),
                ('related_tlds', models.ManyToManyField(blank=True, related_name='related_tlds', to='targetApp.RelatedDomain')),
                ('similar_domains', models.ManyToManyField(blank=True, related_name='similar_domains', to='targetApp.RelatedDomain')),
                ('status', models.ManyToManyField(blank=True, to='targetApp.WhoisStatus')),
                ('tech', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech', to='targetApp.domainregistration')),
            ],
        ),
        migrations.AddField(
            model_name='domain',
            name='domain_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='targetApp.domaininfo'),
        ),
        migrations.AddField(
            model_name='domain',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.project'),
        ),
    ]
