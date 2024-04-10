import React from "react";
import './App.css'

const wishes = [
    { text: "Travel to the moon", done: false },
    { text: "Pay the gym", done: true },
    { text: "Go to the gym", done: false },
];

const App = () => (
    <div className="app">
        <h1>My Wishlist</h1>
        <fieldset className="wish-input">
            <legend className="wish-input__label">New Wish</legend>
            <input className="wish-input_field" placeholder="Enter what do you wish here" />
        </fieldset>
        <ul className="wish-list">
            {wishes.map(({ text, done }, i) => (
                <li key={text} className={`wish-list__item ${done ? 'wish-list__item--done' : ''}` }>
                    <label htmlFor={`wish${i}`}>
                        <input id={`whis${i}`} type="checkbox" checked={done} />
                        {text}
                    </label>
                </li>
            ))}
        </ul>
        <button className="wish-clear" type="button">Archive done</button>
    </div>
);

export default App;