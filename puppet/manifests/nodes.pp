node 'ubuntu-pc' {
  file { '/tmp/hello':
	content => "Hello, world\n",
  }
}
