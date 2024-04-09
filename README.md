# Curso React Mateo Soliño

## <ins> Semana 09/04 </ins>
### Sistemas de diseño, patrones y componentes: 
El diseño "interno" de React se divide en Layout, Lógica y Estilos. Actualmente la arquitectura del frontend se basa en el encapsulamiento, hay un archivo de estilos, uno de lógica común, y por cada bloque llamado página existe un apartado de layout y otro de lógica propia.

### Encapsulación:
La encapsulación se basa en separar los tres "pilares" en componentes, en esos componentes tendremos partes de los estilos, de lógica y del layout. Por lo que finalmente se separará todo por componentes únicos. Por consecuencia la aplicación (el componente general) estará compuesta de varios componentes, a esto se le llama estructura de árbol.

### Atomic Desing:
Este diseño se basa en que toda interfaz se puede dividir en diferentes combinaciones de elementos, la unidad más básica, los átomos, la combinación de estos dan lugar a moleculas, que a su vez combinada dan lugar a organismos, que si se juntan de nuevo dan lugar a templates que si se juntan de nuevo dana lugar a páginas. Ejemplo de átomos: Labels, buttons, inputs.

[imagen](https://github.com/mateosolinho/proyecto-final/assets/124877302/712abe9f-c761-4369-add4-7149c2c70a28)

## JavaScript moderno 
### Identificadores:
+ **var** - Se puede acceder desde fuera del bloque donde esta declarada
+ **let** - No se puede acceder desde fuera del bloque donde esta declarada, es más controlable
+ **const** - Identificador usado para asignar a valores inmutables

### Arrow Functions y Strings literals:
```js
const factorial = a => {
  if ( a <= 1 ) {
    return 1;
  }
  return a * factorial( a - 1 );
};
```

Esta función:
```js
function double(a) {
return a * 2;
}
```
Se puede reducir en esta:
```js
const double = a => a * 2;
```

Para declara Strings de tipo *template* se usan estas comillas **``** :
```js
console.log(`This course is about ${libs[0]}`)
```
En estos strings podemos meter dentro funciones y variables seguidos de un "**$**"

### Destructuración:
Siguiendo la estructura de una arrow function, en el siguiente ejemplo se puede observar como, como parámetro podemos pasarle las claves de un objeto:

```js
const getFullName = ({ name, surname }) => `${name} ${surname}`;
```
