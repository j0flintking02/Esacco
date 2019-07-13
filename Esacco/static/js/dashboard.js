
(function($) {
  const totalShare={};
  const totalPayments={};
  const totalRequest={};
  let total= 0;
  Object.keys(value).map((key)=>{
    const sm = value[key];
    sm.forEach((i)=>{
      total+=i;
      totalShare[key]=total;
    });
    total=0;
  });

  Object.keys(pay_value).map((key)=>{
    const pay = pay_value[key];
    pay.forEach((i)=>{
      total+=i;
      totalPayments[key]=total;
    });
    total=0;
  });
  Object.keys(request_value).map((key)=>{
    const pay = request_value[key];
    pay.forEach((i)=>{
      total+=i;
      totalRequest[key]=total;
    });
    total=0;
  });

  const updateValues=((obj)=>{
    let values=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    for (let counter = 0; counter < Object.keys(obj).length; counter++) {
      Object.keys(obj).map((key)=>{
      switch (key) {
        case 'Jan':
          values[0]=obj[key];
          break;
        case 'Feb':
          values[1]=obj[key];
          break;
        case 'Mar':
          values[2]=obj[key];
          break;
        case 'Apr':
          values[3]=obj[key];
          break;
        case 'May':
          values[4]=obj[key];
          break;
        case 'June':
          values[5]=obj[key];
          break;
        case 'July':
          values[6]=obj[key];
          break;
        case 'Aug':
          values[7]=obj[key];
          break;
        case 'Sept':
          values[8]=obj[key];
          break;
        case 'Oct':
          values[9]=obj[key];
          break;
        case 'Nov':
          values[10]=obj[key];
          break;
        case 'Dec':
          values[11]=obj[key];
          break;
        default:
      }
      });
    }
    return values
  });
  $(function() {
    const dataBar = {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Nov","Dec"],
      datasets: [{
        label: 'Customers',
        data: updateValues(totalShare),
        backgroundColor: [
          '#fc381d',
          '#fc381d',
          '#fc381d',
          '#fc381d',
          '#fc381d',
          '#fc381d',
          '#fc381d',
          '#fc381d',
          '#fc381d',
          '#fc381d',
          '#fc381d',
          '#fc381d',
        ],
        borderColor: [
          '#dee5ef',
          '#fc381d',
        ],
        borderWidth: 1,
        fill: false
      }]
    };
    var optionsBar = {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true,
            display: false,

          },
          gridLines: {
            display: false,
            drawBorder: false
          }
        }],
        xAxes: [{
          ticks: {
            beginAtZero: true,
            display: false,
          },
          gridLines: {
            display: false,
            drawBorder: false
          }
        }]
      },
      legend: {
        display: false
      },
      elements: {
        point: {
          radius: 0
        }
      },
      tooltips: {
        enabled: false
      }

    };
    if ($("#customers").length) {
      var barChartCanvas = $("#customers").get(0).getContext("2d");
      // This will get the first returned node in the jQuery collection.
      var ctx = document.getElementById("customers");
      ctx.height = 60;
      var barChart = new Chart(barChartCanvas, {
        type: 'bar',
        data: dataBar,
        options: optionsBar
      });
    }
    const dataBarOrder = {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Nov","Dec"],
      datasets: [{
        label: 'Payments',
        data: updateValues(totalPayments),
        backgroundColor: [
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
        ],
        borderColor: [
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
          '#51c81c',
        ],
        borderWidth: 1,
        fill: false
      }]
    };
    var optionsBarOrder = {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true,
            display: false,

          },
          gridLines: {
            display: false,
            drawBorder: false
          }
        }],
        xAxes: [{
          ticks: {
            beginAtZero: true,
            display: false,
          },
          gridLines: {
            display: false,
            drawBorder: false
          }
        }]
      },
      legend: {
        display: false
      },
      elements: {
        point: {
          radius: 0
        }
      },
      tooltips: {
        enabled: false
      }

    };
    if ($("#orders").length) {
      var barChartCanvas = $("#orders").get(0).getContext("2d");
      // This will get the first returned node in the jQuery collection.
      var ctx = document.getElementById("orders");
      ctx.height = 60;
      var barChart = new Chart(barChartCanvas, {
        type: 'bar',
        data: dataBarOrder,
        options: optionsBarOrder
      });
    }
    var webAudienceMetricsSatackedData = {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Nov","Dec"],
      datasets: [
        {
          label: 'Shares',
          data: updateValues(totalShare),
          backgroundColor: [
            '#3794fc','#3794fc','#3794fc','#3794fc','#3794fc','#3794fc','#3794fc','#3794fc',
          ],
          borderColor: [
            '#3794fc','#3794fc','#3794fc','#3794fc','#3794fc','#3794fc','#3794fc','#3794fc',
          ],
          borderWidth: 1,
          fill: false
        },
        {
        label: 'Payments',
        data: updateValues(totalPayments),
        backgroundColor: [
          '#a037fc',
          '#a037fc',
          '#a037fc',
          '#a037fc',
          '#a037fc',
          '#a037fc',
          '#a037fc',
          '#a037fc',
        ],
        borderColor: [
          '#a037fc',
          '#a037fc',
          '#a037fc',
          '#a037fc',
          '#a037fc',
          '#a037fc',
          '#a037fc',
          '#a037fc',
        ],
        borderWidth: 1,
        fill: false
      },
      {
        label: 'Loans',
        data: updateValues(totalRequest),
        backgroundColor: [
          '#dee5ef','#dee5ef','#dee5ef','#dee5ef','#dee5ef','#dee5ef','#dee5ef','#dee5ef',
        ],
        borderColor: [
          '#dee5ef','#dee5ef','#dee5ef','#dee5ef','#dee5ef','#dee5ef','#dee5ef','#dee5ef',
        ],
        borderWidth: 1,
        fill: false
      },]
    };
    var webAudienceMetricsSatackedOptions = {
      scales: {
        xAxes: [{
          barPercentage: 0.2,
          stacked: true,
          gridLines: {
            display: true, //this will remove only the label
						drawBorder: false,
						color: "#e5e9f2",
          },
        }],
        yAxes: [{
          stacked: true,
					display: false,
					gridLines: {
            display: false, //this will remove only the label
            drawBorder: false
          },
        }]
      },
      legend: {
        display: false,
        position: "bottom"
      },
      legendCallback: function(chart) {
				var text = [];
        text.push('<div class="row">');
        for (var i = 0; i < chart.data.datasets.length; i++) {
          const chartData = chart.data.datasets[i].data;

          for (const i of chartData) {
          total+=i;
          }
          text.push('<div class="col-lg-4">' +
              '<div class="row">' +
                '<div class="col-sm-12">' +
                  '<h5 class="font-weight-bold text-dark mb-1">'+ total.toLocaleString() + '</h5>' +
                '</div>' +
              '</div>' +
              '<div class="row align-items-center">' +
                '<div class="col-2">' +
                  '<span class="legend-label" style="background-color:' + chart.data.datasets[i].backgroundColor[i] + '"></span>' +
                '</div>' +
                '<div class="col-9 pl-0">' +
                  '<p class="text-muted m-0 ml-1">' + chart.data.datasets[i].label + '</p>' +
                '</div>' +
              '</div>');
          text.push('</div>');
          total = 0;
        }
        text.push('</div>');
        return text.join("");
      },
      elements: {
        point: {
          radius: 0
        }
      }
    };
    if ($("#web-audience-metrics-satacked").length) {
      var barChartCanvas = $("#web-audience-metrics-satacked").get(0).getContext("2d");
      // This will get the first returned node in the jQuery collection.
      var ctx = document.getElementById("web-audience-metrics-satacked");
      ctx.height = 88;
      var barChart = new Chart(barChartCanvas, {
        type: 'bar',
        height: '200',
        data: webAudienceMetricsSatackedData,
        options: webAudienceMetricsSatackedOptions
      });
      document.getElementById('chart-legends').innerHTML = barChart.generateLegend();
		}
  });
})(jQuery);