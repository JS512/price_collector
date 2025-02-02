
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


function set_table(source){
    var url_list = document.getElementById("url_list");
    var table = document.createElement("table");
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

    url_list.appendChild(table);

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
      type: 'bar',
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
