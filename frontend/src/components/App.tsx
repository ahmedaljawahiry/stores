import React, {useState} from 'react';
import '../css/App.css';
import Results from "./Results";
import {fetchStores, Store, STORES_URL} from "../services/storesService";

export default function App() {

    const [search, setSearch] = useState<string>('');
    const [stores, setStores] = useState<Array<Store>>([]);

    async function fetchData(e: any) {
        e.preventDefault();
        const response = await fetchStores(STORES_URL + `?search=${search}`);
        setStores(response.data);
    }

    return (
        <div className="App">
            <form onSubmit={fetchData}>
                <input value={search} onChange={(e) => setSearch(e.target.value)} placeholder='Search...'/>
                <br/>
                <button>Search</button>
            </form>
          <Results data={stores}/>
        </div>
      );
}