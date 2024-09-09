import axios from 'axios';

const signup = async (formData) => {
    // Replace url with deployed backend service
    axios.post('http://localhost:8080/aspectus/users/createAccount', formData
    ).then( response => {
        console.log(response.data);
        return response.data;
    }).catch(error => {
        console.log(error.response.data);
        return error.response.data;
    });
}

export default signup
