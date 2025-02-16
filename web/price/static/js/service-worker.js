self.addEventListener("push", function (event) {
    console.log("called")
    const data = event.data.json();
    // self.registration.showNotification(data.head, {
    //     body: data.body,
    //     icon: data.icon,
    //     data: { url: data.url },
    // });
    
    self.registration.showNotification("whowhwo", {body : "test"})
    
    
});

self.addEventListener("notificationclick", function (event) {
    event.notification.close();
    event.waitUntil(clients.openWindow(event.notification.data.url));
});

self.addEventListener("activate", async (e) => {
    const sbscription = await self.registration.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: urlBase64ToUint8Array("BKneT1QFFUoQoP1dCz-xI0xnKwVHbQU2YQREEj-vNxZ0X18Kby7KIeqTfXFlzR_aUm09zg4jEKUfGXletOAbPXA")
    });
    const response = await saveSubscription(sbscription)
    console.log(response)
    
})



const urlBase64ToUint8Array = base64String => {
    const padding = '='.repeat((4 - (base64String.length % 4)) % 4);
    const base64 = (base64String + padding)
        .replace(/\-/g, '+')
        .replace(/_/g, '/');

    const rawData = atob(base64);
    const outputArray = new Uint8Array(rawData.length);

    for (let i = 0; i < rawData.length; ++i) {
        outputArray[i] = rawData.charCodeAt(i);
    }

    return outputArray;
}

const saveSubscription = async (subscription) => {

    console.log(cookieStore)
    const response = await getCSRFToken().get("csrftoken").then(token => {        
        return fetch('http://127.0.0.1:8000/price/save_subscription/', {
            method : "post",
            headers : {"header" : "X-CSRFTOKEN",             
                      'X-Requested-With': 'XMLHttpRequest',
                    "Content-Type": "application/json",
                    'X-CSRFTOKEN': token } ,
            body : JSON.stringify(subscription)
        })
    })
    

    
    return response.json()
}


function getCSRFToken() {
    return fetch("http://127.0.0.1:8000/price/get-csrf-token/", {
        credentials: "include", // include-cookie
    }).then(response => response.json())
    .then(data => {
        console.log(data.token)
        return data.token
    })
}


//for pwa
var staticCacheName = 'djangopwa-v1';
 
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '',
      ]);
    })
  );
});
 
self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match(''));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});