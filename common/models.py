# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    access_token = models.CharField(max_length=200)
    nickname = models.CharField(max_length=45, blank=True, null=True)
    profile_img_url = models.CharField(max_length=100, blank=True, null=True)
    thumbnail_img_url = models.CharField(max_length=100, blank=True, null=True)
    mail = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    created_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Account'


class Booth(models.Model):
    booth_id = models.AutoField(primary_key=True)
    booth_nm = models.CharField(max_length=1000, blank=True, null=True)
    booth_desc = models.CharField(max_length=1000, blank=True, null=True)
    booth_event = models.CharField(max_length=1000, blank=True, null=True)
    booth_img = models.CharField(max_length=1000, blank=True, null=True)
    booth_product = models.CharField(max_length=1000, blank=True, null=True)
    booth_manager = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Booth'


class Boothstamp(models.Model):
    bt_stamp_id = models.AutoField(primary_key=True)
    bt_account = models.ForeignKey('AuthUser', models.DO_NOTHING)
    booth = models.ForeignKey(Booth, models.DO_NOTHING)
    created_dt = models.DateTimeField()
    bt_referer_url = models.CharField(max_length=500 , null=True)
    bt_is_qr = models.BooleanField(null=False)

    class Meta:
        managed = False
        db_table = 'BoothStamp'


class Contestparticipant(models.Model):
    cp_id = models.IntegerField(primary_key=True)
    cont_participant_img_url = models.CharField(max_length=500)
    cont_participant_des = models.CharField(max_length=1000)
    cont_participant_order = models.SmallIntegerField(blank=True, null=True)
    cont_participant_nm = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ContestParticipant'


class Contestvote(models.Model):
    cv_id = models.AutoField(primary_key=True)
    cv_account = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    cp = models.ForeignKey(Contestparticipant, models.DO_NOTHING, blank=True, null=True)
    create_dt = models.DateTimeField(blank=True, null=True)
    is_main = models.BooleanField(null=False)
    # bt_is_qr = models.BooleanField(null=False)

    class Meta:
        managed = False
        db_table = 'ContestVote'


class Foodtruck(models.Model):
    truck_id = models.AutoField(primary_key=True)
    truck_img_url = models.CharField(max_length=1000, blank=True, null=True)
    truck_desc = models.CharField(max_length=1000, blank=True, null=True)
    truck_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FoodTruck'


class FoodtruckMenu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    menu_name = models.CharField(max_length=500, blank=True, null=True)
    menu_price = models.CharField(max_length=45, blank=True, null=True)
    truck = models.ForeignKey(Foodtruck, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FoodTruck_menu'


class Major(models.Model):
    major_id = models.AutoField(primary_key=True)
    major_name = models.CharField(max_length=45, blank=True, null=True)
    major_logo_url = models.CharField(max_length=500, blank=True, null=True)
    major_desc = models.CharField(max_length=1000, blank=True, null=True)
    major_circ_img = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Major'


class Matchschedule(models.Model):
    sch_id = models.AutoField(primary_key=True)
    sch_date = models.DateTimeField(blank=True, null=True)
    sch_major_a = models.ForeignKey(Major, models.DO_NOTHING, related_name='sch_major_a', blank=True, null=True)
    sch_major_b = models.ForeignKey(Major, models.DO_NOTHING, related_name='sch_major_b', blank=True, null=True)
    sch_kind = models.IntegerField(blank=True, null=True)
    sch_title = models.CharField(max_length=500)
    sch_stage = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MatchSchedule'


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)
