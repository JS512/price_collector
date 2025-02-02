var data;


function load_setting_data(){
    return fetch('../../static/settings.json')
    .then(response => response.json())
    .then(response => {data = response; console.log(data)})
    .catch(error => console.log(error))
}