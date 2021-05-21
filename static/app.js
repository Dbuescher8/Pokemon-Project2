function buildPlot(id) {
    d3.json("/api/v1.0/" + id).then((importedData) => {
    // console.log(importedData);
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
    
        // data
        var chartData = [trace1];
    
        // Apply the group bar mode to the layout
        var layout = {
        title: "helf",
        margin: {
            l: 100,
            r: 100,
            t: 100,
            b: 100
        },
        height: 600,
        width: 1200
        };
    
        // Render the plot to the div tag with id "plot"
        Plotly.newPlot("bar", chartData, layout);

        var data2 = importedData;
        data2.sort(function(a, b) {
            return parseFloat(b.attack) - parseFloat(a.attack);
        });
        // data2 = data2.slice(0,5);
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
            title: "attac",
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

// function plotInfo(id) {
//     d3.json("flaskDataPull.json").then((data)=> {
//         var metadata = data;
//         var metadataFilter = metadata.filter(meta => meta.id.toString() === id)[0];

//         var pokeSet = d3.select("#sample-metadata");
//         pokeSet.html("");
        
//         Object.entries(metadataFilter).forEach((key)=> {
//             pokeSet.append("h5").text(key[0].toUpperCase() + ": " + key[1] + "\n");
//         });
//     });
// }

// function sampleSelection(id) {
//     buildPlot(id);
//     plotInfo(id);
// }

function init() {
    var dropdownMenu = d3.select("#selDataset");
    d3.json("/api/v1.0/types").then((data)=>{
        var pokeList = []
        data.forEach(function(type) {
            if (pokeList.indexOf(type.pokeType)<0) {
                pokeList.push(type.pokeType)
            }
        });
        //  loop through to find if type exists, append
        pokeList.forEach(function(type) {
            dropdownMenu.append("option").text(type).property("value");
        });
        // Binding event
        dropdownMenu.on("change",function(){
            console.log(this)
            // set variable for pokeType - "this" in console.log(this)
        });
        buildPlot("grass");
        // replace "dragon" with variable for Type
        // plotInfo(data.names[0]);
    });
}

init();