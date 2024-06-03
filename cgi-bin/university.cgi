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

    # Coincidir la línea con la expresión regular y capturar todos los campos
    if ($line =~ /^(.*?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)$/) {
        my @campos = ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, $25);

        # Si el nombre de la universidad coincide con el nombre ingresado en el formulario
        if ($campos[1] eq $universidad_input) {
            # Almacenar los campos en el hash
            %detalles_universidad = (
                'Nombre Universidad' => $campos[1],
                'Periodo Licenciamiento' => $campos[6],
                'Departamento Local' => $campos[12],
                'Denominación Programa' => $campos[18]
            );
            last; # Salir del bucle una vez que se encuentren los detalles
        }
    }
}

# Cerrar el archivo CSV
close $fh;

# Imprimir los detalles de la universidad encontrada
print header('text/html');
print "<html><head><title>Resultados de la Consulta</title></head><body>";
print "<h1>Resultados de la Consulta</h1>";
if (%detalles_universidad) {
    print "<p><strong>Nombre Universidad:</strong> $detalles_universidad{'Nombre Universidad'}</p>";
    print "<p><strong>Periodo Licenciamiento:</strong> $detalles_universidad{'Periodo Licenciamiento'}</p>";
    print "<p><strong>Departamento Local:</strong> $detalles_universidad{'Departamento Local'}</p>";
    print "<p><strong>Denominación Programa:</strong> $detalles_universidad{'Denominación Programa'}</p>";
    
} else {
    print "<p>No se encontraron detalles para la universidad: $universidad_input</p>";
}
print "</body></html>";
