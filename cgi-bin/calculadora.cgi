#!"C:\xampp\perl\bin\perl.exe
use strict;
use warnings;
use CGI qw(:standard);

# Imprimir cabecera HTTP
print header(-type => 'text/html', -charset => 'UTF-8'),
	start_html(-title => 'Resultado de la Calculadora', -style => {'src' => "/Lab5_pweb1/style.css"});

# Obtener la operación del formulario
my $operacion = param('operacion');

# Verificar si se envió una operación
if ($operacion) {
    # Definir expresión regular para validar la operación
    my $exp_reg = qr/^((?:\d+(?:\.\d+)?|\((?1)\))(?:\s*[-+*\/]\s*(?:\d+(?:\.\d+)?|\((?1)\)))*)$/;

    # Verificar si la operación cumple con la expresión regular
    if ($operacion =~ $exp_reg) { # =~ se usa para comparar una cadena con una expresion regular
        # Realizar la operación
        my $resultado = eval $operacion;   
        if ($@) {  #variable especial en Perl que contiene el mensaje de error si la ejecución de eval falló
            print "<p class='error'>Error: Operación inválida</p>";
        } else {
             print "<div id='resultado'><p>El resultado de la operación es:</p><p>$resultado</p></div>";
        }
    } else {
        print "<p class='error'>Error: La operación no es válida</p>";
    }
} else {
    print "<p class='error'>Error: No se ha enviado ninguna operación</p>";
}

print end_html;


