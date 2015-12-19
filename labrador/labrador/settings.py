#!/usr/bin/env python
# encoding: utf-8

"""
Django settings for labrador project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')q1axayom)$w%&fs+k3t)ymd+5d9u5yh^_7mj=r4yek%*(4(6+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'labrador.chuzuwu',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'labrador.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'labrador.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TIME_ZONE = 'Asia/Shanghai'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# 便于开发环境下直接runserver时获取需要的静态文件
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# 便于生产环境的结构下由额外的server提供静态文件
STATIC_ROOT = os.path.join(BASE_DIR, 'statics')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'templates/locale'),
)

# 表格信息
EXCEL_RECORD_COL = [u'房号', u'租客', u'租金', u'电费', u'网费', u'充电', u'电视费',
                    u'小计', u'备注']
# 价格信息
INTERNET_FEE = 40
CHARGE_FEE = 10
TV_FEE = 25

# 接口返回信息
RETURN_MSG = {
    'success': {'code': 20000, 'msg': 'success'},
    'room_empty': {'code': 20001, 'msg': 'room is empty'},
    'room_record_not_found': {'code': 20002, 'msg': 'room record not found'},
    'room_record_finish': {'code': 20003, 'msg': 'room record finish'},
    'room_lived': {'code': 20004, 'msg': 'room is lived'},
}


if DEBUG:
    from labrador.conf.labrador_conf_dev import *
