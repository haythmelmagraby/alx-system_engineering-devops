#0. Strace is your friend

exec { 'fix wordpres':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
