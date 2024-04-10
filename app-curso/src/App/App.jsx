import React, { useState } from "react";
import './App.css'
import WishInput from "./WishInput";
import WhisList from "./WishList";

const initialWishes = [
    { text: "Travel to the moon", done: false },
    { text: "Pay the gym", done: true },
    { text: "Go to the gym", done: false },
];

const App = () => {
    const [wishes, setWishes] = useState(initialWishes);
    return (

        <div className="app">
            <h1>My Wishlist</h1>
            <WishInput onNewWish={wish => setWishes(wish, ...wishes)} />
            <WhisList wishes={initialWishes} />
            <button className="wish-clear" type="button">Archive done</button>
        </div>
    );
};

export default App;