import React from "react";
import ArtworkCard from "./ArtworkCard";

function Gallery(props){

    return (
        <div className="grid">
            {props.artwork.map((art)=>(
                <ArtworkCard art={art} key={art.id} />
            ))}
        </div>
    )
}

export default Gallery