import React, {useState} from "react";


function SearchBar(props){
    const [input, setInput] = useState("")

    function handleSubmit(e){
        e.preventDefault()
        props.onSubmit(input)
        setInput("")
    }

    return(
        <form onSubmit={handleSubmit}>
            <input
            onChange={(e) => setInput(e.target.value)}
            value={input} 
            type="text"
            placeholder="Search artwork..."/>
            <button type="submit">Search</button>
        </form>
    )
}

export default SearchBar