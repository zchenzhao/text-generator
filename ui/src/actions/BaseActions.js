
const BaseActions = {
    baseURL: process.env.REACT_APP_URL,

    postToGenerateText: function(body) {
        const url = "/generate_text";
        const fullURL = this.baseURL.concat(url);

        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                opening_word: body
            }),
        };

        return fetch(fullURL, requestOptions)
        .then(result => {
            return result;
        }).catch(error => {
            console.log(error);
            return null;
        });
    }
}

export default BaseActions;