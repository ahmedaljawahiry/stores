
export type Store = {
    name: string,
    postcode: string
}

type PaginatedResponse = {
    total: number,
    page: string,
    next: string,
    previous: string,
    data: Array<Store>
}

export const STORES_URL = 'http://127.0.0.1:8000/stores/';

export async function fetchStores(url: string): Promise<PaginatedResponse> {
    const response = await fetch(url);
    return response.json()
}