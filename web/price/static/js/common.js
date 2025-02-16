var data;



function load_setting_data(){
    return fetch('../../static/settings.json')
    .then(response => response.json())
    .then(response => {data = response; console.log(data)})
    .catch(error => console.log(error))
}

// csrftoken 쿠키에서 값을 가져오는 함수
function getCsrfTokenFromCookie() {
    const cookies = document.cookie.split('; ');
    for (let i = 0; i < cookies.length; i++) {
        const [name, value] = cookies[i].split('=');
        if (name === 'csrftoken') {
            return value;
        }
    }
    return null;  // CSRF 토큰이 없을 경우 null 반환
}


async function setCookieStore(value) {    
    await cookieStore.set({
        name : "csrftoken",
        value : value
    })
}

cookieStore.addEventListener("change", async (event) => {
    await setCookieStore(getCsrfTokenFromCookie());
});