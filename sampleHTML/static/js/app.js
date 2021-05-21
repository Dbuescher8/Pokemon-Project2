var tableData = data;

var tbody = d3.select("tbody");
tableData.forEach(function(ufo){
    var row = tbody.append("tr");
    Object.entries(ufo).forEach(function([key,value]){
        var cell = row.append("td");
        cell.text(value);
    });
});

var button = d3.select("#filter-btn");
button.on("click",function(event){
    d3.event.preventDefault();
    tbody.html("");
    var filterDate = d3.select("#datetime");
    var filterValue = filterDate.property("value");
    var filterCity = d3.select("#city").property("value");
    var filterState = d3.select("#state").property("value");
    var filterCountry = d3.select("#country").property("value");
    var filterShape = d3.select("#shape").property("value");
    var filterData = tableData;
    if (filterValue){
        filterData = filterData.filter(row => row.datetime === filterValue);
    }
    if (filterCity){
        filterData = filterData.filter(row => row.city === filterCity);
    }
    if (filterState){
        filterData = filterData.filter(row => row.state === filterState);
    }
    if (filterCountry){
        filterData = filterData.filter(row => row.country === filterCountry);
    }
    if (filterShape){
        filterData = filterData.filter(row => row.shape === filterShape);
    }
    filterData.forEach(function(ufoDate){
        var row = tbody.append("tr");
        Object.entries(ufoDate).forEach(function([key,value]){
            var cell = row.append("td");
            cell.text(value);
        });
    });
});


