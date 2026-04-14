import React from "react";

const SearchArt = async (query) => {
    const response = await fetch("http://localhost:8000/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            input: query,
        }),
    });

    return response.json()
}

export default SearchArt