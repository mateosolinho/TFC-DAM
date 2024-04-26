# Carreras Proyecto Final Mateo Soliño

*En este Readme.md iré añadiendo curso a curso lo que vaya aprendiendo y lo que me parezca importante de cada clase*

## <ins> Semana 09/04 - 16/04 </ins>

# Carrera React

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
- **Intento 2 -> 18 aciertos** - Aprobado

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

Llamamos Router en react a un componente que muestra u oculta condicionalmente nuestars vistas, administrando la URL y sin realizar una recarga.

La librería de react-router es a día de hoy la más usada y gestiona los porblemas habituales del routing de manera liviana.

El routing de forma general, y especificamente para esta librería se divide en switchs y rutas.

El routing en una aplicación también implica una gestión de la navegación y una forma de recuperar y manipular el historial.

La API de HTML5 History nos permite manipular el historial del navegador sin etener que realizar cargas o recargas reales del contenido.

React router implementa una versión propia de la API de History del navegador que además es compatible con otros navegadores desactualizados.

La navegación programática es posible en React gracias a la inyección de propiedades del router y el uso de hooks.

Llamamos Portal a un componente de React que nos permite respetar la jerarquía de componentes mientras nos proporciona libertad para renderizar en cualquier punto del DOM.

Los portales son usados en casos como modales, diálogos, tolltips y demás elementos entorpecidos por el z-index o sensibles a la posición en el DOM.

Pese a encontrarse en puntos del DOM diferentes, se respetan las consecuencias de la jerarquía de componentes de React, incluyendo en la propagación de eventos.

## Abstracción de funcionalidades

Un HOC está basado en el concepto de función de alto nivel de Javascript (HOF) y consiste en un componente que devuelve otro componente.

Los HOC se dedican principalmente a solucionar preocupaciones transversales, esto es, características comunes que afectann a varias partes de la aplicación.

Para facilitar el desarrollo y trazabilidad es recomendable seguir unas convenciones respecto al uso de HOCs.

Las render props son componentes que entran por propiedades de otros componentes y realizan su renderización, recibiendo parámetros del primero.

Tanto las HOC con las render props son usadas para solucionar preocupaciones transversales, son complementarias y combinables.

Las render props no tienen que ser únicas por componente y el nombre de la propiedad puede ser arbitrario.

Los Hooks de React permiten a los componentes funcionales adquirir la funcionalidad ausente anteriormente de los componentes de clase.

Las funcionalidades incluyen estado, gestión de efectos secundarios y acceso a los contextos existentes de React.

Usando Hooks de efecto también es posible replicar de manera completa el ciclo de vida disponible en los componenytes de clase.

## Gestión de estado

Las aplicaciones en React funcionan por diseño pasando las propiedades verticalmente hacia abajo, encascada, y realizando cambios por callbacks.

La comunicación horizontal no es necesariamente frecuente pero es un caso complicado para la gestión habitual del estado en React.

Existen múltiples soluciones para compartir el estado, algunas de ellas incluso nativas del propio navegador.

Existen varios patrones de centralizado del estado, pero generalmente sólo varían en el flujo de acción y se basan en principios similares.

El patrón Redux se basa en crear una única fuente de verdad en la aplicación, únicamente de sólo lectura y modificable a través de acciones controladas.

El hook useReducer nos permite implementar nativamente en la librrería patrones de gestión del estado como Redux.

Favorecer la cascada y mantener el mínimo posible de componentes con estado o stateFull simlifica la gestión del estado en puntos controlables.

Mantener los componentes puros, cuando sea posible, no sólo favorece a la cascada sino que nos permite introducir optimizaciones de la librería.

Centralizar el estado puede ser positivo incluso aunque no se use un patrón concreto, simplemente tener alguna estrategia simplificaría el desarrollo.


***Examen Curso React Intermedio***

- **Intento 1 -> 16 aciertos** - Aprobado

## Desarrollo con Hooks

Los Hooks de React permiten a las funciones acceder a estado y ciclo de vida, acercando la filosofía más a la inicial del equipo.

Las funcionalidades incluyen estado, gestión de efectos secundarios y acceso a los contextos existentes de React.

Los hooks aprovechan el concepto de hoisting y closure para crear conextos en donde puedan existir y mantener sus valores entre ejecuciones.

## Manejo de estado con Hooks

A diferencia de los componentes de clase, el estado en los componentes funcionales depende de un Hook y no está asociadoa this.

El estado en componentes duncionales se puede lograr gracias al uso de Hooks de estado como son useState y useReducer.

El hook useState nos permite declarar una variable de estado que permanece con un valor inalterado a menos que lo modifiquemos mediante un setter.

El hook useReducer nos permite implementar un estado en un objeto, más parecido al de clases, pero cuya manipulación es similar al patrón Redux.

## Ciclo de vida con Hooks

El Hook de efecto permite realizar efectos secundarios sobre nuestro código, especificando una lista de dependencias que lancen de nuevo dicho hook.

Por su naturaleza, useEffect sustituye de forma efectiva las funciones de ciclo de vida de los componentes de clase y responde a los cambios, montaje, y desmontaje.

Los hooks de efecto son llamados tras cada renderizado de React. Si queremos que sean llamados síncronamente tras las updates debemos de usar useLayoutEffect.

## Fiabilidad y test

La fase de confirmación es muy rápida, pero la de render puede ser muy lenta, por tanto se prevee una mejora con un modo asíncrono. En este modo los métodos de la fase de render pueden ser llamados múltiples veces y de forma automática por React. Por tanto es mandatorio no introducir ningún tipo de efecto secundario en estos métodos del ciclo de vida.

El modo estricto de React es un componente sin renderización que permite debuggear los componentes contenidos.

El uso de la asincronía en React hace que algunos ciclos de vida sean inseguros, al igual que aplicar efectos secundarios en los métodos de la fase de confirmación.

Para detectar efectos secundarios en ciclos de la fase de render, React llama a dichos métodos varias veces para hacer dichos efectos más evidentes.

## Introdución a Jest

Jest es un framework de testing para Javascript y Typescript que es capaz de conectarse con React y puede ser utilizado para testear nuestras apps.

Jest funciona creando archivos .test.js que pueden ser lanzados invocando a un script en nuestro proyecto.

El uso básico de Jest se basa en objetos expectativas y funciones comparadora que nos permiten realizar aserciones en nuestro código.

## Testeando DOM generado por React

Las utilidades para pruebas de React son un conjunto de funciones orientadas a realizar test, sobre todo basados en Jest.

Funcionalidades como act() o Simulate nos permiten reproducir el comportamiento nativo de React fuera de la aplicacion.

## Minimizando el número de renderizados

React renderiza con el ciclo de vida shouldComponentUpdate, que le indica si es necesario renderizar, y luego comprueba los árboles actual y nuevo.

El ciclo shouldComponentUpdate de Component devuelve siempre true, es posible reimplementalo o usar el de PureComponent que compara props y estado.

La renderización y manipulación de listas largas es una tarea pesada para los frameworks Javascript, es posible virtualizarlas para reducir la carga.

## <ins> Semana 16/04 - 23/04 </ins>

### 16/04

## Memorización: Cacheando funciones

La memorización es una técnica que consiste en almacenar en una caché el resultado de una función y devolverlo si los parámetros no cambian.

En React nos interesa para aplicarlo a los componentes funcionales y sus funciones, la forma más sencilla es para componentes puros usando React.memo.

Para aplicar memrización a funciones de un componente funcional podemos usar los hooks useCallback y useMemo, que realizarán memorización sobre las funciones que envuelvan.

## Code-Splitting y tree-shaking

El bundle es el empaquetado que genera Webpack (O Rollup o un bundler similar) y cuyo tamaño puede afectar a la velocidad de carga de la App.

La reducción por code-splitting consiste en la carga diferifa de los componentes usando React.lazy y React.suspense para crear una hasta que esté disponible.

La reducción por tree-shaking es un proceso interno del bundler que consiste en la eliminación del código muerto tanto en nuestro source como en el de las dependencias.

## Renderizado Concurrente

La renderización actual de React hasta la versión 17 es síncrona y por tanto bloqueante, lo cual puede deteriorar la experiencia del usuario.

El modo concurrente es una propuesta experimental cuyo objetivo es lograr que las actualizaciones de React funcionen por separado y los renderizados sean interrumpibles y ordenados por prioridad.

Actualmente el modo experimental va a cambiar con React 18 y la adopción se producirá gradualmente y no directa como se anunció originalmente.

***Examen Curso React Avanzado***

- **Intento 1 -> 17 aciertos**

*Subido código relacionado con el Taller React Hooks*

### 17/04

## Tipos de estado

React controla todo el estado que tiene que ver con la UI o aquel si bien directamente no tiene que ver con el user interface, al final lo utilizamos para renderizar (por ejemplo el estado de una petición http para poder mostrar un spinner).

React nos permite gestionar todo ese estado de UI y se encarga de hacer los cambios pertinentes.

## Props vs State

Si no puede ser recalculado con props y lo voy a usar en el render, deber de ser State.

## Práctica: Tipos de estado

*Subido archivo práctica tipos de estado*

## Diferencias entre Clases y componentes funcionales

Podríamos tener una aplicación donde usemos tanto componentes funcionales como componentes de clase y convivir perfectamente, de hecho hasta que no han llegado los hooks, esto era normal, pero es recomendable pararnos un momento para decidir qué camino tomar en función de nuestras circunstancias y necesidades.

## Composición o herencia

El concepto de Herencia está muy apegado al concepto de Clase. En Javascript no existen las clases porque desde que cualquier función puede devolver un objeto nuevo, no hace falta invocar a un constructor para obtener instancias.

En Javascript favorece la composición frente a la herencia tradicional

### 18/04

## Introducción a Clases

SetState es una petición a React para que actualice un componente determinado. Des esta forma, setState "encolará" los cambios de estado y React actualizará el componente y sus hijos con estos cambios.

## setState con función y validación

Internamente react ejecutará la función que le pasemos a setState y generará un nuevo estado con Object.assign.

## La asincronía de setState

setState es asíncrono. Quiere decir que no se produce una actualización de estado inmediatamente después de invocar a la función

## Funcionamiento de setState con una función

Cuando hacemos una petición de actualización de estado con funciones, React encola las llamadas y después compone las funciones dentro de Object.assign para obtener el nuevo estado.

## Hacer operaciones después de setState

En ocasiones necesitamos hacer operaciones justo después de actualizar el estado. Para ello, React nos proporciona una última forma de llamar a setState. Esto es útil cuando queremos escuchar un cambio en concreto. Para operaciones más complejas, se recomienda usar componentDidUpdate.

*Añadida práctica local-storage-jsx*

### 21/04

## Introducción a Hooks

Los hooks son la nueva forma de a partir de React 16.8 de gestionar estado en los componentes funcionales. Las principales ventajas son las siguientes: 
- Sintaxis más limpia
- Cuaalqueir componente funcional puede ahora gesttionar estado
- Podemos olvidarnos para siempre de las clases
- Nos evitan tener problemas con el contexto
- La funcionalidad es más fácil de abstraer con Custom Hooks

## Refactorizar una clase a componente funcional

Refactorizar una clase a un componente funcional en React implica transformar la manera en que se define un componente, pasando de utilizar una clase de JavaScript a una función. Este cambio simplifica el código y lo hace más legible y fácil de mantener, especialmente para componentes que no necesitan estado o métodos de ciclo de vida complejos.

## Uso de set con una función

La función setState (en componentes de clase) o la función devuelta por useState (en componentes funcionales) toma un nuevo valor de estado como argumento y actualiza el estado del componente. Cuando se actualiza el estado en React, el componente se vuelve a renderizar automáticamente con los nuevos valores de estado.

Es importante notar que en React, los estados deben actualizarse de forma inmutable, es decir, debes crear un nuevo objeto o valor en lugar de modificar directamente el estado existente. Esto garantiza un comportamiento predecible y eficiente del componente.

## Refactorizar estados con función a Hooks

Refactorizar estados con funciones a Hooks en React implica reemplazar el uso de variables de estado gestionadas mediante funciones en componentes de clase, por el uso de Hooks como useState en componentes funcionales. Esto simplifica el código y lo hace más claro y fácil de mantener.

## La asincronía de set

La asincronía de set se refiere al comportamiento en JavaScript donde la ejecución de la función set (como setState en React) puede no ser inmediatamente efectiva. En React, cuando utilizas setState para actualizar el estado de un componente de clase, la actualización no es necesariamente instantánea.

En lugar de aplicar los cambios de estado de inmediato, React puede agrupar múltiples llamadas a setState y realizar las actualizaciones en lotes para mejorar el rendimiento. Esto significa que no puedes confiar en que el estado se actualice de inmediato después de llamar a setState.

## LocalStorage con useEffect

Cuando utilizas useEffect con LocalStorage en React, lo haces para sincronizar el estado de tu componente con el almacenamiento local del navegador.

Usar LocalStorage implica que los datos se almacenan en el navegador del usuario y persisten incluso después de que se cierre la ventana del navegador o se actualice la página.

Cuando utilizas useEffect, puedes leer datos del LocalStorage cuando el componente se monta por primera vez y actualizar el LocalStorage cuando el estado del componente cambia. Esto asegura que el estado del componente esté siempre actualizado y refleje los datos almacenados en el LocalStorage.

En resumen, useEffect te permite manejar la sincronización entre el estado del componente y el LocalStorage, lo que es útil para aplicaciones que necesitan almacenar y recuperar datos de forma persistente en el navegador del usuario.

## Dependencias de useEffect

Las dependencias de useEffect en React son un array opcional que se pasa como segundo argumento a useEffect. Estas dependencias controlan cuándo se ejecuta el efecto.

Cuando proporcionas un array vacío de dependencias ([]), el efecto se ejecuta solo una vez, después de que el componente se monta. Esto es útil para tareas que solo deben realizarse una vez, como la inicialización de datos.

Si proporcionas una lista de dependencias, el efecto se ejecutará cada vez que una de esas dependencias cambie. Por ejemplo, si tienes [count] como dependencia y count cambia, el efecto se ejecutará nuevamente. Si la lista está vacía, el efecto se ejecutará en cada renderizado.

## Custom Hook
Un custom hook en React es una función que te permite encapsular la lógica de tu componente y reutilizarla en otros componentes. Puedes crear tus propios hooks para compartir lógica entre componentes de una manera limpia y modular.

***Examen Curso de Manejo de Estado con Clases y Hooks en React***

- **Intento 1 -> 12 aciertos**
- **Intento 2 -> 16 aciertos** - Aprobado
- 
## <ins> Semana 24/04 - 01/05 </ins>

### 24/04

## Arquitectura Flux

Es la arquitectura que utiliza Facebook para construir sus aplicaciones Frontend.

Es importante resaltar que Redux, es una implementación de Flux.

Por tanto puedes obtener los beneficios de la arquitectura Flux sin usar Redux.

## Introducción a los Reducers

Flux es un patrón para el manejo de datos en tu aplicación.

Lo más inportante de Flux es: Define un flujo unidireccional para la UI.

En programación encontramos la utilidad reduce que nos permite aplicar una función a cada uno de los elementos de una lista con el objetivo de acumular valor.

## Actions

Una acción (o action) es cualquier evento que se produzca en nuestra aplicación t genere un cambio en nuestro estdo.

## Action Creators

Comno su propio nombre indica, un action crea acciones. Si la única forma de crear Acciones es a través de Action creators, nuestra aplicación es consistente.

## Selectors

La forma de nuestro estado (state shape) debe de estar optimizada al como se actualice en lugar de al como se visualice. Un selector es una funciñon que toma un estado y devuelve una visualizaciñon del mismo.

## Testing Reducers

Como los reducers son funciones puras en Javascript, es muy fácil realizar tests unitarios sobre ellos.

## Context

Context nos ofrece una forma de poder compartir una prop entre componentes sin necesidad de tener que ir pasándola en cascada a todos nuestros componentes. 

Context tiene varias aplicaciones, una de ellas es el poder compartir nuestro estado por todos los componentes.

## React.memo y useCallback

React.memo en conjución con useCallback usados en el sitio adecuado puede aportar una mejora en el rendimiento de nuestra aplicación. Nos permite no hacer re-renders innecesarios. Recibe una unas dependencias y una función. Mientras las dependencias no cambien, la referencia a esa función será la misma.

## Introducción a Data fetching en React

Cuando hablamos de traernos datos de una fuente externa como un servidor, estamos hablando de Data Fetching. LocalStorage tambien es un ejemplo de Data Fetching.

Debido a que las funciones que acceden a localStorage o a un servidor externo está fuera de nuestro control, no son consideradas funciones puras.

Para poder lanzar side effects o efectos en React, tenemos que usar siempre "useEffect".

### 25/04

## Data fetching en useEffect

Para lanzar una función con side-effects necesitamos hacerlo dentro de un useEffect, pero esto solo courre cuando la función en cuestión está relacionada de alguna forma con el ciclo de vida del componente.

## Gestionando successes, errors y loadings

En nuestras aplicaciones no solo queremos controlar cuando todo vaya bien, si no cuando el proceso se esté ejecutando o cuando ocurra un error

## Custom hook para Data fetching

Lo que se ha visto hasta ahora es funcional cuando solo tenemos una peticiçon que hacer, sin embargo, en una aplicación real vamos a querer realizar muchas peticiones a diferentes servicios, por lo que es necesario disponer de una abstracción.

## Data fetching con Reducers

Un reducer aparte de separarnos la lógica de estado de nuestros componentes, nos permite aunar en una única función todos los cambios de estado necesarios dada una acción. 

Y es precisamente con Data Fetching donde cobran mucho sentido, ya que por lo general vamos a querer realizar varios camios en el estado depende de la acción.

***Examen Curso de Manejo de Estado y Data Fetching en React***

- **Intento 1 -> 16 aciertos** - Aprobado

*Añadido taller Code splitting en SPA con React*

*Añadido taller React en el servidor*

# Carrera Python Aplicado a Machine Learning

## Introducción a Scikit-learn

Una librería que establece un framework para crear flujos de la creación de algoritmos de ML.
Efectivamente unifica un campo muy diverso y abstrae las dificultades de cada algoritmo distinto.
Nuevas librerias frecuentemente adopta su sintaxis, facilitando su adopción.

Para manejar detos lo más común es utilizar Numpy y Pandas, siempre es útil crear gráficos con por ejemplo Matplotlib, Seaborne o Plotnine, si hacen falta otras implementaciones de algoritmos, altenativas típicas son XGBoost, statsmodels y Keras

### 26/04

## Sintaxis Básica

El entrenamiento de un modelo supervisado siempre sigue el mismo patrón:

```python
my_model = SomeModel(...)
my_model.fit(X_train, Y_train)
my_model.predict(X_test)
```
*Añadido SckLearn-test.py*

Primer Modelo:
- Declaramos el modelo, lo "entrenamos" y luego predecimos
- La sintaxis simple vale para los distintos modelos
- Cada modelo tiene sus propios "hiperparámetros" que se tiene que especificar
- El requisito previo es un "X" y "y" en condiciones

*Añadido first-model.py*

Output:

![imagen](https://github.com/mateosolinho/proyecto-final/assets/124877302/bf50c87b-d443-4bd7-b980-e86a1bd649e7)

## Requisitos mínimos

Antes de entrenar un modelo hay que preparar los datos.
Generalmente la preparación de datos es muy amplio, vamos a centrar en los requisitos básicos por ahora
Siempre necesitamos:
- X: datos de los "features" de n filas y m columnas, todos los datos numéricos
- y: datos del "target" de n filas y 1 columna, todo numérico

Hacen falta un "X" y "y" para entrenar, del mismo número de filas y datos numéricos

Cualquier columna con texto se tiene que transformar a numérico de alguna forma (los nulos a veces tambien)

Es normal que el "X" y "y" vengan de unos datos crudos y que las transformaciones necesarias se hacen ahí

Puntos importantes:
- Scikit-learn convierte los data frames en arrays de Numpy, entonces el orden de las columnas es importante
- La flexibilidad de scikit-learn nos permite crear nuestros propios modelos
- Gracias a scikit-learn, otras librerías adoptan el mismo sintaxis
- El proceso es similidar para clasificación de varias clases

## Pasos previos a entrenar un modelo

Todas las transformaciones que podemos hacer con slklearn se pueden hacer en Pandas

Sklearn es útil cuando queremos que el proceso sea robusto, "optimizables" y manejar nuestro "train" y "test"

Es común hacer la parte exploratoria en Pandas y explotar sklearn para construir el flujo completo de entrenamiento

## Dividir en Train y Test

La división de los datos de train y test es importante por muchos motivos, tambien para la preparación inicial

No queremos que influyan los datos "no vistos" en el diseño de los pasos de preparación

Se puede hacer con Pandas, pero sklearn nos facilita el proceso y garantizamos evitar errores comunes

## Pipelines

El "pipelearn" de sklearn es una herramienta fundamental para mejorar el precode de preapración

El us manera flexible de crear "flujos" de diferentes pasos de preparación que luego podemos optimizar y ejecutar sobre los datos de test

*Añadido pipelines.py*

Output:
```python
array([ 2208.96109587, 14931.09346813, 12903.23640107, 12903.23640107,
       12903.23640107, 12903.23640107, 11874.23288725,  2301.11985276,
        4328.97691981,  2301.11985276])
```

Para realmente aprovechar el pipeline explotamos las funciones especiales de scikit-learn

Normalmente utilizan un sintaxis muy similar a nuestros modelos

El pipeline es una serie de "pasos" con nombres que se ejecutan al ejecutar el pipeline

Podemos tratar nuestro pipeline como si fuera un modelo cualquiera ya que comparte los métodos y sintaxis común

## Funciones espaciales para preparar los datos

*Añadido fnc-preparar-datos.py*

Output:

```python
array([['en', 'Los Angeles'],
       ['en', 'UKNOWN'],
       ['es', 'New York City'],
       ...,
       ['en', 'New York, NY'],
       ['en', 'UKNOWN'],
       ['en', 'New York City']], dtype=object)
```

Sklearn nos facilita varias funciones útiles para los pasos típicos de preparación de los datos.

Utiliza una sintaxis similar a la sintaxis de los modelos, pero ahora incorporando el método "transform"

Estos pasos se pueden ejecutar con Pandas, pero es difícil respetar los datos de train y test

## Creando un pipeline

*Añadido first-pipeline.py*

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/ea628505-b4a5-4f3b-b419-d78093a235b0)

Además de los pasos fundamentales hay algunos que también son muy comunes

Las funciones especiales utilizan una sintaxis común que incorporan el método "transform"

Los pipeline de sklearn nos permiten crear flujos robustos que respetan los datos de train y test

## Introducción a los modelos de Scikit-learn

El modelo es la implementación del algoritmo que aprende a predecir nuestro target basándose en los features

Cada modelo tiene sus propios hiperparámetros y manera de funcionar, pero el "input" y "output" es casi igual

Existen implementaciones distintas para regresión y clasificación

## GLM

Varios distintos modelos que forman la base de los models más "clásicos"

Los más comunes son la regresión lineal y regresión logística

No existen tantos hiperparámetros ya que se ven más afectados por la preparación previa de los datos

Útiles por su interpreatibilidad
