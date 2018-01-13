# Actualizo los repositorios existentes

exec { "apt-get update":
    command => "/usr/bin/apt-get update"
}

# Instalación de libpq
package { "libpq-dev":
    ensure => present,
    require => Exec["apt-get update"]
}

# Instalación de git
package { "git":
    ensure => present,
    require => Exec["apt-get update"]
}

# Instalación de pip
package { "python-pip":
    ensure => present,
    require => Exec["apt-get update"]
}

#Clonamos repositorio
vcsrepo { "/home/ubuntu/":
  ensure => latest,
  provider => git,
  require => [ Package[ 'git' ] ],
  source => "https://github.com/cvlolo/IV-Proyecto.git",
  revision => 'master',
}

#Instalamos requirements
exec { "requirements":
    require    => File["home/ubuntu/IV-Proyecto/requirements.txt"],
    command => "/usr/bin/pip install -r  home/ubuntu/IV-Proyecto/requirements.txt
}
