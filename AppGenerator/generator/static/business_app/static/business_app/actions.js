$(document).ready(function() {
    $('#datepicker').datepicker();
});

$(function () { 
	$("[data-toggle='tooltip']").tooltip(); 
});

window.onload = function(){
	var placeholder = document.getElementById("placeHolder");
	if(placeholder != null){
		$.ajax({
	    	type: 'GET',
	        dataType: 'json',
	        data : {
	        	'pk' : '1'
	        },
	        url: '/visuals/',
	        success: function(data){
	        	var graph = data["graph"];
	        	
	        	for(var index in graph){
	        		$("#graph").append("<canvas id='" + index +"' height='100'></canvas>");
	        		var ctx = document.getElementById(index).getContext("2d");
					window.index = new Chart(ctx).Line(graph[index], {
						responsive: true
					});
	        	}
	   			
	        },
	        error: function(){
	        	alert("error");
	        }
		});
	}
}