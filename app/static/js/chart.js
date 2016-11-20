/**
 * Created by Akash on 11/19/2016.
 */
var ctx = document.getElementById("chart");

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

var convertDataToChart = function(label, dataSet) {
    xLabels = [];
    yPoints = [];
    for (var entry in dataSet) {
        console.log(entry);
        console.log(dataSet[entry][label]);
        // if (dataSet.hasOwnProperty(entry)) { // this will check if key is owned by data object and not by any of it's ancestors
            xLabels.push(entry);
            yPoints.push(dataSet[entry][label])
        // }
    }

    console.log(xLabels);
    console.log(yPoints);
    createChart(xLabels, yPoints);
};

// var dataset = $('#dataSetDiv').attr('val');
convertDataToChart('Smile', dataSetJson);
var jsonData = {0: {'Smile': 0.50381887}, 1: {'Smile': 0.5244584}, 2: {'Smile': 0.37471813}, 3: {'Smile': 0.3662309}, 4: {'Smile': 0.38467777}, 5: {'Smile': 0.35506552}, 6: {'Smile': 0.35424682}, 7: {'Smile': 0.3941398}, 8: {'Smile': 0.41692236}, 9: {'Smile': 0.38992262}, 10: {'Smile': 0.33604342}, 11: {'Smile': 0.44526315}, 12: {'Smile': 0.38967356}, 13: {'Smile': 0.46438512}, 14: {'Smile': 0.33246452}, 15: {'Smile': 0.34840274}, 16: {'Smile': 0.34378657}, 17: {'Smile': 0.33653626}, 18: {'Smile': 0.48442918}, 19: {'Smile': 0.53641176}, 20: {'Smile': 0.531845}, 21: {'Smile': 0.44345507}, 22: {'Smile': 0.33793026}, 23: {'Smile': 0.33024272}, 24: {'Smile': 0.35893732}, 25: {'Smile': 0.35307083}, 26: {'Smile': 0.35426182}, 27: {'Smile': 0.36865106}, 28: {'Smile': 0.3226741}}
//convertDataToChart('Smile', jsonData);