#fix our stack so that we get to 0.
#increase limit
exec {'fix-ngninx':
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  provider => shell,
}

exec {'restart-nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
