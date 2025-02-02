
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
        cell1.innerHTML = '<input type="text" placeholder="이름 입력">';
        cell2.innerHTML = '<input type="number" placeholder="나이 입력">';
        cell3.innerHTML = '<input type="text" placeholder="직업 입력">';
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
        table.appendChild(tr);
    }

    table_body.appendChild(table);
    url_list.appendChild(table_body)

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
