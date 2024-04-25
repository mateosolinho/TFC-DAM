import React from "react";
import { hydrate } from "react-dom"
import { BrowserRouter } from "react-router-dom";
import App from "./components/App";

const AppWithRouter = () => {
    <BrowserRouter>
        <App />
    </BrowserRouter>
}

hydrate(<App />, document.getElementById('app'));