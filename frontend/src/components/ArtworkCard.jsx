import React from "react";

function ArtworkCard(props){
    const image = props.art.image_id ?
    `https://www.artic.edu/iiif/2/${props.art.image_id}/full/843,/0/default.jpg`:
    `No Image Available`

    return (
        <div className="card">
            <img src={image} alt="image" />
            <h3>{props.art.title}</h3>
            <p>Artist: {props.art.artist}</p>
            <p>Release Date: {props.art.date}</p>
        </div>
    )
}

export default ArtworkCard