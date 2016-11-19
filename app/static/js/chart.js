/**
 * Created by Akash on 11/19/2016.
 */
var ctx = document.getElementById("chart");
console.log("Hey");

var convertDataToChart = function(label, dataSet) {
    xLabels = [];
    yPoints = [];
    for (var entry in dataSet) {
        if (dataSet.hasOwnProperty(entry)) { // this will check if key is owned by data object and not by any of it's ancestors
            xLabels.push(entry);
            yPoints.push(dataSet[entry][label])
        }
    }

    createChart(xLabels, yPoints);
};

var createChart = function (xLabels, yPoints) {
    var lineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: xLabels,
            datasets: [{
                data: yPoints,
                fill: false,
                borderColor: "rgba(75,192,192,1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "rgba(75,192,192,1)",
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                label: "Smile"
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: "Time"
                    }
                }],
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: "Happiness"
                    }
                }]
            }
        }
    });
};