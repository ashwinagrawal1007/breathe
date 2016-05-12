$.get('/chart_json?sensor_id=' + sensorId, function (data) {
    
    data = JSON.parse(data);
    
	var data_nitrogen_dioxide = _.object(_.map(data, function(item) {
        return [item['timestamp'], item['data']['nitrogen dioxide']]
                         }))

      var chartData = {
          labels: _.keys(data_nitrogen_dioxide),
          datasets: [
              {
                  label: "nitrogen dioxide",
                  fillColor: "rgba(220,20,20,0.2)",
                  strokeColor: "rgba(220,20,20,1)",
                  pointColor: "rgba(220,20,20,1)",
                  pointStrokeColor: "#fff",
                  pointHighlightFill: "#fff",
                  pointHighlightStroke: "rgba(220,220,220,1)",
                  data: _.values(data_nitrogen_dioxide)
              }]
      };
      var ctx = document.getElementById("nitrogen_dioxide").getContext("2d");
      var myLineChart = new Chart(ctx).Line(chartData);

	 
 	var data_hydrogen_sulfide = _.object(_.map(data, function(item) {
         return [item['timestamp'], item['data']['hydrogen sulfide']]
                          }))

       var chartData = {
           labels: _.keys(data_hydrogen_sulfide),
           datasets: [
               {
                   label: "hydrogen sulfide",
                   fillColor: "rgba(290,220,0,0.2)",
                   strokeColor: "rgba(290,220,0,1)",
                   pointColor: "rgba(290,220,0,1)",
                   pointStrokeColor: "#fff",
                   pointHighlightFill: "#fff",
                   pointHighlightStroke: "rgba(220,220,220,1)",
                   data: _.values(data_hydrogen_sulfide)
               }]
       };
       var ctx = document.getElementById("hydrogen_sulfide").getContext("2d");
       var myLineChart = new Chart(ctx).Line(chartData);
	   
    var data_sulphur_dioxide = _.object(_.map(data, function(item) {
         return [item['timestamp'], item['data']['sulphur dioxide']]
                          }))

       var chartData = {
           labels: _.keys(data_sulphur_dioxide),
           datasets: [
               {
                   label: "sulphur dioxide",
                   fillColor: "rgba(10,330,100,0.2)",
                   strokeColor: "rgba(10,330,100,1)",
                   pointColor: "rgba(10,330,100,1)",
                   pointStrokeColor: "#fff",
                   pointHighlightFill: "#fff",
                   pointHighlightStroke: "rgba(220,220,220,1)",
                   data: _.values(data_sulphur_dioxide)
               }]
       };
       var ctx = document.getElementById("sulphur_dioxide").getContext("2d");
       var myLineChart = new Chart(ctx).Line(chartData); 
	  
	  
    var data_carbon_monoxide = _.object(_.map(data, function(item) {
         return [item['timestamp'], item['data']['carbon monoxide']]
                          }))

       var chartData = {
           labels: _.keys(data_carbon_monoxide),
           datasets: [
               {
                   label: "carbon monoxide",
                   fillColor: "rgba(20,20,330,0.2)",
                   strokeColor: "rgba(20,20,330,1)",
                   pointColor: "rgba(20,20,330,1)",
                   pointStrokeColor: "#fff",
                   pointHighlightFill: "#fff",
                   pointHighlightStroke: "rgba(220,220,220,1)",
                   data: _.values(data_carbon_monoxide)
               }]
       };
       var ctx = document.getElementById("carbon_monoxide").getContext("2d");
       var myLineChart = new Chart(ctx).Line(chartData); 	     
	   
      })

