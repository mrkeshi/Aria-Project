import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:8000/";
//axios.defaults.baseURL = "https://localhost:5001";

export default {
    get: axios.get,
    post: axios.post,
    put: axios.put,
    delete: axios.delete
}
