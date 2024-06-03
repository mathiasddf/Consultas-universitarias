#!"C:\xampp\perl\bin\perl.exe
use strict;
use warnings;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);

# Ruta al archivo CSV
my $file_path = "C:/xampp/cgi-bin/ProgramasUniversidades.csv";

# Obtener el nombre de la universidad desde el formulario HTML y convertirlo a mayúsculas
my $universidad_input = uc(param('nombuniversidad') || '');

