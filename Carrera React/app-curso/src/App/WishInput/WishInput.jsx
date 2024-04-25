import React, { useState } from "react";
import PropTypes from "prop-types";

const WishInput = ({ onNewWish }) => {
    const [newWishText, setNewWishText] = useState('');
    return (
        <fieldset className="wish-input">
            <legend className="wish-input__label">New Wish</legend>
            <input
                className="wish-input_field"
                placeholder="Enter what do you wish here"
                value={newWishText}
                onChange={e => setNewWishText(e.target.value)}
                onKeyUp={e => {
                    if (e.key === 'Enter' && newWishText.length) {
                        onNewWish({ done: false, text: newWishText })
                        setNewWishText('')
                    }
                }} />
        </fieldset>
    );
};

WishInput.propTypes = {
    onNewWish: PropTypes.func
}

WishInput.defaultProps = {
    onNewWish: () => { },
}
export default WishInput;