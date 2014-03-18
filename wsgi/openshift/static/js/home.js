$(document).ready(function(){
	
	$("#list").click(function(e) {
        	$.ajax({
		type:"GET",
		url:"/list",
		success:loadlist,
		dataType:'html'		
		})
    	});
	
	 $("#new").click(function(e) {
        	$.ajax({
		type:"GET",
		url:"/new",
		success:newform,
		dataType:'html'		
		})
    	});
	$("#submit").click(function(e) {
		var a=$('#id_title').val();
		var b=$('#id_info').val();
		var c=$('#id_tag').val();
        	$.ajax({
		type:"POST",
		url:"/new",
		data:{'title':a,'info':b,'tag':c,'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val()},
		success:calllist,		
		dataType:'html'
		 		
		})
		
    	});
	$("#search").keyup(function(e) {
			$('#result').show();		
			$.ajax({
			type:"POST",
			url:"/search/",
			data:{'title':$('input[name=search]').val(),'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val()},
			success:callsearch,		
			dataType:'html'
		})
		
    	});

	$("#id_info").keyup(function(e) {
		$('#preview').show();		
		$.ajax({
		type:"POST",
		url:"/preview/",
		data:{'info':$('#id_info').val(),'title':$('#id_title').val(),'tag':$('#id_tag').val(),'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val()},
		success:callpreview,		
		dataType:'html'
		 		
		})
		
    	});

	$("#id_title").keyup(function(e) {
		$('#preview').show();		
		$.ajax({
		type:"POST",
		url:"/preview/",
		data:{'info':$('#id_info').val(),'title':$('#id_title').val(),'tag':$('#id_tag').val(),'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val()},
		success:callpreview,		
		dataType:'html'
		 		
		})
		
    	});
	
	$("#id_tag").keyup(function(e) {
		$('#preview').show();		
		$.ajax({
		type:"POST",
		url:"/preview/",
		data:{'info':$('#id_info').val(),'title':$('#id_title').val(),'tag':$('#id_tag').val(),'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val()},
		success:callpreview,		
		dataType:'html'
		 		
		})
		
    	});
});
function callpreview(data){
	$('#preview').html(data);
}
function callsearch(data){
		$('#result').html(data);

}
function newform(data)
{
	$('#infoform').html(data);
}
function calllist(){
	$("#list").click();
}
function loadlist(data)
{
	$('#work').html(data);
}
