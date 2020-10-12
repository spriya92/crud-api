from django.contrib.auth.models import AbstractBaseUser
import uuid
from django.db import models


# Create your models here.
class PMUser(AbstractBaseUser):
    """
    User model using Abstract Base user from django which provide basic
    entities by default.
    """

    def get_short_name(self):
        pass

    def get_full_name(self):
        pass

    # Constant for language choices
    EN_LANGUAGE_CHOICE = "en"
    FR_LANGUAGE_CHOICE = "fr"
    GR_LANGUAGE_CHOICE = "gr"
    ENGLISH_LANGUAGE_CHOICE = 'English'
    FRENCH_LANGUAGE_CHOICE = 'French'
    GERMAN_LANGUAGE_CHOICE = 'German'
    # ENUM for language choices
    LANGUAGE_CHOICES = (
        (EN_LANGUAGE_CHOICE, ENGLISH_LANGUAGE_CHOICE),
        (FR_LANGUAGE_CHOICE, FRENCH_LANGUAGE_CHOICE),
        (GR_LANGUAGE_CHOICE, GERMAN_LANGUAGE_CHOICE)
    )
    PROFILE_THEME_LIGHT_ID = 1
    PROFILE_THEME_LIGHT_VALUE = 'Light'
    PROFILE_THEME_DARK_ID = 2
    PROFILE_THEME_DARK_VALUE = 'Dark'

    # ENUM for Profile theme choices
    USER_PROFILE_THEME_ENUM = (
        (PROFILE_THEME_LIGHT_ID, PROFILE_THEME_LIGHT_VALUE),
        (PROFILE_THEME_DARK_ID, PROFILE_THEME_DARK_VALUE)
    )
    # Constant for Timezone
    DEFAULT_TIMEZONE = 'UTC'

    # Constant fo max length for fields
    USERNAME_MAX_LENGTH = 30
    EMAIL_MAX_LENGTH = 255
    FIRST_NAME_MAX_LENGTH = 10
    MIDDLE_NAME_MAX_LENGTH = 10
    LAST_NAME_MAX_LENGTH = 10
    EMP_ID_MAX_LENGTH = 50
    LOCATION_MAX_LENGTH = 30
    DESIGNATION_MAX_LENGTH = 50
    TIME_ZON_MAX_LENGTH = 100
    LANGUAGE_MAX_LENGTH = 100
    PROFILE_PICTURE_MAX_LENGTH = 200
    PROFILE_PICTURE_EXTENSION_MAX_LENGTH = 200
    REFERENCE_ID_MAX_LENGTH = 100
    REFERENCE_TYPE_MAX_LENGTH = 100
    MAX_LENGTH_DEACTIVATION_COMMENT = 500

    # Max size of file is 10 mb
    max_size_in_bytes = 10485760
    max_size_in_mb = 10
    ALLOWED_FILE_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
    FILE_ATTACHMENT_MAX_COUNT = 1

    # Password max-min length constant
    PASSWORD_MIN_LENGTH = 8
    PASSWORD_MAX_LENGTH = 16

    # Constant for field name
    ID = 'id'
    USERNAME = 'username'
    EMAIL = 'email'
    FIRST_NAME = 'first_name'
    MIDDLE_NAME = 'middle_name'
    LAST_NAME = 'last_name'
    EMP_ID = 'empid'
    LOCATION = 'location'
    REPORT_TO = 'report_to'
    DESIGNATION = 'designation'
    TIMEZONE = 'timezone'
    LANGUAGE = 'language'
    CREATED_AT = 'created_at'
    UPDATED_AT = 'updated_at'
    CREATED_BY = 'created_by'
    MODIFIED_BY = 'modified_by'
    PROFILE_PICTURE = 'profile_picture'
    PROFILE_PICTURE_EXTENSION = 'profile_picture_extension'
    PROFILE_PICTURE_DATETIME = 'profile_picture_datetime'
    PERMANENT = 'permanent'
    STATUS_FLAG = 'status_flag'
    REFERENCE_ID = 'reference_id'
    REFERENCE_TYPE = 'reference_type'
    IS_ACTIVE = 'is_active'
    IS_ADMIN = 'is_admin'
    IS_INTERNAL = 'is_internal'
    DEACTIVATE_USER_COMMENT = 'deactivate_user_comment'
    COMPANY = 'company'
    COMPANY_ID = 'company_id'
    COMPANY_NAME = 'company__name'
    DEPARTMENT_ID = 'department_id'

    # Define attributes
    # Username for user
    username = models.CharField(
        verbose_name='username',
        max_length=USERNAME_MAX_LENGTH,
        blank=True, null=True, default=None, unique=True
    )

    # Email id of user
    email = models.EmailField(
        verbose_name='email address',
        max_length=EMAIL_MAX_LENGTH,
        unique=True
    )

    # First name of user
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH, blank=True)

    # Middle name of user
    middle_name = models.CharField(max_length=MIDDLE_NAME_MAX_LENGTH, blank=True)

    # Last name of user
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH, blank=True)

    # Unique id generation for record
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)

    # Datetime when record has been created
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    # Datetime when record has been updated last time
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    # Id of user who has created record
    # TODO: null=true can be removed eventually
    created_by = models.IntegerField(default=0, null=True)

    # Id of user who has modified record last time
    # TODO: null=true can be removed eventually
    modified_by = models.IntegerField(default=0, null=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def __unicode__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    @property
    def is_staff(self):
        """
        "Is the user a member of staff?"
        Simplest possible answer: All admins are staff
        :return:
        """
        return self.is_admin

    class Meta:
        verbose_name = "PMUser"
        verbose_name_plural = "PMUsers"