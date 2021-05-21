function buildPlot(id) {
    d3.json("/api/v1.0/" + id).then((importedData) => {
        var data = importedData;

        data.sort(function(a, b) {
        return parseFloat(b.hp) - parseFloat(a.hp);
        });
    
        var trace1 = {
        y: data.map(row => row.hp),
        x: data.map(row => row.name),
        text: data.map(row => row.name),
        name: "Health",
        type: "bar",
        orientation: "v"
        };
    
        var chartData = [trace1];
    
        var layout = {
        title: "HP",
        margin: {
            l: 100,
            r: 100,
            t: 100,
            b: 100
        },
        height: 600,
        width: 1200
        };
    
        Plotly.newPlot("bar", chartData, layout);

        var data2 = importedData;
        data2.sort(function(a, b) {
            return parseFloat(b.attack) - parseFloat(a.attack);
        });
        var trace2 = {
            x: data2.map(row=>row.name),
            y:data2.map(row=>row.attack),
            text: data2.map(row=>row.name),
            name: "Attack",
            type: 'scatter',
            mode: 'lines+markers'
        };
        var chartData2 = [trace2];
        var layout2 = {
            title: "Attack",
            margin: {
                l: 100,
                r: 100,
                t: 100,
                b: 100
            },
            height: 600,
            width: 1200
        };
        Plotly.newPlot("scatter",chartData2,layout2);
  });
}

function plotInfo(id) {
    d3.json("/api/v1.0/" + id).then((importedData)=> {
        var data = importedData;
        data.sort(function(a, b) {
            return parseFloat(b.name) - parseFloat(a.name);
            });

        var pokeSet = d3.select("#sample-metadata");
        pokeSet.html("");
        
        Object.entries(data).forEach(function(Pokemon) {
            console.log(Pokemon);
            pokeSet.append("h5").text(Pokemon[1]["name"].toUpperCase() + "\n");
        });
    });
}

function init() {
    var dropdownMenu = d3.select("#selDataset");
    d3.json("/api/v1.0/types").then((data)=>{
        var pokeList = []
        data.forEach(function(type) {
            if (pokeList.indexOf(type.pokeType)<0) {
                pokeList.push(type.pokeType)
            }
        });
        dropdownMenu.append("option").text("-select-").property("value");
        //  loop through to find if type exists, append
        pokeList.forEach(function(type) {
            dropdownMenu.append("option").text(type).property("value");
        });
        // Binding event
        dropdownMenu.on("change",function(){
            console.log(this.value)
            buildPlot(this.value)
            plotInfo(this.value)
        });
    });
}

init();