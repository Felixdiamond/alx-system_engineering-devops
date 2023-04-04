# Set up the package manager
class { '::apt':
  update => {
    frequency => 'daily',
  },
}

# Install Nginx and set up the custom HTTP header
class { '::nginx':
  # Add the custom header
  header => [
    'add_header X-Served-By $hostname;',
  ],
}

