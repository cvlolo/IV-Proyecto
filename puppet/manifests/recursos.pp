# Actualizo los repositorios existentes

exec { "apt-get update":
    command => "/usr/bin/apt-get update"
}


# Instalación de git
package { "git":
    ensure => present,
    require => Exec["apt-get update"]
}


# Instalación de build-essential
package { "build-essential":
    ensure => present,
    require => Exec["apt-get update"]
}

