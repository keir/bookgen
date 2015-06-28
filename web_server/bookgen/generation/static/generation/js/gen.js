
function tripleToRGB(triple, opacity) {
  if (opacity) {
    return 'rgb(' + triple[0] + ', ' +
                    triple[1] + ', ' +
                    triple[2] + ', ' +
                    opacity + ')';
  }
  return 'rgb(' + triple[0] + ', ' +
                  triple[1] + ', ' +
                  triple[2] + ')';
}


$(document).ready(function(){
        var colorThief = new ColorThief();
	var $img = $('#image');
        $img[0].crossOrigin = "Anonymous";

	$img.on('load', function(){
		var height = $img.height();
		
		var padding = Math.floor(Math.random() * (15));
		$img.css({'padding': padding + 'px'});

                var palette = colorThief.getPalette($img[0], 8)
	
		$('#title').css({'font-color': tripleToRGB(palette[0])});
		$('#title').css({'background-color': tripleToRGB(palette[1])});

		
		if (height > 550) {
			var less = height - 100;
			$('#title').css({'position': 'relative', 'top': '-' + less + 'px'});
			$('#title').css({'background-color': '#ffffff'});
			var opacity = (Math.random() * (1.0 - 0.50) + 0.50).toFixed(4);
			$('#title').css({'background-color': 'rgba(255,255,255,' + opacity + ')'});

                        $('#title').css({'font-color': tripleToRGB(palette[0])});
                        $('#title').css({'background-color': tripleToRGB(palette[1], opacity)});
			
			var border_thickness = Math.floor(Math.random() * (5));
			var border_radius = Math.floor(Math.random() * (12));

			var opacity_border = (Math.random() * (1.0 - 0.10) + 0.10).toFixed(4);
			$('#title').css({'border-radius': border_radius + 'px'});
			$('#title').css({'box-shadow': '0px 0px 0px ' + border_thickness + 'px rgba(0,0,0,' + opacity_border + ')'});
			
			$('#author').css({'position': 'relative', 'top': '-' + (less - 100) + 'px'});
			$('#author').css({'background-color': '#ffffff'});
			$('#author').css({'background-color': 'rgba(255,255,255,' + opacity + ')'});

			$('#book').css({'height': height + 14});
		} else {
			var border_radius = Math.floor(Math.random() * (12));

			$('#title').css({'border-radius': border_radius + 'px'});
			
					var img_border_radius = Math.floor(Math.random() * (4));
		
		if (img_border_radius == 1) {
			$img.addClass('img-rounded');
		}
		if (img_border_radius == 2) {
			$img.addClass('img-polaroid');
		}
		if (img_border_radius == 3) {
			$img.addClass('img-circle');
		}
			
		}
		
		var div_height = $('#book').height();
		if (div_height < 650) {
			$('#book').css({'height': 650});
		} 
		
		if ($('#title').height() > 400) {
			$('#title').css({'font-size': '60px'});
			if ($('#title').height() > 400) {
				$('#title').css({'font-size': '50px'});
			}
		}
		if ($('#title').offsetWidth < $('#title').scrollWidth) {
			$('#title').css({'font-size': '50px'});
		}
	  
	});

	
});
