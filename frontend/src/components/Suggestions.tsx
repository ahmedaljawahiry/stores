import React from "react";
import "../css/Suggestions.css"


interface Props {
    data: Array<string>,
    onClick: (v: string) => void
}

export default function Suggestions(props: Props) {

    if (!props.data.length) return null;
    return <div id="suggestions-container">
        {props.data.map(text => <div key={text}>
            <div className="suggestion" onClick={() => props.onClick(text)}>{text}</div><br/>
        </div>)}
    </div>
}