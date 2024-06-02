#!"C:/xampp/perl/bin/perl.exe"

use strict;
use warnings;
use CGI qw(:standard);
use Text::CSV;

# Crear objeto CGI y establecer charset
my $cgi = CGI->new;
$cgi->charset('latin-1');

# Obtener parámetro del nombre de la universidad y convertirlo a mayúsculas
my $nombre_universidad = uc($cgi->param('nombre_universidad') || '');

# Imprimir encabezado HTTP
print $cgi->header(-type => 'text/html', -charset => 'latin-1');

# Inicializar variable para almacenar resultados HTML
my $resultados_html = "";

# Si se ha enviado el parámetro, realizar la consulta
if ($nombre_universidad) {
    # Nombre del archivo CSV
    my $csv_file = 'Programas de Universidades.csv';

    # Crear objeto Text::CSV
    my $csv = Text::CSV->new({ binary => 1, auto_diag => 1, sep_char => '|' });

    # Abrir archivo CSV
    open my $fh, '<:encoding(latin-1)', $csv_file or die "No se puede abrir archivo CSV: $csv_file";

    # Leer encabezado del CSV
    my $header = $csv->getline($fh);

    # Leer cada línea del CSV
    while (my $fila = $csv->getline($fh)) {
        my %datos;
        @datos{@$header} = @$fila;

        # Verificar condiciones de búsqueda
        if ($datos{'NOMBRE'} eq $nombre_universidad) {
            $resultados_html .= "<tr>";
            $resultados_html .= "<td>$datos{'NOMBRE'}</td>";
            $resultados_html .= "<td>$datos{'PERIODO_LICENCIAMIENTO'}</td>";
            $resultados_html .= "<td>$datos{'DEPARTAMENTO_LOCAL'}</td>";
            $resultados_html .= "<td>$datos{'DENOMINACION_PROGRAMA'}</td>";
            $resultados_html .= "</tr>";
        }
    }

    # Cerrar archivo CSV
    close $fh;

  