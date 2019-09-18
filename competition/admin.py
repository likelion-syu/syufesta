from django.contrib import admin
from .models import Account, Booth, Boothstamp, Contestparticipant, Contestvote, Foodtruck, Major, Matchschedule, AccountEmailaddress, AccountEmailconfirmation, AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, DjangoSite, SocialaccountSocialaccount, SocialaccountSocialapp, SocialaccountSocialappSites, SocialaccountSocialtoken


admin.site.register(Booth)
admin.site.register(Foodtruck)