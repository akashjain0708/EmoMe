var createRadarChart = function(cand1,cand2,cand3,cand4,cand5,chartID){
    var ctx = document.getElementById(chartID);
    var radarChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: ["Angry","Happy","Fear","Surprised","Sad"],
            datasets:[
                {
                    label: "Candidate 1",
                    backgroundColor: "rgba(82, 26, 186, 0.8)",
                    borderColor: "rgba(82, 26, 186, 1)",
                    pointBackgroundColor: "rgba(82, 26, 186, 1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(82, 26, 186, 1)",
                    data: cand1
                },
                {
                    label: "Candidate 2",
                    backgroundColor: "rgba(160, 155, 170, 0.6)",
                    borderColor: "rgba(160, 155, 170, 1)",
                    pointBackgroundColor: "rgba(160, 155, 170, 1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(160, 155, 170, 1)",
                    data: cand2
                },
                {
                    label: "Candidate 3",
                    backgroundColor: "rgba(255, 160, 251, 0.5)",
                    borderColor: "rgba(255, 160, 251, 1)",
                    pointBackgroundColor: "rgba(255, 160, 251, 1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(255, 160, 251, 1)",
                    data: cand3
                },
                {
                    label: "Candidate 4",
                    backgroundColor: "rgba(255, 252, 122, 0.4)",
                    borderColor: "rgba(255, 252, 122, 1)",
                    pointBackgroundColor: "rgba(255, 252, 122, 1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(255, 252, 122, 1)",
                    data: cand4
                },
                {
                    label: "Candidate 5",
                    backgroundColor: "rgba(137, 242, 121, 0.2)",
                    borderColor: "rgba(137, 242, 121, 1)",
                    pointBackgroundColor: "rgba(137, 242, 121, 1)",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(137, 242, 121, 1)",
                    data: cand5
                }
            ]
        },
        options:{

        }
    });
};


var means = {'candidate1':[44.189026367898154,38.95985128892452,41.489440996399596,31.42052784188115,36.07731298739554], 
'candidate2':[47.29818240604992,31.78755582670416,40.1774693682167,41.04337894074965,44.399468039827916], 
'candidate3':[36.63659336124626,45.69623042014987,38.902848826559226,48.41636807005666,36.41018893488894],
'candidate4':[43.686052288310745,24.07434158692435,41.64041390829151,37.76943822720839,41.61740466384932],
'candidate5':[43.726476744207704,36.024121556146976,43.095816095527734,34.08776591816049,38.34814250675056]}

createRadarChart(means['candidate1'],means['candidate2'],means['candidate3'],means['candidate4'],means['candidate5'],'radarChart');
