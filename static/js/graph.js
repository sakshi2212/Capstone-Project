// Pie Charts
var colorBackground = [
  "#581845",
  "#93007d",
  "#900C35",
  "#c70039",
  "#d10667",
  "#e72b59",
  "#f74a48",
  "#ff6936",
  "#ff5733",
  "#ff8821",
  "#ffc300",
  "#aebf18",
  "#61b241",
  "#009f61",
  "#008977",
  "#00717d",
];

$.ajax({
  method: "GET",
  url: "india-category-count-chart",
  success: function (data) {
    var config = {
      type: "doughnut",
      data: {
        datasets: [
          {
            data: data.data,
            backgroundColor: colorBackground,
          },
        ],
        labels: data.labels,
      },
      options: {
        title: {
          display: true,
          text: "No of trending videos in a Particular Category",
        },
        legend: {
          display: false,
        },
        responsive: true,
      },
    };

    var ctx = document.getElementById("category-count-chart").getContext("2d");
    new Chart(ctx, config);
  },
  error: function (error_data) {
    console.log(error_data);
  },
});

$.ajax({
  method: "GET",
  url: "india-most-trending-channel",
  success: function (data) {
    // console.log(data.data_likes);
    var config = {
      type: "bar",
      data: {
        labels: data.labels,
        datasets: [
          {
            backgroundColor: colorBackground,
            label: "Channels",
            data: data.data,
          },
        ],
      },
      options: {
        title: {
          display: true,
          text: "Most trending Channels",
        },
      },
    };

    var ctx = document.getElementById("most-trending-channel").getContext("2d");
    new Chart(ctx, config);
  },
  error: function (error_data) {
    console.log(error_data);
  },
});