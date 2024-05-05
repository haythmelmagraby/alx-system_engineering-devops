# kill process
exec { 'pkill killmenow':
  path => '/usr/bin:/bin/:/usr/sbin'
}
