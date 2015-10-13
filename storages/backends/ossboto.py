from boto.aliyun.oss.connection import OSSConnection
from boto.s3.connection import SubdomainCallingFormat
from boto.aliyun.oss.key import Key as OSSKey
from storages.backends.s3boto import S3BotoStorage as Storage
from storages.utils import setting


class OSSBotoStorage(Storage):
    connection_class = OSSConnection
    key_class = OSSKey

    # used for looking up the access and secret key from env vars
    access_key_names = ['ALIYUN_OSS_ACCESS_KEY_ID', 'ALIYUN_ACCESS_KEY_ID']
    secret_key_names = ['ALIYUN_OSS_SECRET_ACCESS_KEY', 'ALIYUN_SECRET_ACCESS_KEY']

    access_key = setting('ALIYUN_OSS_ACCESS_KEY_ID', setting('ALIYUN_ACCESS_KEY_ID'))
    secret_key = setting('ALIYUN_OSS_SECRET_ACCESS_KEY', setting('ALIYUN_SECRET_ACCESS_KEY'))
    file_overwrite = setting('ALIYUN_OSS_FILE_OVERWRITE', True)
    headers = setting('ALIYUN_HEADERS', {})
    bucket_name = setting('ALIYUN_STORAGE_BUCKET_NAME')
    auto_create_bucket = setting('ALIYUN_AUTO_CREATE_BUCKET', False)
    default_acl = setting('ALIYUN_DEFAULT_ACL', 'public-read')
    bucket_acl = setting('ALIYUN_BUCKET_ACL', default_acl)
    querystring_auth = setting('ALIYUN_QUERYSTRING_AUTH', True)
    querystring_expire = setting('ALIYUN_QUERYSTRING_EXPIRE', 3600)
    reduced_redundancy = setting('ALIYUN_REDUCED_REDUNDANCY', False)
    location = setting('ALIYUN_LOCATION', '')
    encryption = setting('ALIYUN_OSS_ENCRYPTION', False)
    custom_domain = setting('ALIYUN_OSS_CUSTOM_DOMAIN')
    calling_format = setting('ALIYUN_OSS_CALLING_FORMAT', SubdomainCallingFormat())
    secure_urls = setting('ALIYUN_OSS_SECURE_URLS', True)
    file_name_charset = setting('ALIYUN_OSS_FILE_NAME_CHARSET', 'utf-8')
    gzip = setting('ALIYUN_IS_GZIPPED', False)
    preload_metadata = setting('ALIYUN_PRELOAD_METADATA', False)
    url_protocol = setting('ALIYUN_OSS_URL_PROTOCOL', 'http:')
    host = setting('ALIYUN_OSS_HOST', OSSConnection.DefaultHost)
    use_ssl = setting('ALIYUN_OSS_USE_SSL', True)
    port = setting('ALIYUN_OSS_PORT', None)
    proxy = setting('ALIYUN_OSS_PROXY_HOST', None)
    proxy_port = setting('ALIYUN_OSS_PROXY_PORT', None)
