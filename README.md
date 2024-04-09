# Curso React Mateo Soliño

## <ins> Semana 09/04 </ins>
## Fundamentos y Origen
### Sistemas de diseño, patrones y componentes: 
El diseño "interno" de React se divide en Layout, Lógica y Estilos. Actualmente la arquitectura del frontend se basa en el encapsulamiento, hay un archivo de estilos, uno de lógica común, y por cada bloque llamado página existe un apartado de layout y otro de lógica propia.

### Encapsulación:
La encapsulación se basa en separar los tres "pilares" en componentes, en esos componentes tendremos partes de los estilos, de lógica y del layout. Por lo que finalmente se separará todo por componentes únicos. Por consecuencia la aplicación (el componente general) estará compuesta de varios componentes, a esto se le llama estructura de árbol.

### Atomic Desing:
Este diseño se basa en que toda interfaz se puede dividir en diferentes combinaciones de elementos, la unidad más básica, los átomos, la combinación de estos dan lugar a moleculas, que a su vez combinada dan lugar a organismos, que si se juntan de nuevo dan lugar a templates que si se juntan de nuevo dana lugar a páginas. Ejemplo de átomos: Labels, buttons, inputs.

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

console.log("getFullName:" , getFullName(user))
```
Otra manera de hacerlo sería la siguiente:
```js
const { name, surname } = user;

console.log(user) 
```

Gracias a la destructuración tambien podemos darle un nuevo valor a una clave de un objeto:
```js
const { name: newName } = newUser;

console.log("newName:" , newName)
```

Destructuración de los parametros de una función:
```js
const sum = {...nums} =>
  nums.reduce((total, num) => total + num, 0);

console.log("sum:", sum(1, 2, 3, 4, 5, 6, 7, 8, 9));
```

### Clases y módulos:
En el caso de las clases y la orientación a objetos gran parte de los contenidos es igual que en Java
Lo único a destacar es que el en cada clase solo puede haber un export default, pero puede haber varios exports nombrados.
Al hacer un export en la clase en la que lo quiera utilizar debo usar un import.

## Anatomía de React
### Reconciliación:
Proceso en el cual React intenta optimizar el renderizado que va a realizar a posterior.
Esto es así gracias al uso del DOM y posteriormente al Virtual DOM

### Renderización:
React se encarga del tratamiento del Virtual DOM, captura de eventos, etc
React DOM/Native/Vr se encarga del renderizado

## Crear una aplicación en React
