# Curso React Mateo Soliño

## <ins> Semana 09/04 </ins>

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
Instalar node.js:
```bash
https://nodejs.org
```

Instalar nvm (Puede ser tanto para Windows como para Linux)

Inicializar proyecto
```bash
npm init
```

Instalar React en el proyecto:
```bash
npm install --save react
```

Instalar empaquetador:
```bash
npm install --save-dev parcel-bundler
```

Podemos definir scripts en el package.json:
```js
"scripts" : {
  "start" : "parcel index.html"
},
```

Lanzar el script:
```bash
npm start
```

Instalar React DOM:
```bash
npm install --save react-dom
```

Creamos un fichero index.jsx y le añadimos lo siguiente:
```js
import React from "react";
import ReactDOM from "react-dom";

ReactDOM.render(<div> Mi wishlist </div>, document.getElementById("root"));
```

=======================
Podemos agrupar las carpetas en tres tipos:
- Carpetas por tipos
- Carpetas por Features
- Carpetas bien definidas y por tipos
=======================

Instalar ESLint globally
```bash
npm install -g eslint
```

Inicializar ESLint
```bash
eslint --init
```

Instalar Prettier:
```bash
npm install --dev prettier
```
***Examen***
**Intento 1 -> 12 aciertos**
**Intento 2 -> 18 aciertos**

## Comunicación con el servidor
Una web clásica se basa en un servidor estático que puede estar en cualquier sitio, cuando al servidor le llega una petición la procesa y le devuelve al navegador una respuesta en HTML, el navegador es el que se encarga de la renderización; esto es un problema ya que toda la carga del renderizado se la lleva el servidor

AJAX es un conjunto de tecnologías que permite actualizar el contenido de una página sin necesidad de recargarla. El propio motor de AJAX es quien comunica con el servidor y delega la respuesta a JavaScript.

En cuanro a peticiones, un POST es permite introducir crácteres ilimitados, mientras que si lo hacemos con GET serían limitados a 200 que equivale a las "/" de las URL

Los dos tipos principales de peticiones o request más usadas son las tipo POST
y las tipo GET, ambas tienen limitaciones distintas.
Las peticiones GET tienen dirección, cabeceras, y parámetros mientras que
las POST aparte de esto también tienen body (o cuerpo).
Las peticiones con Fetch están compuestas por un objeto init con unas
cabeceras Headers y devuelven una respuesta en formato Response.
El éxito de una petición dependerá tanto de elegir correctamente las
cabeceras como del envío del body así como del procesamiento de la
respuesta.

Un servicio en front-end son un punto intermedio entre nuestro servicio backend y nuestra aplicación o compoenete, este coge la información que emite el backend y la transforma en una información útil para nuestra aplicación.

Un modelo de front es una representación abstracta de la entidad de backend con una orientación a la renderización del contenido.

Un servicio front-end consume información de un backend y simplifica el proceso de consumo del servidor.

Los modelos de front-end no tienen porqué coincidir con los de back-end, y pueden disponer de métodos que nos faciliten su uso.

Un interceptor es uan función que procesa la respuesta o el envio de una petición y añade funcionalidad global para cualquiera que se realice.
