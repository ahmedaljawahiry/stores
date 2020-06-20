import React from "react";
import "../css/Search.css"

interface Props {
    value: string,
    onChange: (v: string) => void,
    onSubmit: (e: any) => void
}

export default function Search(props: Props) {
    return <form onSubmit={props.onSubmit}>
        <input value={props.value} onChange={(e) => props.onChange(e.target.value)} placeholder='Search...'/>
        <br/>
        <button type='submit'>Search</button>
    </form>
}