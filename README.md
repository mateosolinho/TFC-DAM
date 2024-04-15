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
**Wishlist React**
Las tres últimas clases del curso se basaban en hacer una app con React usando componentes, react-dom, arrow functiones, etc, aunque hay cosas en el video que a día de hoy están deprecated, o no funcionan.

***Examen Curso React Principiante***

- **Intento 1 -> 12 aciertos**

- **Intento 2 -> 18 aciertos**

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

## Rutas, navegación y portales

Llamamos Router en react a un componente que muestra u oculta condicionalmente nuestars vistas, administrando la URL y sin realizar una recarga

La librería de react-router es a día de hoy la más usada y gestiona los porblemas habituales del routing de manera liviana

El routing de forma general, y especificamente para esta librería se divide en switchs y rutas

El routing en una aplicación también implica una gestión de la navegación y una forma de recuperar y manipular el historial

La API de HTML5 History nos permite manipular el historial del navegador sin etener que realizar cargas o recargas reales del contenido

React router implementa una versión propia de la API de History del navegador que además es compatible con otros navegadores desactualizados

La navegación programática es posible en React gracias a la inyección de propiedades del router y el uso de hooks

Llamamos Portal a un componente de React que nos permite respetar la jerarquía de componentes mientras nos proporciona libertad para renderizar en cualquier punto del DOM

Los portales son usados en casos como modales, diálogos, tolltips y demás elementos entorpecidos por el z-index o sensibles a la posición en el DOM

Pese a encontrarse en puntos del DOM diferentes, se respetan las consecuencias de la jerarquía de componentes de React, incluyendo en la propagación de eventos

## Abstracción de funcionalidades

Un HOC está basado en el concepto de función de alto nivel de Javascript (HOF) y consiste en un componente que devuelve otro componente

Los HOC se dedican principalmente a solucionar preocupaciones transversales, esto es, características comunes que afectann a varias partes de la aplicación

Para facilitar el desarrollo y trazabilidad es recomendable seguir unas convenciones respecto al uso de HOCs

Las render props son componentes que entran por propiedades de otros componentes y realizan su renderización, recibiendo parámetros del primero

Tanto las HOC con las render props son usadas para solucionar preocupaciones transversales, son complementarias y combinables

Las render props no tienen que ser únicas por componente y el nombre de la propiedad puede ser arbitrario

Los Hooks de React permiten a los componentes funcionales adquirir la funcionalidad ausente anteriormente de los componentes de clase

Las funcionalidades incluyen estado, gestión de efectos secundarios y acceso a los contextos existentes de React

Usando Hooks de efecto también es posible replicar de manera completa el ciclo de vida disponible en los componenytes de clase

## Gestión de estado

Las aplicaciones en React funcionan por diseño pasando las propiedades verticalmente hacia abajo, encascada, y realizando cambios por callbacks

La comunicación horizontal no es necesariamente frecuente pero es un caso complicado para la gestión habitual del estado en React

Existen múltiples soluciones para compartir el estado, algunas de ellas incluso nativas del propio navegador

Existen varios patrones de centralizado del estado, pero generalmente sólo varían en el flujo de acción y se basan en principios similares

El patrón Redux se basa en crear una única fuente de verdad en la aplicación, únicamente de sólo lectura y modificable a través de acciones controladas

El hook useReducer nos permite implementar nativamente en la librrería patrones de gestión del estado como Redux

Favorecer la cascada y mantener el mínimo posible de componentes con estado o stateFull simlifica la gestión del estado en puntos controlables

Mantener los componentes puros, cuando sea posible, no sólo favorece a la cascada sino que nos permite introducir optimizaciones de la librería

Centralizar el estado puede ser positivo incluso aunque no se use un patrón concreto, simplemente tener alguna estrategia simplificaría el desarrollo


***Examen Curso React Intermedio***

- **Intento 1 -> 16 aciertos** 

## Desarrollo con Hooks

Los Hooks de React permiten a las funciones acceder a estado y ciclo de vida, acercando la filosofía más a la inicial del equipo

Las funcionalidades incluyen estado, gestión de efectos secundarios y acceso a los contextos existentes de React

Los hooks aprovechan el concepto de hoisting y closure para crear conextos en donde puedan existir y mantener sus valores entre ejecuciones

## Manejo de estado con Hooks

A diferencia de los componentes de clase, el estado en los componentes funcionales depende de un Hook y no está asociadoa this

El estado en componentes duncionales se puede lograr gracias al uso de Hooks de estado como son useState y useReducer

El hook useState nos permite declarar una variable de estado que permanece con un valor inalterado a menos que lo modifiquemos mediante un setter

El hook useReducer nos permite implementar un estado en un objeto, más parecido al de clases, pero cuya manipulación es similar al patrón Redux

## Ciclo de vida con Hooks

El Hook de efecto permite realizar efectos secundarios sobre nuestro código, especificando una lista de dependencias que lancen de nuevo dicho hook

Por su naturaleza, useEffect sustituye de forma efectiva las funciones de ciclo de vida de los componentes de clase y responde a los cambios, montaje, y desmontaje

Los hooks de efecto son llamados tras cada renderizado de React. Si queremos que sean llamados síncronamente tras las updates debemos de usar useLayoutEffect
