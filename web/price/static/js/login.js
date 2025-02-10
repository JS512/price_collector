async function login(){
  var id = document.getElementById("id").value
  var pw = document.getElementById("pw").value
  user_obj = {
    "id" : id,
    "pw" : pw
  }
  var res = await fetch(data["login_server"] + data["login_api"], {
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
    window.location.replace(data["data_page"]);
  }else{
    console.log(res_data)
  }
}
