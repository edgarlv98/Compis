# PATITO ++

_Patito ++ es un lenguaje de programación capaz de soportar operaciones lineales, no lineales, funciones, el uso de matrices y arreglos. Además cuenta con funciones pre-establecidas para operaciones en matrices (inversa, determinante, transpuesta)._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

### Pre-requisitos 📋

_El proyecto se ejecuta con python._
_Es necesario tener instalado ply.lex, ply.yacc y numpy. (Es necesario contar con pip instalado, para instalar los modulos)_

```
pip install <modulo>
```

### Comienza 🔧

_Una vez que se tengan los pre-requisitos instalados debes proceder a clonar el proyecto._

_El primer paso para correr el proyecto es crear un script en Patito++ (sintaxis se muestra mas abajo)._
_Busca en el archivo lexAndSyn.py la línea que contiene el nombre del archivo que desees ejectuar._
```
archivo = "<nombreDeTuArchivo>.txt"
```

## Ejecutando las pruebas ⚙️

_Una vez que hayas asignado el nombre de tu archivo a la variable 'archivo' estás listo para ejecutar una prueba._
_Para ejectuar las pruebas es necesario realizar el siguiente comando en tu terminal:_
```
python lexAndSyn.py
```
_Nota: Es recomendable utilizar una version de Python superior a la 3.0_

### Syntaxis 🔩

_Declaración de variables:_
```
var <tipo> <idArray>[<size>], <id>, <idMatriz>[<size>][<size>];
<OtroTipo> <id>, <id>;
```

_Declaración de funciones:_
```
function <tipo> <id> (<parametros){
<bloqueCódigo>
}
```

_Algunas declaraciones de asignaciones:_
```
<id> = <id>;
<id> = <cte>;
<id> = <array>[<index>];
<id> = <matrix>[<index>][<index>];
<id> = <id/cte> <operador + - * /> <id/cte> 
```

_Declaración de Ciclos:_
```
while ( <cond> ) {
  <bloqueCódigo>
}
```
_Nota: La variable que se utilice en la condición no se actualiza automáticamente. No olvides actualizarla!_

_Declaración Escritura:_
```
print(<id>);
print(<cte>);
print(<id> <op> <cte>);
print(<array>[<cte/id>]);
print(<matrix>[<cte/id>][<cte/id>]);
```

_Declaración Lectura:_
```
input[<id>]
```

## Resumen 🛠️

El proyecto fue elaborado para la clase 'Desarrollo de Compiladores' en el ITESM Campus Monterrey.
Febrero - Junio 2020

## Autores 📖

Francisco J. Castro Zuñiga
Edgar López Villarreal

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* No dudes en contactarnos si quieres continuar con el desarrollo del proyecto🤓.
* No critiques, disfruta!

