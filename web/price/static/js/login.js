// import data from "../../settings.json";
// console.log(data);


// export function a() {
//     alert("xxx")
// }

var data;

fetch('../static/settings.json')
  .then(response => response.json())
  .then(response => {data = response})
  .catch(error => console.log(error));



async function login(){
  var id = document.getElementById("id").value
  var pw = document.getElementById("pw").value
  user_obj = {
    "id" : id,
    "pw" : pw
  }
  var res = await fetch(data["login_server"], {
      method: "POST",
      mode : "cors",
      cache : "no-cache",
      credentials : "include",      
      headers: {
        "Content-Type" : "application/json"
      },
      body : JSON.stringify(user_obj)
    }
  );
  console.log(res)
  var res_data = await res.json()
  if(res.status == 200){
    // window.location.replace("http://example.com");
  }else{
    console.log(res_data)
  }
}

async function test(){
  var res = await fetch("http://127.0.0.1:5055/login", {
    method: "GET",    
    credentials : "include",      
    headers: {
      "Content-Type" : "application/json"
    }
  }
);
}


// async function login(){
//   var id = document.getElementById("id").value
//   var pw = document.getElementById("pw").value
//   user_obj = {
//     "id" : id,
//     "pw" : pw
//   }
//   var res = await fetch(data["login_server"], {
//       method: "POST",
//       mode : "cors",
//       cache : "no-cache",
//       credential : "same-origin",
//       crossDomain: true,
//       headers: {
//         "Content-Type" : "application/json"
//       },
//       body : JSON.stringify(user_obj)
//     }
//   );
//   console.log(res)
// }

