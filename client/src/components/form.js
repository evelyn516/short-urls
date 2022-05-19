import React from "react";

function Form() {
    return (
        <>
            <h1>Shorten your urls</h1>
            <form method='POST' action="https://shorter-urls-4all.herokuapp.com/">
                <input type="text" name="name" placeholder="enter a url that needs shortening" />
                <input type="submit" value="submit" />
            </form>
        </>
    )
};

export default Form;
