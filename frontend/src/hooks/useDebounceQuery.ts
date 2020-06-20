import {useEffect} from "react";

interface Args {
    queryStr: string,
    query: (s: string) => void,
    debounceTime: number
}

export default function useDebounceQuery(args: Args) {

    const {queryStr, query, debounceTime} = args;

    useEffect(() => {
        const handler = setTimeout(() => query(queryStr), debounceTime);
        return () => {
            clearTimeout(handler);
        }
    // eslint-disable-next-line react-hooks/exhaustive-deps
    },[queryStr, debounceTime]) // dont want to add query() to deps
}