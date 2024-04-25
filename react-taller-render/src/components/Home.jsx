import React from "react";
import { Link } from "react-router-dom";

export default () => {
    const greet = () => {
        alert(Hello)
    }

    return (
        <>
            <h1>Home Page</h1>
            <button onClick={greet}>Greet</button>
            <Link to="/about">About</Link>
        </>
    )
};