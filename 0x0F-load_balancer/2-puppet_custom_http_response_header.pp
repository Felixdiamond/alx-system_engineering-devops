class { 'nginx':
  # Install Nginx
  ensure => present,
}

file { '/etc/nginx/conf.d/custom_http_headers.conf':
  # Create a new file to hold custom HTTP headers
  ensure  => file,
  content => "add_header X-Served-By $hostname;\n",
  notify  => Service['nginx'],
}

service { 'nginx':
  # Restart Nginx to apply changes
  ensure => running,
  enable => true,
}

