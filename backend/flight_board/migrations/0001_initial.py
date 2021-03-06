# Generated by Django 3.0.4 on 2020-06-21 14:23

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия')),
                ('education', models.CharField(blank=True, max_length=150, null=True, verbose_name='Образование')),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Возраст')),
                ('passport_number', models.IntegerField(blank=True, null=True, verbose_name='Пасспортные данные')),
                ('position', models.CharField(blank=True, choices=[('Главный пилот', 'Главный пилот'), ('Второй пилот', 'Второй пилот'), ('Стюардесса', 'Стюардесса'), ('Стюард', 'Стюард')], max_length=50, null=True, verbose_name='Должность')),
                ('status', models.CharField(blank=True, choices=[('Явлеется сотрудником', 'Является сотрудником'), ('На рассмотрении', 'На рассмотрении'), ('Уволен', 'Уволен'), ('Пользователь сайта', 'Пользователь сайта')], default='Пользователь сайта', max_length=50, null=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AirlineCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('logo', models.ImageField(upload_to='airline_componies/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Авиакомпания',
                'verbose_name_plural': 'Авиакомпании',
            },
        ),
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airplane_number', models.IntegerField(unique=True, verbose_name='Номер самолета')),
                ('type', models.CharField(max_length=60, verbose_name='Тип')),
                ('number_of_places', models.SmallIntegerField(verbose_name='Число мест')),
                ('flight_speed', models.SmallIntegerField(verbose_name='Скорость полета (км/ч)')),
                ('airline_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_board.AirlineCompany', verbose_name='Компания авиаперевозчик')),
            ],
            options={
                'verbose_name': 'Самолет',
                'verbose_name_plural': 'Самолеты',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.IntegerField(unique=True, verbose_name='Номер рейса')),
                ('distance', models.SmallIntegerField(verbose_name='Расстояние до пункта назначения (км)')),
                ('departure_point', models.CharField(max_length=100, verbose_name='Пункт вылета')),
                ('destination', models.CharField(max_length=100, verbose_name='Пункт назначения')),
                ('departure_time', models.DateTimeField(verbose_name='Дата и время вылета')),
                ('destination_time', models.DateTimeField(verbose_name='Дата и время прилета')),
                ('transit_landings', models.BooleanField(default=False, verbose_name='Транзитные посадки')),
                ('transit_departure_time', models.DateTimeField(blank=True, null=True, verbose_name='Время транзитных посадок')),
                ('transit_destination_time', models.DateTimeField(blank=True, null=True, verbose_name='Время транзитных вылетов')),
                ('number_of_seats', models.PositiveSmallIntegerField(default=0, verbose_name='Количество мест')),
                ('number_of_tickets_sold', models.PositiveSmallIntegerField(default=0, verbose_name='Количество проданых билетов')),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_board.Airplane', verbose_name='Самолет')),
            ],
            options={
                'verbose_name': 'Рейс',
                'verbose_name_plural': 'Рейсы',
                'ordering': ['departure_time'],
            },
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_board.AirlineCompany', verbose_name='Авиакомпания')),
                ('head_pilot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='head_pilot', to=settings.AUTH_USER_MODEL, verbose_name='Главный пилот')),
                ('second_pilot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_pilot', to=settings.AUTH_USER_MODEL, verbose_name='Второй пилот')),
                ('served_flight', models.ManyToManyField(related_name='served_flight', to='flight_board.Flight', verbose_name='Обслуживаемый рейс(-ы)')),
                ('steward', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='steward', to=settings.AUTH_USER_MODEL, verbose_name='Стюард')),
                ('stewardess1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stewardess1', to=settings.AUTH_USER_MODEL, verbose_name='Стюардесса 1')),
                ('stewardess2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stewardess2', to=settings.AUTH_USER_MODEL, verbose_name='Стюардесса 2')),
            ],
            options={
                'verbose_name': 'Экипаж',
                'verbose_name_plural': 'Экипажи',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='flight',
            field=models.ManyToManyField(related_name='flight', to='flight_board.Flight', verbose_name='Рейс(-ы)'),
        ),
        migrations.AddField(
            model_name='employee',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
