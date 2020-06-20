import React, {useState} from 'react';
import '../css/App.css';
import Results from "./Results";
import {fetchStores, Store, STORES_URL} from "../services/storesService";
import Search from "./Search";
import Suggestions from "./Suggestions";

export default function App() {

    const [search, setSearch] = useState<string>('');
    const [stores, setStores] = useState<Array<Store>>([]);
    const [suggestions, setSuggestions] = useState<Array<string>>([]);
    const [total, setTotal] = useState<number>(0);
    const [nextUrl, setNextUrl] = useState<string>();

    async function fetchData(e: any) {
        e.preventDefault();
        const response = await fetchStores(STORES_URL + `?search=${search}`);
        setStores(response.data);
        setNextUrl(response.next);
        setTotal(response.total);
    }

    async function loadSuggestions(searchValue: string) {
        if (searchValue.length < 2) {
            setSuggestions([]);
            return
        }
        const response = await fetchStores(STORES_URL + `?search=${searchValue}`);
        let matches: Array<string> = [];
        response.data.forEach(store => {
            const match = store.postcode.toLowerCase().includes(searchValue.toLowerCase()) ? store.postcode : store.name;
            matches.push(match);
        })
        setSuggestions(matches);
    }

    return (
        <div className="App">
            {nextUrl && <div className='fetch-url'><b>Fetch URL:</b> {nextUrl}</div>}
            <Search
                value={search}
                onChange={async (v) => {
                    setSearch(v);
                    await loadSuggestions(v);
                }}
                onSubmit={async (e) => {
                    setSuggestions([]);
                    await fetchData(e);
                }}
            />
            <Suggestions
                data={suggestions}
                onClick={(v) => {
                    setSearch(v);
                    setSuggestions([]);
                }}
            />
            <Results
                data={stores}
                total={total}
                loadMore={async () => {
                    if (nextUrl) {
                        const response = await fetchStores(nextUrl);
                        setStores(s => [...s].concat(response.data));
                        setNextUrl(response.next);
                    }
                }}
            />
        </div>
      );
}