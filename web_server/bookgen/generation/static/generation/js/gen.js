


$(document).ready(function(){
	
	
	var $img = $('#image');

	$img.on('load', function(){
		var height = $img.height();
		console.log(height);
		if (height > 550) {
			var less = height - 100;
			$('#title').css({'position': 'relative', 'top': '-' + less + 'px'});
			$('#author').css({'position': 'relative', 'top': '-' + less + 'px'});
			if (height < 670) {
				$('#book').css({'height': 670});
				var margin = (670 - height)/2;
				$('#image').css({'position': 'relative', 'top': margin + 'px'});
			} else {
				$('#book').css({'height': height});
			}
		}
	  
	});

	
});