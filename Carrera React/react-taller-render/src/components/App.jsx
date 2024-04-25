import React from "react";
import { Route, Switch } from "react-router-dom";
import Home from "./Home";
import About from "./About";

export default () => {
    <Switch>
        <Route path="/" exact={true} Component={Home}></Route>
        <Route path="/about" exact={true} Component={About}></Route>
    </Switch>
}