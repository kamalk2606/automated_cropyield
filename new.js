const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://weather338.p.rapidapi.com/locations/search',
  params: {
    query: 'Hyderabad',
    language: 'en-US'
  },
  headers: {
    'X-RapidAPI-Key': '09f9ee34ccmsh2a3d0be0f89ff81p10ad72jsn6b824fb7399e',
    'X-RapidAPI-Host': 'weather338.p.rapidapi.com'
  }
};

try {
	const response = await axios.request(options);
	console.log(response.data);
} catch (error) {
	console.error(error);
}