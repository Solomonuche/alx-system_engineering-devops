# Using Puppet, create a manifest that kills a process named killmenow

exec { 'pkill':
  path    => '/bin/',
  command => 'pkill killmenow',
}
