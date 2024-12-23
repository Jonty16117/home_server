<?php
$CONFIG = array (
  'htaccess.RewriteBase' => '/',
  'memcache.local' => '\\OC\\Memcache\\APCu',
  'apps_paths' => 
  array (
    0 => 
    array (
      'path' => '/var/www/html/apps',
      'url' => '/apps',
      'writable' => false,
    ),
    1 => 
    array (
      'path' => '/var/www/html/custom_apps',
      'url' => '/custom_apps',
      'writable' => true,
    ),
  ),
  'memcache.distributed' => '\\OC\\Memcache\\Redis',
  'memcache.locking' => '\\OC\\Memcache\\Redis',
  'redis' => 
  array (
    'host' => 'nextcloud-redis',
    'password' => 'test',
    'port' => 6379,
  ),
  'upgrade.disable-web' => true,
  'instanceid' => 'asdfadfadf',
  'passwordsalt' => 'asdfasdfasdf',
  'secret' => 'asdfadsfasdf+asdf/asdfadsfasdf',
  'trusted_domains' => 
  array (
    0 => 'nextcloud.kantiwal.xyz',
  ),
  'datadirectory' => '/var/www/html/data',
  'dbtype' => 'mysql',
  'version' => '28.0.3.2',
  'overwrite.cli.url' => 'https://nextcloud.example.com',
  'overwriteprotocol' => 'https',
  'dbname' => 'nextcloud',
  'dbhost' => 'nextcloud-db:3306',
  'dbport' => '',
  'dbtableprefix' => 'oc_',
  'mysql.utf8mb4' => true,
  'dbuser' => 'nextcloud',
  'dbpassword' => 'test',
  'installed' => true,
  'config_is_read_only' => true,
);
