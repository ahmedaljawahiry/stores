import React from "react";
import {Store} from "../services/storesService";
import "../css/Results.css";

interface Props {
    data?: Array<Store>
}

export default function Results(props: Props) {
    if (props.data) {
        return <div>
            <div>Result count: {props.data.length}</div>
            <div id='results'>
                {props.data.map(result => <div key={result.postcode}>
                    <span>{result.name}, {result.postcode}</span>
                    <br/>
                </div>)}
            </div>
        </div>
    }
    return null;
}