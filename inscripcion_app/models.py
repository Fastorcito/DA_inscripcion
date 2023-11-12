from django.db import models


class Aficion(models.Model):
    id_aficion = models.AutoField(primary_key=True)
    nom_afi = models.CharField(max_length=25)

    def __str__(self):
        return self.nom_afi

    class Meta:
        managed = False
        db_table = 'aficion'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Interes(models.Model):
    id_interes = models.AutoField(primary_key=True)
    nom_int = models.CharField(max_length=25)

    def __str__ (self):
        return self.nom_int
        

    class Meta:
        managed = False
        db_table = 'interes'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    correo = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioAficion(models.Model):
    id_usuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='id_usuario', primary_key=True)  
    id_aficion = models.ForeignKey(Aficion, models.DO_NOTHING, db_column='id_aficion')

    class Meta:
        managed = False
        db_table = 'usuario_aficion'
        unique_together = (('id_usuario', 'id_aficion'),)


class UsuarioInteres(models.Model):
    id_usuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='id_usuario', primary_key=True) 
    id_interes = models.ForeignKey(Interes, models.DO_NOTHING, db_column='id_interes')

    class Meta:
        managed = False
        db_table = 'usuario_interes'
        unique_together = (('id_usuario', 'id_interes'),)
