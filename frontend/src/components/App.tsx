import React, {useState} from 'react';
import '../css/App.css';
import Results from "./Results";
import {fetchStores, Store, STORES_URL} from "../services/storesService";
import Search from "./Search";

export default function App() {

    const [search, setSearch] = useState<string>('');
    const [stores, setStores] = useState<Array<Store>>([]);
    const [total, setTotal] = useState<number>(0);
    const [nextUrl, setNextUrl] = useState<string>();

    async function fetchData(e: any) {
        e.preventDefault();
        const response = await fetchStores(STORES_URL + `?search=${search}`);
        setStores(response.data);
        setNextUrl(response.next);
        setTotal(response.total);
    }

    async function loadMore() {
        if (nextUrl) {
            const response = await fetchStores(nextUrl);
            setStores(s => [...s].concat(response.data));
            setNextUrl(response.next);
        }
    }

    return (
        <div className="App">
            <Search value={search} onChange={setSearch} onSubmit={fetchData}/>
            <Results data={stores} total={total} loadMore={loadMore}/>
        </div>
      );
}