/**
 * Created by Akash on 11/19/2016.
 */

var createChart = function (xLabels, yPoints, yPoints_2, yPoints_3, chartID, borderColor, pointColor, hoverBackColor, hoverBorderColor, label, xLabelString, yLabelString) {

    console.log(xLabels);
    console.log(yPoints);

    var ctx = document.getElementById(chartID);
    console.log(ctx);
    var lineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: xLabels,
            datasets: [{
                data: yPoints,
                fill: false,
                borderColor: "#d30845",
                pointBackgroundColor: pointColor,
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: hoverBackColor,
                pointHoverBorderColor: hoverBorderColor,
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                label: "Smile"
            }, {
                data: yPoints_2,
                fill: false,
                borderColor: "#33701a",
                pointBackgroundColor: pointColor,
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: hoverBackColor,
                pointHoverBorderColor: hoverBorderColor,
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                label: "Sad"
            }, {
                data: yPoints_3,
                fill: false,
                borderColor: "#ff442b",
                pointBackgroundColor: pointColor,
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: hoverBackColor,
                pointHoverBorderColor: hoverBorderColor,
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                label: "Anger"
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: xLabelString
                    }
                }],
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: yLabelString
                    }
                }]
            }
        }
    });
};

var createPolarChart = function(happyVal, sadVal, angerVal, fearVal, surpriseVal, chartID){
    var ctx = document.getElementById(chartID);
    var polarChart = new Chart(ctx,{
        type: 'polarArea',
        data: {
            labels: ['Happy','Sad','Angry','Surprised','Fear'],
            datasets: [{
                data: [happyVal, sadVal, angerVal, surpriseVal, fearVal],
                backgroundColor: ["#d30845", "#33701a", "#ff442b", "#0a96b2", "#3c187f"]
            }]
        },
        options: {
            animateRotate: true,
            animateScale: true,
        }
    });
};

var createRadarChart = function(cand1,cand2,cand3,cand4,cand5,chartID){
    var ctx = document.getElementById(chartID);
    var radarChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: ["Happy","Sad","Angry","Surprised","Fear"],
            datasets:[
                {
                    label: "Candidate 1",
                    backgroundColor: "rgb(82, 26, 186, 0.2)",
                    borderColor: "rgb(82, 26, 186, 1)",
                    pointBackgroundColor: "rgb(82, 26, 186, 1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgb(82, 26, 186, 1)",
                    data: cand1
                },
                {
                    label: "Candidate 2",
                    backgroundColor: "rgb(160, 155, 170, 0.2)",
                    borderColor: "rgb(160, 155, 170, 1)",
                    pointBackgroundColor: "rgb(160, 155, 170, 1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgb(160, 155, 170, 1)",
                    data: cand2
                },
                {
                    label: "Candidate 3",
                    backgroundColor: "rgb(255, 160, 251, 0.2)",
                    borderColor: "rgb(255, 160, 251, 1)",
                    pointBackgroundColor: "rgb(255, 160, 251, 1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgb(255, 160, 251, 1)",
                    data: cand3
                },
                {
                    label: "Candidate 4",
                    backgroundColor: "rgb(255, 252, 122, 0.2)",
                    borderColor: "rgb(255, 252, 122, 1)",
                    pointBackgroundColor: "rgb(255, 252, 122, 1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgb(255, 252, 122, 1)",
                    data: cand4
                },
                {
                    label: "Candidate 5",
                    backgroundColor: "rgb(137, 242, 121, 0.2)",
                    borderColor: "rgb(137, 242, 121, 1)",
                    pointBackgroundColor: "rgb(137, 242, 121, 1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgb(137, 242, 121, 1)",
                    data: cand5
                }
            ]
        },
        options:{

        }
    });
};

var getXYPoints = function(label, dataSet) {
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
    return [xLabels, yPoints];
};

// var dataset = $('#dataSetDiv').attr('val');
[x1, y1] = getXYPoints('Smile', dataSetJson);
[x2, y2] = getXYPoints('sad', dataSetJson);
[x1, y1] = getXYPoints('Smile', dataSetJson);
[x3, y3] = getXYPoints('Anger', dataSetJson);

// createChart(x2, y2, "sadChart","rgba(75,192,192,1)" ,"#fff", "rgba(75,192,192,1)", "rgba(220,220,220,1)" , 'Smile', 'Time', 'Happiness');



// var barChartData = {
//     labels : getXYPoints('Smile', dataSetJson)[0],
//     datasets : [
//         {
//             fillColor : "rgba(220,220,220,0.5)",
//             strokeColor : "rgba(220,220,220,0.8)",
//             highlightFill: "rgba(220,220,220,0.75)",
//             highlightStroke: "rgba(220,220,220,1)",
//             data : getXYPoints('Smile', dataSetJson)[1]
//         }
//     ]

// };

// var barChartData2 = {
//     labels : getXYPoints('sad', dataSetJson)[0],
//     datasets : [
//         {
//             fillColor : "rgba(220,220,220,0.5)",
//             strokeColor : "rgba(220,220,220,0.8)",
//             highlightFill: "rgba(220,220,220,0.75)",
//             highlightStroke: "rgba(220,220,220,1)",
//             data : getXYPoints('sad', dataSetJson)[1]
//         }
//     ]

// };



// window.onload = function(){
//     // s1 = getXYPoints('Smile', dataSetJson);
//     // s2 = getXYPoints('sad', dataSetJson);

//     var ctx = document.getElementById("smileChart").getContext("2d");
//     window.myBar = new Chart(ctx).Line(barChartData, {
//         responsive : true
//     });
//     var ctx2 = document.getElementById("sadChart").getContext("2d");
//     window.myBar = new Chart(ctx2).Line(barChartData2, {
//         responsive : true
//     });
// }



createChart(x1, y1, y2, y3, "smileChart","rgba(75,192,192,1)" ,"#fff", "rgba(75,192,192,1)", "rgba(220,220,220,1)" , 'Smile', 'Time', 'Happiness');
// createChart(x2, y2, "sadChart","rgba(75,192,192,1)", "#fff", "rgba(75,192,192,1)" , "rgba(220,220,220,1)" , 'Sad', 'Time', 'Sadness');

//var jsonData = {0: {'Smile': 0.50381887}, 1: {'Smile': 0.5244584}, 2: {'Smile': 0.37471813}, 3: {'Smile': 0.3662309}, 4: {'Smile': 0.38467777}, 5: {'Smile': 0.35506552}, 6: {'Smile': 0.35424682}, 7: {'Smile': 0.3941398}, 8: {'Smile': 0.41692236}, 9: {'Smile': 0.38992262}, 10: {'Smile': 0.33604342}, 11: {'Smile': 0.44526315}, 12: {'Smile': 0.38967356}, 13: {'Smile': 0.46438512}, 14: {'Smile': 0.33246452}, 15: {'Smile': 0.34840274}, 16: {'Smile': 0.34378657}, 17: {'Smile': 0.33653626}, 18: {'Smile': 0.48442918}, 19: {'Smile': 0.53641176}, 20: {'Smile': 0.531845}, 21: {'Smile': 0.44345507}, 22: {'Smile': 0.33793026}, 23: {'Smile': 0.33024272}, 24: {'Smile': 0.35893732}, 25: {'Smile': 0.35307083}, 26: {'Smile': 0.35426182}, 27: {'Smile': 0.36865106}, 28: {'Smile': 0.3226741}}
//convertDataToChart('Smile', jsonData);

createPolarChart(percentageJson['Smile'],percentageJson['sad'],percentageJson['Anger'],percentageJson['Fear'],percentageJson['Surprise'],'polarChart');

createRadarChart(means['candidate1'],means['candidate2'],means['candidate3'],means['candidate4'],means['candidate5'],'radarChart');