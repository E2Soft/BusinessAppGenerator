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
	        	//popunjava se graf panel
	        	var graph = data["graph"];
	        	
	        	for(var index in graph){
	        		$("#graph").append("<canvas id='" + index +"' height='100'></canvas>");
	        		var ctx = document.getElementById(index).getContext("2d");
					window.index = new Chart(ctx).Line(graph[index], {
						responsive: true
					});
	        	}
	        	
	        	//popunjavam levi panel
	        	var left = data["left"];
	        	
	        	var counter = 0;
	        	
	        	for(var index in left){
	        		var prop = left[index];//elem
	        		
	        		$("#leftPanel").append("<div class='box'><ul class='list-group' id='box" + counter + "'>");
	        		for(var i in prop){
	        			if(i != "title"){
	        				$("#box"+counter).append("<li class='list-group-item'><span class='glyphicon glyphicon-chevron-right'></span> "+prop[i]+"</li>");
	        			}else{
	        				$("#box"+counter).append("<li class='list-group-item list-group-item-info'><b><span class='glyphicon glyphicon-certificate'></span><a href='"+prop[i][1]+"'> "+prop[i][0]+"</a></b></li>");
	        			}
	        		}
	        		$("#leftPanel").append("</ul></div>");
	        		counter++;
	        	}
	   			counter++;
	   			
	   			//popuni centralni panel
	   			var centar = data["centar"];
	        	
	        	for(var index in centar){
	        		var prop = centar[index];//elem
	        		
	        		$("#centarPanel").append("<div class='box'><ul class='list-group' id='box" + counter + "'>");
	        		for(var i in prop){
	        			if(i != "title"){
	        				$("#box"+counter).append("<li class='list-group-item'><span class='glyphicon glyphicon-chevron-right'></span> "+prop[i]+"</li>");
	        			}else{
	        				$("#box"+counter).append("<li class='list-group-item list-group-item-info'><b><span class='glyphicon glyphicon-certificate'></span><a href='"+prop[i][1]+"'> "+prop[i][0]+"</a></b></li>");
	        			}
	        		}
	        		$("#centarPanel").append("</ul></div>");
	        		counter++;
	        	}
	   			counter++;
	   			
	   			//popuni desni panel
	   			var right = data["right"];
	        	
	        	for(var index in right){
	        		var prop = right[index];//elem
	        		
	        		$("#rightPanel").append("<div class='box'><ul class='list-group' id='box" + counter + "'>");
	        		for(var i in prop){
	        			if(i != "title"){
	        				$("#box"+counter).append("<li class='list-group-item'><span class='glyphicon glyphicon-chevron-right'></span> "+prop[i]+"</li>");
	        			}else{
	        				$("#box"+counter).append("<li class='list-group-item list-group-item-info'><b><span class='glyphicon glyphicon-certificate'></span><a href='"+prop[i][1]+"'> "+prop[i][0]+"</a></b></li>");
	        			}
	        		}
	        		$("#rightPanel").append("</ul></div>");
	        		counter++;
	        	}
	   			counter++;
	        },
	        error: function(){
	        	alert("error");
	        }
		});
	}
}