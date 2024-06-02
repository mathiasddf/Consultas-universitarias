#!"D:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI qw(:standard);
use Text::CSV;

# Ruta al archivo CSV
my $file_path = "D:/xampp/cgi-bin/universidades.csv";

# Crear un objeto CGI
my $cgi = CGI->new;

# Obtener el nombre de la universidad desde el formulario
my $universidad_input = $cgi->param('nombuniversidad') || '';

# Manejo de errores para la apertura del archivo CSV
open my $fh, '<', $file_path or do {
    print $cgi->header('text/html');
    print "<h1>Error al abrir el archivo CSV</h1>";
    print "<p>No se pudo abrir el archivo '$file_path': $!</p>";
    exit;
};

my $csv = Text::CSV->new({ sep_char => '|' });

# Variable para almacenar las opciones del datalist
my $options = "";

# Leer todas las líneas del archivo
my @lines = <$fh>;
close $fh;

# Procesar el encabezado
my $header = shift @lines;
chomp $header;

# Construir las opciones del datalist y encontrar la universidad solicitada
my @resultados;
foreach my $line (@lines) {
    chomp $line;
    if ($csv->parse($line)) {
        my @fields = $csv->fields();
        my $universidad = $fields[1];
        $options .= "<option value=\"$universidad\">\n";

        if ($universidad eq $universidad_input) {
            @resultados = (
                $fields[1],  # Nombre Universidad
                $fields[4],  # Periodo Licenciamiento
                $fields[8],  # Departamento Local
                $fields[18]  # Denominación Programa
            );
        }
    }
}

# Imprimir la cabecera HTTP y el HTML
print $cgi->header('text/html');
print <<HTML;
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Consulta de Universidades Licenciadas</title>
</head>
<body>
  <header>       
    <h1>Consulta de Universidades Licenciadas</h1>
  </header>

  <main>
    <form action="/cgi-bin/universidades.cgi" method="get">
      <div class="form-group">
        <label for="nombuniversidad">Nombre de la Universidad:</label>
        <input id="nombuniversidad" name="nombuniversidad" list="unis" placeholder="Ingresa el nombre">
        <datalist id="unis">
          $options
        </datalist>
      </div>
      <button type="submit">Consultar</button>
    </form>

    <div class="resultado">
      <h2>Resultados</h2>
      <div class="resultdatos">
HTML

if (@resultados) {
    print "<h3>Nombre de la universidad:</h3><p id=\"resultadonombre\">$resultados[0]</p>";
    print "<h3>Periodo de licenciamiento:</h3><p id=\"licenciamiento\">$resultados[1]</p>";
    print "<h3>Departamento local:</h3><p id=\"departamento\">$resultados[2]</p>";
    print "<h3>Denominacion del programa:</h3><p id=\"denomprograma\">$resultados[3]</p>";
} else {
    print "<p>No se encontraron resultados para la universidad '$universidad_input'</p>";
}

print <<HTML;
      </div>
    </div>
  </main>
</body>
</html>
HTML


