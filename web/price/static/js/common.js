var data;

if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/static/js/service-worker.js')
        .then(registration => {
          console.log('Service Worker registered with scope:', registration.scope);
        })
        .catch(error => {
          console.error('Service Worker registration failed:', error);
        });
    });
  }

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