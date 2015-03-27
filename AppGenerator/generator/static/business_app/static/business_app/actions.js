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
	        var json = JSON.stringify(data);
	        	alert(json);
	        	alert(data["hello"]);
	        },
	        error: function(){
	        	alert("error");
	        }
		});
	}
}