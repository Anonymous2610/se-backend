# Generated by Django 4.1.7 on 2023-03-24 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], max_length=10)),
                ('year', models.IntegerField(default=2023)),
                ('expenditure', models.IntegerField(default=0)),
                ('available_rooms', models.IntegerField(default=0)),
                ('unavailable_rooms', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RoomNo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=10)),
                ('capacity', models.IntegerField(default=2)),
                ('room_status', models.CharField(choices=[('available', 'Available'), ('not available', 'Not Available')], default='not available', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HouseKeeping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('clean', 'Clean'), ('dirty', 'Dirty')], default='dirty', max_length=10)),
                ('inventory', models.CharField(choices=[('available', 'Available'), ('not available', 'Not Available')], default='not available', max_length=20)),
                ('room_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.roomno')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('room_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.roomno')),
            ],
        ),
    ]
