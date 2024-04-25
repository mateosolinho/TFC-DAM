import React, { lazy, Suspense } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
// import Home from "./components/Home";
// import About from "./components/About";

const About = lazy(() => import('./components/About'));
const Home = lazy(() => import('./components/Home'))

export default () => {
    <BrowserRouter>
        <Suspense fallback={<h1>Loading...</h1>}>
            <Switch>
                <Route path="/" exact={true} Component={Home} />
                <Route path="/about" exact={true} Component={About} />
            </Switch>
        </Suspense>
    </BrowserRouter>
}