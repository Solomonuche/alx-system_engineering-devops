# increase the hard and soft limits of Holberton user

exec { 'increase-hard-limit':
  command => 'sed -i "/holberton hard/s/5/30000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-soft-limit':
  command => 'sed -i "/holberton soft/s/4/30000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
