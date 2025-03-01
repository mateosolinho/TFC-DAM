# Carreras Proyecto Final Mateo Soliño

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

La regresión logística nos permite predecir una "probabailidad" real con el método "predict-proba"

## 29/04

## Near Neighbours

Otro modelo simple basado en buscar los vecinos de los puntos

Existe una implementacion tanto para clasificacion y regresion

El hiperparametro mas importante corresponde al numero de "vecinos" a tener en cuenta

## SVM

Otros modelos muy clasicos que buscan separar los datos, con implementacion para clasificacion y regresion

Ahora existen muchos mas hiperparametros interesantes, pero las mas importantes son el kernel y la regularizacion

Para SVM es muy importante estandarizar los datos antes de entrenar

## Modelos basados en arboles

Los modelos basados en arboles son entre los mas poderosos y son muy populares por su flexibilidad ante muchos problemas

La base de todo es el "CART" pero nuevos algoritmos aprovechan el "ensembling" para mejorar los resultados

Hay que tener mucho cuidado con el overfitting y existen algunos hiperparametros claves para esto

*Añadido tree-model.py*

Output:

![imagen](https://github.com/mateosolinho/proyecto-final/assets/124877302/3f499fd8-71b5-4d03-b9d4-51e5ab200953)

Modelos muy poderosos tanto para regresion y clasificacion

Se consigue mucho poder aprovechando el "ensembling" pero siempre hay que limitar la profundidad y las divisiones para limitar el overfitting

Estos modelos son extremadamente flexibles ante cualquier problema

## Redes neuronales

Modelos famosos por sus avances importantes en los ultimos años

La implementacion en scikit-learn es limitado a una red simple y no utiliza GPU

Es el modelo que mas flexibilidad tiene a la hora de optimizar y variar a traves de los hiperparametros

## Introduccion a la evaluacion de resultados

Por un lado tenemos implementaciones de metricas comunes

Tambien disponemos de metodologias graficas

Generalmente lo unico que necesitamos son las predicciones del target y el "target" real

*Añadido evaluacion.py*

Ouput:

```python
For predictions_log_reg we scored 46%
For predictions_neigh_clas we scored 77%
For predictions_neigh_clas_10 we scored 77%
For predictions_svm_clas we scored 69%
For predictions_svm_kernel_clas we scored 67%
For predictions_tree_clas we scored 85%
For predictions_rf_clas we scored 86%
For predictions_nn_clas we scored 69%
For predictions_nn_clas_arq we scored 69%
```

## Las diferentes metricas

La metrica correcta siempre depende del contexto

Algunas usan la probabilidad, no el valor concreto predicho

## Metodos visuales para la evaluacion

Existen tecnicas de evaluacion que usan graficos, los mas famosos siendo la curva ROC y precision/recall

Sklearn nos facilita la creacion de estas curvas

En algunos casos tambien nos proporciona los datos para que podamos crear nuestro propio grafico con facilidad

- Matriz de confusion:

![imagen](https://github.com/mateosolinho/proyecto-final/assets/124877302/9f58b54c-8408-4eb2-83a6-e0f95b84b3db)

- Curva ROC:

![imagen](https://github.com/mateosolinho/proyecto-final/assets/124877302/ae01e6e5-2b9c-4338-bbf6-54cdac5e9fb9)

### 30/04

## Calibracion de la probabilidad

Es generalmente util tener una probabilidad en vez de una prediccion concreta, pero algunos algoritmos no nos lo dan

Algunas tecnicas de evaluacion requieren esta probabilidad

Sklearn nos facilita una manera de "calibrar" la pseudo probabilidad que tenemos para que esta se comporte mejor

*Añadido calibracion.py*

Output:

![imagen](https://github.com/mateosolinho/proyecto-final/assets/124877302/a2cd9b01-c612-45fa-98a6-66d62ceed4b7)

## Optimizacion basica

Para conseguir los mejores resultados es necesario optimizar los modelos que entrenamos

Nos centramos en 3 patas principales:
- Seleccionar los mejores features
- Elegir los hiperparametros
- Mejorar nuestro pipeline

## Eligiendo los mejores features

Puede ser importante reducir el numero de features que tenemos para:
- Mejorar los resultados
- Reducir overfiting
- Mejorar interpretabilidad

Sklearn nos facilita este procesp de varias maneras

## Resumen

Scikit-learn es una libreria muy poderosa ya que contruye un framework completo para el proceso de construir modelos

Ademas de modelos tipicos de ML, existen implementaciones para muchos mas procesos, como la preparacion de los datos

La ventaja de utilizar sklearn es el poder de combinaar todos los pasos en un unico sitio de forma muy flexible

***Examen Curso de Machine Learning supervisado con Scikit-learn***

- **Intento 1 -> 17 aciertos** - Aprobado

## ML no supervisado en Python

## Introduccion a Scikit-learn

Una libreria que establece un framework para crear flujos de la creacion de algoritmos de ML

Unifica un campo muy diverso y abstrae las dificultades de cada algoritmo distinto

Nuevas librerias frecuentemente adoptan su sintaxis, facilitando su adaptacion

## Introduccion a K-Means

- Que es la clusterizacion?
Un campo que busca agrupar los datos en unos clusters compuestos por datos similares

En vez de predecir un arget, buscamos asignar este target a los datos

Aunque no tengamos un target especifico, construimos los clusters con un objetivo


Kmeans crea grupos centrados en la media de los datos que pertenecen al grupo

Nosotros tenemos que elegir el numero de grupos que existen y el algoritmo busca los centroides

La implementacion en sklearn es muy escalable y sigue el patron tipico de un modelo de aprendizaje supervisado

## Visualizando los resultados

Para evaluar los resultados es muy util visualizar los cluster qie estamos construyendo

Nos permite entender de una forma sencilla si los resultados tienen un sentido comun

Es importante combinar la prediccion del modelo con alguna libreria de visualizacion

*Añadido visualizacion.py*

```python
graph = (
    pn.ggplot(user_stats, pn.aes(x='followers', y='following', color='predictions_kmeans_3'))
    + pn.geom_point()
    + pn.scale_x_continuous(trans='log')
    + pn.scale_y_continuous(trans='log')
)

graph.draw();
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/b368f132-301a-48cd-b82a-eedb17a670d6)

```python
graph = (
    pn.ggplot(user_stats, pn.aes(x='followers', y='media', color='predictions_kmeans_3'))
    + pn.geom_point()
    + pn.scale_x_continuous(trans='log')
    + pn.scale_y_continuous(trans='log')
)

graph.draw();
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/d71b231b-19b0-4392-9748-53ded094e96c)

```python
graph = (
    pn.ggplot(user_stats, pn.aes(x='media', y='following', color='predictions_kmeans_3'))
    + pn.geom_point()
    + pn.scale_x_continuous(trans='log')
    + pn.scale_y_continuous(trans='log')
)

graph.draw();
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/2764ad7b-c625-4faf-807c-96b395f7a004)

```python
graph = (
    pn.ggplot(user_stats, pn.aes(x='followers', y='following', color='predictions_kmeans_10'))
    + pn.geom_point()
    + pn.scale_x_continuous(trans='log')
    + pn.scale_y_continuous(trans='log')
)

graph.draw();
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/7cb20bef-3a9b-43d6-b50e-4907e3b51387)

## Evaluando los resultados

Para una evaluacion mas rigurosa es importante usar las metricas de evaluacion para entender:
- Como de puros son los clusters
- Como de alejados estan uno del otro

Tambien tenemos que elegir el mejor numero de clusters y esto lo conseguimos con el famoso metodo del codo

*Añadido evaluacion.py*

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/0fbae6fc-bdb2-433b-893b-12ab03505990)

Tenemos disponibles varias metricas para medir la calidad de los clusters que utilizan los datos de entrada y los grupos aprendidos

Nos podemos aprovechar de esto para elegir el mejor numero de clusters utilizando el metodo del codo y buscando el outno de menor cambio de la metrica

## La preparacion tipica

El requisito basico es un conjunto de datos numericos

Normalmente preferimos trabajar con variables continuas para conseguir los mejores resultados

Kmeans es muy sensible a ciertos aspectos de los datos

## Eligiendo y normalizando las variables I

Mencionamos anteriormentw que Kmeans es muy sensible a los datos que utilizamos, por lo que es muy importante elegir las mejores variables

Es muy importante utilizar variables cateoricas, existen adaptaciones a kmeans

*Añadido variables.py*

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/52080b3b-2c04-4dc2-97c5-19769d7d2607)

El paso de elegir las variables es fundamental con el algoritmo de kmeans

### 02/05

## Eligiendo y normalizando las variables II

Kmeans depende de instancias, entonces es fundamental que las varaibles esten en la misma distancia

Existen varias maneras de hacer esto, pero es muy importante aprovecharse de los pipelines para crear procesos mejores

*Añadido visualizacion2.py*

Variables followers y following

```python
graph = (
    pn.ggplot(user_stats, pn.aes(x='followers', y='following', color='predictions_kmeans_5_scaler'))
    + pn.geom_point()
    + pn.scale_x_continuous(trans='log')
    + pn.scale_y_continuous(trans='log')
)

graph.draw();
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/0a8a171b-f2d0-43c5-8649-d3822423bdd9)

Variables followers y media

```python
graph = (
    pn.ggplot(user_stats, pn.aes(x='followers', y='media', color='predictions_kmeans_5_scaler'))
    + pn.geom_point()
    + pn.scale_x_continuous(trans='log')
    + pn.scale_y_continuous(trans='log')
)

graph.draw();
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/619dbc3f-a593-4dfc-b409-67525b174988)

Variables media y following

```python
graph = (
    pn.ggplot(user_stats, pn.aes(x='media', y='following', color='predictions_kmeans_5_scaler'))
    + pn.geom_point()
    + pn.scale_x_continuous(trans='log')
    + pn.scale_y_continuous(trans='log')
)

graph.draw();
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/a1ec382b-41b9-40e5-b6e0-3ec1ab6c3fbe)


## DBSCAN

Kmeans tiene algunas debilidades, principalemente:
- Tenemos que decidir cuantos grupos existen
- Prefiere variables contiguas ante categoricas

Dos alternativas populares:
- DBSCAN
- Clusterizacion jerarquica

DBSCAN es u algoritmo potente que evita el problema de definir el numero de clusters

Los resultados son similares a los del KMeans, pero ahora vemos que al incluir variables categóricas, también podemos distinguir grupos según si los tweets tienen o no retweets. Esto nos muestra cómo estas variables influyen en la agrupación de los datos junto con las numéricas, dándonos una visión más completa.

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/b3d810c9-5f15-4ae2-a536-212148c69827)

Dengogram:

*Añadido dendogram.py*

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/8ada9a75-a7f6-4e37-8951-0febdb19f0b4)


## Clusterizacion Grupos de Interes

Uno de los usos principales de la clusterizacion es la deteccion de los grupos de interes

Empezamos construyendo clusters con las variables de interes y hacemos un analisis posterior para entender los comportamientos que captamos

Podemos incorporar estos grupos en procesos de negocio

Este es un algoritmo que funciona de manera distinta a los otros que hemos visto hasta ahora

## Reduccion de dimensiones PCA:

La alta dimensionalidad es problematica por varios motivos:
- Es dificil extraer conocimiento concreto
- Modelos supervisados entrenando con muchas dimensiones son propensos a tener overfitting
- La significancia de los resultados se reduce

*Añadido pca.py*

2 dimensiones

```python
fig, ax = model.biplot(n_feat=6, alpha_transparency=0.1, hotellingt2=True)
ax.set_xlim([-5, 12])
ax.set_ylim([-1, 12])
fig
```

Ouput:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/374d91f0-f9a2-4d14-a44d-b7a45e3cadb9)

3 dimensiones

```python
fig, ax = model.biplot(n_feat=6, alpha_transparency=0.1, hotellingt2=True, d3=True)
ax.set_xlim([-5, 12])
ax.set_ylim([-1, 12])
ax.set_zlim([-6, 8])
fig
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/caf08288-c974-4007-b948-1d848eb0de3f)

## T-SNE

PCA es muy popular pero no es perfecto

Los algoritmos de t-SNE y UMAP son alternativas mas avanzadas que tambien son muy populares

Es comun primero aplicar un PCA para que se pueda ejecutar bien

## Resumen

El aprendizaje no supervisado no tiene en cuenta un target especifico, pero trabajamos con un objetivo concreto

Scikit-learn es muy util para una gran parte de aprendizaje no supervisado debido a su framework y sintaxis comun

La cluesterizacio busca grupos de datos comunes mientras la reduccion de dimensiones busca simplificar los datos

***Examen Curso de Machine Learning no supervisado en Python***

- **Intento 1 -> 12 aciertos**
- **Intento 2 -> 18 aciertos** - Aprobado

### 03/05

## Taller ML con clasificadores lineales en Python

```pyhton
graph = (
    pn.ggplot(tweet_data, pn.aes(x='0', y='nlikes'))
    + pn.geom_boxplot()
    + pn.coord_cartesian(ylim=[0, tweet_data.nlikes.quantile(0.90)])
    + pn.xlab('')
)

graph.draw();
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/8135e9b5-7706-459e-9f0d-a112bc8205a7)


Dividimos los datos en train y test

```pyhton
train, test = sklearn.model_selection.train_test_split(tweet_data, train_size=0.7, random_state=0)

train = train.reset_index(drop=True)
test = test.reset_index(drop=True)

print(train.shape)
print(test.shape)
```

Output:

```python
(28406, 57)
(12175, 57)
```

Grafico de seguidore sy probabilidad de popularidad por video

```python
train['video'] = train.video.astype(bool)

graph = (
    pn.ggplot(train, pn.aes(x='following', y='predictions_1', color='video'))
    + pn.geom_line()
    + pn.ylab('Probability of being popular')
)

graph.draw();
```

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/5109e382-b0e5-4b5c-9f32-6c2b41c79a17)

De esta manera podemos crear nuevas variables

```python
train['has_hashtags'] = (train.hashtags.str.len() > 2).astype(int)

train['is_english'] = (train.language == 'en').astype(int)

train['avg_likes'] = train.likes / train.tweets
train['followers_per_tweet'] = train.followers / train.tweets

train['is_reply'] = (train.reply_to.str.len() > 2).astype(int)

potential_variables = [
    'has_hashtags', 'is_english', 'avg_likes', 'followers_per_tweet', 'is_reply'
]

for variable in potential_variables:
    print(f'For variable {variable}:')
    print(train.groupby(target)[variable].agg(['mean', 'sem']))
    print('\n')
```

La curva de precision recall es fundamental para entender los resultados y como se podrian aplicar a una problema real de negocio, la dibujamos utilizando scikit-learn.

```pyhton
c = (results.recall_diff >= 0)
graph = (
    pn.ggplot(results[c], pn.aes(x='recall', y='precision', color='prediction_number'))
    + pn.geom_line(size=1.4)
)

graph.draw();
```

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/b4fd6f14-3cbb-4ae8-97d2-0500d46a1a17)

## Taller ML con modelos basados en arboles en Python

Empezamos entrenando un arbol de decision para entender que hay pro debajo de los arboles de decision

```pyhton
auc_train = sklearn.metrics.roc_auc_score(train[target], train[pred_col])
auc_test = sklearn.metrics.roc_auc_score(test[target], test[pred_col])

acc_train = sklearn.metrics.accuracy_score(train[target], train[pred_col].round())
acc_test = sklearn.metrics.accuracy_score(test[target], test[pred_col].round())

print(f'The auc in train is {auc_train:.3} and in test it is {auc_test:.3}, the accuracies are {acc_train:.1%} and {acc_test:.1%}')
```

Output:

```python
The auc in train is 0.995 and in test it is 0.853, the accuracies are 96.1% and 87.0%
```
En esta caso los resultados no parecen malos, el modelo ha podido incorporar casi todos los datos y producir un resultado bastante bueno

```python
feature_names = train.language.sort_values().unique().tolist() + numeric_variables

plt.figure(figsize=(25, 12))
sklearn.tree.plot_tree(
    full_pipeline['classifier'], fontsize=12, feature_names=feature_names, class_names=[f'Under {cutoff}', f'Over {cutoff}'], max_depth=4, 
    impurity=False, proportion=True, precision=2
)
plt.show()
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/caacb84d-02cd-40ba-b69d-3bb21effa6c3)

```python
graph_data = pd.DataFrame(
    [(imp, variable) for imp, variable in zip(full_pipeline['classifier'].feature_importances_, feature_names)], 
    columns=['importance', 'variable']
).sort_values('importance', ascending=False)

limit = 15
graph = (
    pn.ggplot(graph_data.head(limit), pn.aes(x='variable', y='importance')) 
    + pn.geom_col()
    + pn.coord_flip()
    + pn.theme(figure_size=(7, 5))
    + pn.scale_x_discrete(limits=graph_data.head(limit).variable.unique()[::-1])
)

graph.draw();
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/9c920c76-970e-4ec2-8780-084a02932186)

Podemos ver que los followers por tweet es un feature muy importante

Ahora vamos a intentar hacer lo que hemos hecho, pero utilizando 2 modelos más complejos, RandomForest y XGBoost.

```python
The auc in train is 0.938 and in test it is 0.936, the accuracies are 88.4% and 87.8%
```

En este caso conseguimos una mejora muy ligera, y ademas hemos utilizado los mismos parametros para mejorar un poco el overfitting

```pyhton
graph_data = pd.DataFrame(
    [(imp, variable) for imp, variable in zip(full_pipeline['classifier'].feature_importances_, feature_names)], 
    columns=['importance', 'variable']
).sort_values('importance', ascending=False)

limit = 20
graph = (
    pn.ggplot(graph_data.head(limit), pn.aes(x='variable', y='importance')) 
    + pn.geom_col()
    + pn.coord_flip()
    + pn.theme(figure_size=(7, 5))
    + pn.scale_x_discrete(limits=graph_data.head(limit).variable.unique()[::-1])
)

graph.draw();
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/9d404f60-0604-4662-a9ec-c53f1fc4fa95)

Podemos ver que los resultados son sim ilares, pero los resultados son mucho menos extremos que los anteriores

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/b9886380-beb6-4de4-8671-4c343dc7593e)

De nuevo hemos conseguido una mejora significativa pero el over training es mas exagerado. La importancia de las variables ha cambiado, otra vez siendo mas extremo.

Si optimizamos los pipelines y el metodo de train podemos conseguir mejorar tanto de rendimiento como de accuracies bastante significativas

```python
The auc in train is 0.963 and in test it is 0.948, the accuracies are 90.8% and 89.2%
```

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/34b4d244-17a3-4d5f-8005-0d7f588aeb60)

En esta grafica podemos apreciar unos resultados bastante mejores para random forest y XGBoost, conseguimos un 0.4 de recall con 100% de precision

## Taller Reduccion de dimensionalidad para ML en Python

El PCA es una de las grandes tecnicas para hacer reduccion de dimensiones

```python
pca_pipeline = Pipeline(
    [
        ('scaler', preprocessing.StandardScaler()),
        ('pca', PCA(random_state=0))
    ]
)

pca_pipeline.fit(user_stats[variables])

transformed_data = pd.DataFrame(pca_pipeline.transform(user_stats[variables]))
transformed_data.columns = [f'component_{i+1}' for i in range(transformed_data.shape[1])]

graph_data = pd.DataFrame(pca_pipeline['pca'].explained_variance_ratio_.cumsum(), columns=['explained_variance']).reset_index()

graph = pn.ggplot(graph_data, pn.aes(x='index', y='explained_variance')) + pn.geom_col() + pn.xlab('Component') + pn.scale_y_continuous(labels=percent_format())
graph.draw();
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/882544e5-fbd1-45f4-8fe6-e53ffeac6dc7)

Cuando no especificamos un numero de componentes el PCA devuelve todos los posibles

```python
limit_x = transformed_data.component_1.quantile(0.95)
limit_y = transformed_data.component_2.quantile(0.95)

condition = (transformed_data.component_1 < limit_x) & (transformed_data.component_2 < limit_y)

graph = (
    pn.ggplot(transformed_data[condition], pn.aes(x='component_1', y='component_2'))
    + pn.geom_point()
)

graph.draw();
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/a70c950c-3aaf-4363-90fc-f516f15438fb)

```python
limit_x = transformed_data.component_1.quantile(0.95)
limit_y = transformed_data.component_2.quantile(0.95)
limit_z = transformed_data.component_3.quantile(0.95)

condition = (transformed_data.component_1 < limit_x) & (transformed_data.component_2 < limit_y) & (transformed_data.component_3 < limit_z)

graph = (
    pn.ggplot(transformed_data[condition], pn.aes(x='component_1', y='component_2', color='component_3'))
    + pn.geom_point()
)

graph.draw();
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/8a8d4773-fd3f-45d2-bce4-d93a179a1028)

Asi podemos visualizar los datos en diferentes componentes en un grafico
Podemos ver que algunos de los datos se encuentran en los extremos de estos componentes

Para saber la relacion que tienen nuestros compoentes con las variables iniciales usamos Biplot

```python
fig, ax = model.biplot(n_feat=6, alpha_transparency=0.1, hotellingt2=True, visible=False)
ax.set_xlim([-2, 6])
ax.set_ylim([-1, 6])
fig.set_visible(True)
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/1fe0e379-243c-47f0-af4e-15cf18088f40)


```python
fig, ax = model.biplot(n_feat=6, alpha_transparency=0.1, hotellingt2=True, d3=True, visible=False)
ax.set_xlim([-2, 6])
ax.set_ylim([-1, 4])
ax.set_zlim([-6, 5])
fig.set_visible(True)
```

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/491684c4-5451-464d-a6c3-aaa3893603a5)

Las flechas nos muestran las variables iniciales y podemos entender que cietas variables tienen una correlacion alta con los componentes

En la ultima imagen podemos ver lo mismo pero en 3D, nuestros tres primeros componentes se definen por, el numero de retweets, el numero de respuestas de media, el numero de tweets

Esto es interesante ya que corresponde con los 3 tipos de tweet diferente que se pueden hacer, por lo que entendemos que nuestro conjunto de usuarios se explican principalmente por estas variables

Podemos aprovechar esta reduccion de dimensxiones para hacer un clustering de datos

```python
graph = (
    pn.ggplot(transformed_data[transformed_data.predictions_clusters != '-1'], pn.aes(x='component_1', y='component_2', color='predictions_clusters'))
    + pn.geom_point()
)

graph.draw();
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/eeeaca18-85d6-4531-8b46-65344acb6645)

En esta imagen podemos ver que el algoritmo ha conseguido identificar unos clusters bastante claros, hay una gran masa de usuarios en el centro y luego tenemos grupos de usuarios en los diferentes lados
Por otra parte los puntos rojos son que no pertenecen a ningun grupo en especifico

```python
prct_changes = ((transformed_data.groupby('predictions_clusters')[vis_vars].mean() - transformed_data[vis_vars].mean()) / transformed_data[vis_vars].mean()).reset_index()
graph_data = pd.melt(prct_changes, 'predictions_clusters')

graph = (
    pn.ggplot(graph_data[graph_data.predictions_clusters != '-1'], pn.aes(x='predictions_clusters', y='value', fill='variable'))
    + pn.geom_col(position='dodge')
    + pn.theme(figure_size=(10, 5))
    + pn.scale_y_continuous(labels=percent_format())
    + pn.scale_x_discrete(labels=[str(i) for i in range(graph_data[graph_data.predictions_clusters != '-1'].predictions_clusters.nunique())])
    + pn.ylab('Percentage increase over the global average')
)

graph.draw();
```

Output:

![Sin título](https://github.com/mateosolinho/proyecto-final/assets/124877302/733972b7-4918-40be-8d20-f65bf81749e6)

Observando este grafico, podemos ver que muchos de los clusters tienen un valor muy fuerte en alguna variable y ademas que mucho tambien tienen una mezcla de cosas unicas, como el 1 que tiene un numero regular de todo pero con mas replies

# Resumen

Para finalizar con el proyecto final y ambas carreras de openwebinars, en mi opinion la Carrera que mas me ha gustado y mas interesante me ha parecido ha sido la de Machine Learning con Python
Por otra parte ambas me ha parecido que tenian contenido dificil de comprender pero una buena base para comenzar y entender bien la mayoria de contenidos, sin embargo en el caso de la de Machine Learning a mi parecer hay terminos mas complejos y ha habido veces que algunas cosas no las acababa de entender del todo
