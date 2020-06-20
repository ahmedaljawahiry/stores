import React from "react";
import {Store} from "../services/storesService";
import "../css/Results.css";

interface Props {
    data: Array<Store>,
    total: number,
    loadMore: () => void
}

export default function Results(props: Props) {

    function onScroll(e: any) {
        // at bottom if (total scrollable height - scrolled height) is equal to the height of the div
        const reachedBottom = e.target.scrollHeight - e.target.scrollTop === e.target.clientHeight;
        if (reachedBottom) {
            props.loadMore();
        }
    }

    if (!props.data) return null;
    return <div>
        <div id='results-container' onScroll={onScroll}>
            {props.data.map(result => <div key={result.postcode}>
                <div className="result">{result.name}, {result.postcode}</div>
                <br/>
            </div>)}
        </div>
        <div>Results rendered: {props.data.length}</div>
        <div>Total number of results: {props.total || 0}</div>
    </div>
}