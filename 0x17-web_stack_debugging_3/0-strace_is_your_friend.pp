# Fixes Bad `phpp` Extensions To `php`

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/usr/bin/:/bin/'
}
