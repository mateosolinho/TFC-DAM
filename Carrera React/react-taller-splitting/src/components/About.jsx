import { toUpper } from "lodash";
import React from "react";
import { Link } from "react-router-dom";
// import toUpper from 'lodash/toUpper';

// console.log(toUpper('hola'));

export default () => {
    const { title, setTitle } = React.useState('Open Webinars');

    const handler = () => {
        import('lodash/toUpper')
            .then(toUpper => {
                setTitle(toUpper.default(title))
            })
    }

    return <>

        <h1>About Page</h1>
        <h2>{title}</h2>
        <button onClick={handler}>To upper title</button>
        <Link to={"/"}>Back Home</Link>

    </>
}