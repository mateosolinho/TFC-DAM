import React from "react";
import { renderToString } from "react-dom/server";
import App from "./components/App";

const render = (req, res) => {
    const markup = renderToString(<App />)

    res.send(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>SSR workshop</title>
            <script src="./app.js" defer></script>
            <script src="./vendor.js" defer></script>
        </head>
        <body>
            <div id="app">
                ${markup}
            </div>
        </body>
        </html>
    `)

}