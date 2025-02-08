
document.addEventListener("DOMContentLoaded", ()=> {
	load_setting_data().then(response => load_chart_data())
});


async function load_chart_data(){
    console.log(data)
    var res = await fetch(data["get_user_chart_data"], {
        method: "GET",        
        headers: {
          "Content-Type" : "application/json"
        }
      }
    );
    
    var res_data = await res.json()
    if(res.status == 200){
        set_table(res_data)
        
    }else{
      console.log(res_data)
    }
    
}


function create_table_input_row(){
    let table = document.getElementById("url_list").getElementsByTagName("tbody")[0]
    let new_row = table.insertRow();

    let cell1 = new_row.insertCell(0);
    let cell2 = new_row.insertCell(1);
    let cell3 = new_row.insertCell(2);

    // 입력 가능한 칸 생성
    cell1.innerHTML = '<input type="text" name="url[]" placeholder="URL">';
}

function set_table(source){
    var url_list = document.getElementById("url_list");    
    var table = document.createElement("table");
    var table_body = document.createElement("tbody");

    var links = source["links"];
    var canvas_ids = [];

    for(var i=0; i<links.length; i++){
        var tr = document.createElement("tr");

        var url = document.createElement("td")
        url.innerHTML = links[i];

        var chart = document.createElement("td");
        var id = "acquisitions_" + i;
        canvas_ids.push(id);
        var canvas_container = create_chart_canvas(id,
            source["chart_data"][i]["labels"],
            source["chart_data"][i]["data"]
        );

        chart.appendChild(canvas_container);

        tr.appendChild(url)
        tr.appendChild(chart)
        table_body.appendChild(tr);
    }

    table.appendChild(table_body);
    url_list.appendChild(table)

    for(var i=0; i<canvas_ids.length; i++){
        document.getElementById(canvas_ids[i]).style.width="800px";
    }
}

function create_chart_canvas(id, labels, chart_data){
    var canvas_container = document.createElement("div");
    var canvas = document.createElement("canvas");
    canvas_container.appendChild(canvas);    

    canvas.setAttribute("id", id);    
    canvas.style.width="800px";

    set_chart(canvas, labels, chart_data);

    
    return canvas_container

}

function set_chart(element, labels, chart_data){
    console.log(labels, chart_data)
    let myChart = new Chart(element, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [
          {
            label: 'Dataset',
            data: chart_data,
          }
        ]
      },
    });
}


function save_urls() {
  const urls = Array.from(document.querySelectorAll('input[name="url[]"]'))
                       .map(input => input.value)
                       .filter(value => value);
  let send_data  = {
    "urls" : urls
  }
  // const header = document.querySelector('meta[name="_csrf_header"]').content;
  //   const token = document.querySelector('meta[name="_csrf"]').content;
  const csrfToken = getCsrfTokenFromCookie();
	fetch(data["save_url"], {
            method: "POST",
            headers: {   
                "header" : "X-CSRFTOKEN",             
              	'X-Requested-With': 'XMLHttpRequest',
                "Content-Type": "application/json",
                'X-CSRFTOKEN': csrfToken	// header에 X-CSRF-Token부분에 토큰값이 들어가 정상적으로 POST값이 넘어가는 것을 볼 수 있다!
            },
            body: JSON.stringify(send_data)
        })
}