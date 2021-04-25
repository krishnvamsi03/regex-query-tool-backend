from django.contrib import admin
from .models import userDetails, languageSC, regex, savedRegex, authToken
# Register your models here.


class userDetailsAdmin(admin.ModelAdmin):
    list_display = ('userId', 'username', 'email',
                    'isUserVerified', 'createdOn')


class languageAdmin(admin.ModelAdmin):
    list_display = ('languageId', 'languageName')


class regexAdmin(admin.ModelAdmin):
    list_display = ('regexId', 'regexName', 'regexPattern', 'regexLanguage')


class savedRegexAdmin(admin.ModelAdmin):
    list_display = ('savedRegexId', 'userId', 'regexId')


class authTokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')


admin.site.register(userDetails, userDetailsAdmin)
admin.site.register(languageSC, languageAdmin)
admin.site.register(regex, regexAdmin)
admin.site.register(savedRegex, savedRegexAdmin)
admin.site.register(authToken, authTokenAdmin)
