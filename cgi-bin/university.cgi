#!"C:\xampp\perl\bin\perl.exe
use strict;
use warnings;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);

# Ruta al archivo CSV
my $file_path = "C:/xampp/cgi-bin/ProgramasUniversidades.csv";

# Obtener el nombre de la universidad desde el formulario HTML y convertirlo a mayúsculas
my $universidad_input = uc(param('nombuniversidad') || '');

# Validar que se haya proporcionado un nombre de universidad
unless ($universidad_input) {
    print header('text/html');
    print "<html><head><title>Error</title></head><body>";
    print "<h1>Error</h1>";
    print "<p>No se ha proporcionado un nombre de universidad.</p>";
    print "</body></html>";
    exit;
}

# Variable para almacenar los detalles de la universidad encontrada
my %detalles_universidad;

# Manejo de errores para la apertura del archivo CSV
open my $fh, '<', $file_path or do {
    print header('text/html');
    print "<html><head><title>Error</title></head><body>";
    print "<h1>Error</h1>";
    print "<p>No se pudo abrir el archivo CSV: $!</p>";
    print "</body></html>";
    exit;
};

# Leer todas las líneas del archivo
while (my $line = <$fh>) {

    
}


