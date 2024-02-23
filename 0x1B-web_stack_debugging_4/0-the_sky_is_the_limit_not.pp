# Increases the amount of traffic an Nginx server can handle

exec { 'fix-for-nginx':
  command     => 'sed -i "s/15/4096/" /etc/default/nginx',
  path        => '/usr/local/bin:/bin',
  refreshonly => true,
}

# Restart Nginx when the configuration file is modified
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Exec['fix-for-nginx'],
}

